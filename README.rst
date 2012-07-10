amiandopy
======

amiandopy makes it really easy to interact with Facebook's Graph API.

Usage
-----

::

    from amiandopy.amiando_api import AmiandoAPI

    graph = AmiandoAPI(amiando_api_key)

    # Get events
    graph.get('event/find')

Installation
------------

::

    $ pip install amiandopy

Contribute
----------

* Fork `the repository <https://github.com/ledil/amiandopy>`_.
* Do your thing (preferably on a feature branch).
* Write a test that demonstrates that the bug was fixed or the feature works as expected.
* Send a pull request and bug me until I merge it!
