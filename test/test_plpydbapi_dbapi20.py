"""
DB-API test class for plpydbapi, to be used with
https://launchpad.net/dbapi-compliance
"""

import dbapi20
import plpydbapi


class test_Plpydbapi(dbapi20.DatabaseAPI20Test):
    driver = plpydbapi

    def setUp(self):
        dbapi20.DatabaseAPI20Test.setUp(self)

    def tearDown(self):
        dbapi20.DatabaseAPI20Test.tearDown(self)

    def test_nextset(self):
        pass

    def test_setoutputsize(self):
        pass
