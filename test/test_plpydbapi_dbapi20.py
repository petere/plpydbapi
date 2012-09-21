"""
DB-API test class for plpydbapi, to be used with
https://launchpad.net/dbapi-compliance
"""

import dbapi20
import plpy
import plpydbapi
import unittest


is_pg92_or_newer = 'cursor' in plpy.__dict__


class test_Plpydbapi(dbapi20.DatabaseAPI20Test):
    driver = plpydbapi

    def setUp(self):
        dbapi20.DatabaseAPI20Test.setUp(self)

    def tearDown(self):
        dbapi20.DatabaseAPI20Test.tearDown(self)

    @unittest.skipUnless(is_pg92_or_newer, ".description not fully supported in this version")
    def test_description(self):
        super(test_Plpydbapi, self).test_description()

    def test_nextset(self):
        pass

    def test_setoutputsize(self):
        pass
