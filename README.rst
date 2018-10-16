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

OpenCelliD Project is licensed under a Creative Commons Attribution-ShareAlike
4.0 International License.


Usage (with API key from Unwired Labs)
--------------------------------------

::

        import opencellid
        ocid_obj = opencellid.OpenCellIdFeed("/dir/for/feed/file/", "api_key")
        # Update OpenCellID feed from web:
        ocid_obj.update_feed()
        # Print all rows in OpenCellID feed:
        for row in ocid_obj:
            print row


Usage (no API key, update from Mozilla Location Services)
---------------------------------------------------------

::

        import opencellid
        ocid_obj = opencellid.OpenCellIdFeed("/dir/for/feed/file/")
        # Update OpenCellID feed from web:
        ocid_obj.update_feed()
        # Print all rows in OpenCellID feed:
        for row in ocid_obj:
            print row


Error Handling
--------------

The tool will attempt to detect if the download is a gzipped CSV file before
boving the download to replace the original gzipped CSV.  If an IOError is
encountered, a meaningful message will be displayed, and the exception will
be re-raised.  For example, if you're being rate-limited, you'll see...

::

        >>> ocid_obj.update_feed()
        Updating OpenCellID feed from Unwired Labs.
        Feed did not update... you're being rate-limited!
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "opencellid/opencellid_feed.py", line 60, in update_feed
            consumer.next()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 107, in next
            self.fieldnames
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 90, in fieldnames
            self._fieldnames = self.reader.next()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 464, in readline
            c = self.read(readsize)
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 268, in read
            self._read(readsize)
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 303, in _read
            self._read_gzip_header()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 197, in _read_gzip_header
            raise IOError, 'Not a gzipped file'
        IOError: Not a gzipped file


And if your API key is not accepted, you'll see...

::

        >>> ocid_obj.update_feed()
        Updating OpenCellID feed from Unwired Labs.
        API token rejected by Unwired Labs!!
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "opencellid/opencellid_feed.py", line 60, in update_feed
            consumer.next()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 107, in next
            self.fieldnames
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 90, in fieldnames
            self._fieldnames = self.reader.next()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 464, in readline
            c = self.read(readsize)
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 268, in read
            self._read(readsize)
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 303, in _read
            self._read_gzip_header()
          File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/gzip.py", line 197, in _read_gzip_header
            raise IOError, 'Not a gzipped file'
        IOError: Not a gzipped file


When this happens, the original feed is not updated, so you can catch and
re-initialize the ``ocid_obj`` to pull from MLS until you can sort out the
rate limiting or API key issue.


Installation
------------

pip install opencellid

Testing
-------

py.test

The test fixture file cell_towers.csv.gz contains information from the
OpenCellID database, which is licensed CC-BY-SA 4.0
