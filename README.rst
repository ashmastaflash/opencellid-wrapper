----------------
OpenCellID Utils
----------------

.. image:: https://travis-ci.org/ashmastaflash/opencellid-wrapper.svg?branch=master
    :target: https://travis-ci.org/ashmastaflash/opencellid-wrapper

.. image:: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper/badges/gpa.svg
   :target: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper
   :alt: Code Climate

.. image:: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper/badges/coverage.svg
   :target: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper/coverage
   :alt: Test Coverage

.. image:: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper/badges/issue_count.svg
   :target: https://codeclimate.com/github/ashmastaflash/opencellid-wrapper
   :alt: Issue Count


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

The test fixture file cell_towers.csv.gz contains information from the
OpenCellID database, which is licensed CC-BY-SA 3.0
