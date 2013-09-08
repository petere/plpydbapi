"""
DB-API test class for plpydbapi, to be used with
https://launchpad.net/dbapi-compliance
"""

import dbapi20
import decimal
import plpy
import plpydbapi
import sys
import unittest


if sys.version[0] == '3':
    long = int

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

    def test_type_bool(self):
        con = self._connect()
        cur = con.cursor()
        try:
            cur.execute("select %s is true", [True])
        except self.driver.Error:
            self.fail("Driver does not support bool type")
        finally:
            con.close()

    def test_type_decimal(self):
        con = self._connect()
        cur = con.cursor()
        try:
            cur.execute("select round(%s)", [decimal.Decimal('55.678')])
        except self.driver.Error:
            self.fail("Driver does not support Decimal type")
        finally:
            con.close()

    def test_type_float(self):
        con = self._connect()
        cur = con.cursor()
        try:
            cur.execute("select round(%s)", [1.01])
        except self.driver.Error:
            self.fail("Driver does not support float type")
        finally:
            con.close()

    @unittest.skipUnless(sys.version[0] == '2', "long not supported after Python 2")
    def test_type_long(self):
        con = self._connect()
        cur = con.cursor()
        try:
            cur.execute("select round(%s)", [long(1)])
        except self.driver.Error:
            self.fail("Driver does not support long type")
        finally:
            con.close()
