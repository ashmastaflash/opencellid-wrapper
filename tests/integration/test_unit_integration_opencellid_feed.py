import imp
import os
modulename = 'opencellid'
modulepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
file, pathname, description = imp.find_module(modulename, [modulepath])
opencellid = imp.load_module(modulename, file, pathname, description)

herepath = os.path.dirname(os.path.abspath(__file__))
integrations_path = os.path.join(herepath, "../fixtures")


class TestIntagrationOpenCellIdFeed:

    def instantiate_opencellid_feed_object(self):
        api_key = "I-am-an-api-key"
        feed_dir_path = integrations_path
        return opencellid.OpenCellIdFeed(feed_dir_path, api_key)

    def test_integration_instantiation(self):
        assert self.instantiate_opencellid_feed_object()

    def test_integration_opencellid_db_iterator(self):
        row_count = 0
        ocid_obj = self.instantiate_opencellid_feed_object()
        for row in ocid_obj:
            row_count += 1
            print row
        assert row_count == 999
