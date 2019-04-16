import logging
import os

import opencellid

herepath = os.path.dirname(os.path.abspath(__file__))
integrations_path = os.path.join(herepath, "../fixtures")

logging.basicConfig(level=logging.DEBUG)

class TestIntagrationOpenCellIdFeed:
    def instantiate_opencellid_feed_object(self):
        api_key = os.getenv('OCID_KEY')
        feed_dir_path = integrations_path
        return opencellid.OpenCellIdFeed(feed_dir_path, api_key)

    def instantiate_mls_feed_object(self):
        feed_dir_path = integrations_path
        return opencellid.OpenCellIdFeed(feed_dir_path)

    def test_integration_instantiation(self):
        assert self.instantiate_opencellid_feed_object()

    def test_integration_opencellid_db_iterator(self):
        row_count = 0
        ocid_obj = self.instantiate_opencellid_feed_object()
        for row in ocid_obj:
            row_count += 1
        assert row_count == 999

    def test_update_opencellid(self):
        log = logging.getLogger('test_update_opencellid')
        if os.getenv("TRAVIS_EVENT_TYPE") == "cron":
            row_count = 0
            ocid_obj = self.instantiate_opencellid_feed_object()
            ocid_obj.debug = True
            ocid_obj.update_feed()
            for row in ocid_obj:
                row_count += 1
                if row_count % 1000000 == 0:
                    log.debug("Parsed %s from Unwired Labs feed..." % row_count)
            assert row_count > 100
        else:
            log.info("Not a cron job, not testing against Unwired Labs.")
            assert True

    def test_update_mls(self):
        log = logging.getLogger('test_update_mls')
        row_count = 0
        ocid_obj = self.instantiate_mls_feed_object()
        ocid_obj.debug = True
        ocid_obj.update_feed()
        for row in ocid_obj:
            row_count += 1
            if row_count % 1000000 == 0:
                log.debug("Parsed %s from MLS feed..." % row_count)
        assert row_count > 100
