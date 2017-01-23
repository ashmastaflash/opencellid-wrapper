import csv
import gzip
import os
import requests
import shutil

class OpenCellIdFeed(object):
    def __init__(self, ocid_dir_path, ocid_api_key):
        self.ocid_dir_path = ocid_dir_path
        self.ocid_api_key = ocid_api_key
        self.ocid_feed_file = os.path.join(ocid_dir_path, "cell_towers.csv.gz")

    def __iter__(self):
        """Yields dict objects for each row in the feed"""
        with gzip.open(self.ocid_feed_file, 'r') as feed_data:
            consumer = csv.DictReader(feed_data)
            for row in consumer:
                yield row

    @classmethod
    def build_ocid_url(cls, api_key):
        """Builds OpenCellID download URL"""
        base = "http://opencellid.org/downloads/?"
        file_name = "cell_towers.csv.gz"
        return "%sapiKey=%s&filename=%s" % (base, api_key, file_name)

    def update_from_web(self):
        """Updates OpenCellID file from web.

        Downloads to a temp file first, and moves into place if download is
        successful.

        """
        payload = {"key": self.ocid_api_key}
        url = OpenCellIdFeed.build_ocid_url(self.ocid_api_key)
        response = requests.post(url, data=payload, stream=True)
        temp_file = self.ocid_feed_file.replace('csv.gz', 'csv.gz.tmp')
        print("Updating OpenCellID feed from web.")
        with open(temp_file, 'wb') as feed_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    feed_file.write(chunk)
        shutil.move(temp_file, self.ocid_feed_file)
        print("OCID feed file written to %s" % self.ocid_feed_file)
