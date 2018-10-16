Changelog
=========

v1.3
----

Changes
~~~~~~~

- Updated CodeClimate settings. [Ash Wilson]

  Closes #3

- Updated download URL for OpenCellID feed. [Ash Wilson]

  Updated tests to avoid Travis-CI silence timeout.

  Closes #2

v1.2 (2017-06-13)
-----------------

Changes
~~~~~~~

- Improved error handling for bad API token and rate limiting
  situations. [Ash Wilson]

v1.0 (2017-06-13)
-----------------

Changes
~~~~~~~

- Support update from UnwiredLabs or Mozilla Location Services.  API
  changed, now use update_feed() method and source will be chosen
  depending on the presence of an API key. [Ash Wilson]

v0.1.1 (2017-01-23)
-------------------

New
~~~

- Unit and integration tests. [Ash Wilson]

- Creates an OpenCellIdFeed object which can be updated from web and
  iterated over. [Ash Wilson]


