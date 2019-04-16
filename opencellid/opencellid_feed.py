"""Manage OpenCellID feed."""
import csv
import gzip
import logging
import os
import re
import shutil

import requests


logging.basicConfig(level=logging.DEBUG)


class OpenCellIdFeed(object):
    """OpenCellID feed abstraction.

    Args:
        ocid_dir_path (str): Directory path for placing OpenCellID feed.
        ocid_api_key (str): Optional. If set, we attempt to use the OpenCellID
            feed. Otherwise, we retrieve the feed from Mozilla Location
            Services.
    """

    def __init__(self, ocid_dir_path, ocid_api_key=None):
        """Initialize the feed."""
        self.debug = False
        self.ocid_dir_path = ocid_dir_path
        self.ocid_api_key = ocid_api_key
        self.ocid_feed_file = os.path.join(ocid_dir_path, "cell_towers.csv.gz")
        self.ul_base = "https://opencellid.org/ocid/downloads"
        self.mls_dl_page = "https://location.services.mozilla.com/downloads"

    def __iter__(self):
        """Yield dict objects for each row in the feed."""
        with gzip.open(self.ocid_feed_file, 'rt') as feed_data:
            consumer = csv.DictReader(feed_data)
            for row in consumer:
                yield row

    def update_feed(self):
        """Update OpenCellID DB from remote source.

        If the OpenCellID API key is configured when instantiating this class,
        the update will come from Unwired Labs.  Otherwise, it will come from
        Mozillla Location Services (MLS)

        Downloads to a temp file first, and moves into place if download is
        successful.
        """
        log = logging.getLogger('feed_updater')
        if self.ocid_api_key is not None:
            params = {"token": self.ocid_api_key, "file": "cell_towers.csv.gz"}
            response = requests.get(self.ul_base, params=params, stream=True)
            feed_source = "Unwired Labs"
        else:
            target_url = self.pick_ocid_url_from_list(
                self.get_ocid_urls_from_mls_page())
            response = requests.get(target_url, stream=True)
            feed_source = "Mozilla Location Services"
        temp_file = self.ocid_feed_file.replace('csv.gz', 'csv.gz.tmp')
        if self.debug:
            log.debug("Updating OpenCellID feed from %s.", feed_source)
        totes_chunks = 0
        with open(temp_file, 'wb') as feed_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    feed_file.write(chunk)
                    totes_chunks += 1024
                    if self.debug and totes_chunks % 1000000 == 0:
                        log.debug("Downloaded %s from "
                                  "%s...", totes_chunks, feed_source)
        try:
            with gzip.open(temp_file, 'rt') as feed_data:
                consumer = csv.DictReader(feed_data)
                _unused = consumer.fieldnames
            shutil.move(temp_file, self.ocid_feed_file)
            log.debug("OCID feed file written to %s", self.ocid_feed_file)
        except IOError:
            rate_limit = 'RATE_LIMITED'
            bad_token = 'INVALID_TOKEN'
            with open(temp_file, 'r') as eggs_erroneous:
                contents = eggs_erroneous.readline()
            if rate_limit in contents:
                logging.error("Feed did not update. You're rate-limited!")
            elif bad_token in contents:
                logging.error("API token rejected by Unwired Labs!!")
            else:
                logging.error("Non-specific error.  Details in %s", temp_file)
            raise

    def get_ocid_urls_from_mls_page(self):
        """Extract OCID urls from MLS downloads page."""
        dl_page_contents = requests.get(self.mls_dl_page).text
        targets = []
        rxmatch = r'https://[A-Za-z0-9]+\.cloudfront\.net/export/MLS-full-cell-export-\d{4}-\d{2}-\d{2}T\d+\.csv.gz'  # NOQA
        for line in dl_page_contents.splitlines():
            matches = re.findall(rxmatch, line)
            if matches:
                targets.extend(matches)
        return targets

    def pick_ocid_url_from_list(self, url_list):
        """Gets the link to the most recent MLS download"""
        date_struct = {}
        date_list = []
        for url in url_list:
            d = re.findall(r'\d{4}-\d{2}-\d{2}T\d+', url)[0]
            date_struct[d] = url
            date_list.append(d)
        target = sorted(date_list)[-1]
        return date_struct[target]
