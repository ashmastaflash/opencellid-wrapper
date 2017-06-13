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
            print row
        assert row_count == 999

    # def test_update_opencellid(self):
    #    row_count = 0
    #    ocid_obj = self.instantiate_opencellid_feed_object()
    #    ocid_obj.debug = True
    #    ocid_obj.update_feed()
    #    for row in ocid_obj:
    #        row_count += 1
    #        print row
    #    assert row_count > 100

    def test_update_mls(self):
        row_count = 0
        ocid_obj = self.instantiate_mls_feed_object()
        ocid_obj.debug = True
        ocid_obj.update_feed()
        for row in ocid_obj:
            row_count += 1
            if row_count % 10000 == 0:
                print("Parsed %s from MLS feed..." % row_count)
        assert row_count > 100
