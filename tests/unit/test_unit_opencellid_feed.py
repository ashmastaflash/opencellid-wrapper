import imp
import os
modulename = 'opencellid'
modulepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
file, pathname, description = imp.find_module(modulename, [modulepath])
opencellid = imp.load_module(modulename, file, pathname, description)

class TestOpenCellIdFeed:

    def test_build_ocid_url(self):
        api_key = "I-am-an-api-key"
        result = opencellid.OpenCellIdFeed.build_ocid_url(api_key)
        control = "http://opencellid.org/downloads/?apiKey=I-am-an-api-key&filename=cell_towers.csv.gz"
        assert result == control
