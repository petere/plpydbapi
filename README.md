plpydbapi
=========

This module provides a (sort of) Python DB-API 2.0 compatible
interface on top of PL/Python.

About DB-API: <http://www.python.org/dev/peps/pep-0249/>

About PL/Python: <http://www.postgresql.org/docs/current/static/plpython.html>

Installation
------------

plpydbapi supports Python 2.6 and later, including Python 3.x, and
requires PostgreSQL 9.1 or later.  Using `cursor.description` requires
PostgreSQL 9.2.

Just install it like any setuptools-enabled Python module, for example

    python setup.py install

or use easy_install.  Make sure you use the Python version that your
installation of PL/Python was built against.

Using
-----

Here is an example how to use it:

    import plpydbapi

    dbconn = plpydbapi.connect()
    cursor = dbconn.cursor()
    cursor.execute("SELECT ... FROM ...")
    for row in cursor.fetchall():
        plpy.notice("got row %s" % row)
    dbconn.close()

Test suite
----------

[![Build Status](https://secure.travis-ci.org/petere/plpydbapi.png)](http://travis-ci.org/petere/plpydbapi)

There is a test suite in the test/ subdirectory.  It uses the DB-API
compliance test framework from
<https://launchpad.net/dbapi-compliance>.  So first fetch, er, clone,
er, branch yourself a copy of that

    bzr branch lp:dbapi-compliance

into the current directory.  If you have
[mr](http://kitenet.net/~joey/code/mr/), just run `mr up`.

If you are using Python 2.6, you also need the unittest2 package; with
Python 2.7 and later, the unittest module in the standard library is
enough.

Then run

    python setup.py test

This will run the unittest suite inside the PostgreSQL server,
forwarding the output for the client to see.

If you have a complicated setup, such as multiple PostgreSQL versions
or nonstandard ports, use libpq environment variables such as PGHOST
and PGPORT to point the test suite driver to an instance it can use.
You can also look into the files setup.py and
test/run_test_plpydbapi_dbapi20.sql for some additional ways to tweak
the process.
