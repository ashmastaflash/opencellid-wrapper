----------------
OpenCellID Utils
----------------

This project is not associated with the OpenCellID project.  This is a utility
package for downloading and parsing the OpenCellID database.


Usage:
------

::

        import opencellid
        ocid_obj = opencellid.OpenCellIdFeed("/dir/for/feed/file/", "api_key")
        # Update OpenCellID feed from web:
        ocid_obj.update_from_web()
        # Print all rows in OpenCellID feed:
        for row in ocid_obj:
            print row


Installation:
-------------

pip install opencellid

Testing:
--------

py.test
