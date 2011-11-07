"""
Support classes for hooking together unittest and PL/Python
"""

import plpy
import unittest


class PlpyInfoStream(object):
    """
    A file-like object that prints to plpy.info

    This is used as an output stream for
    unittest.runner.TextTestResult and only needs to support what's
    used there.  In particular, printErrorList() forgets to call
    .flush() at the end, so we need to do the funny business with
    automatically flushing to the last newline, which sort of emulates
    the normal stderr behavior.

    http://bugs.python.org/issue13236
    """

    def __init__(self):
        self.buf = ""

    def __del__(self):
        self.close()

    def close(self):
        self.flush()

    def flush(self):
        if len(self.buf) > 0:
            plpy.info(self.buf.rstrip("\n"))
        self.buf = ""

    def _flush_to_newline(self):
        pos = self.buf.rfind("\n")
        if pos == -1:
            return
        plpy.info(self.buf[:pos])
        self.buf = self.buf[(pos + 1):]

    def write(self, str):
        self.buf += str
        self._flush_to_newline()


class PlpyTestRunner(unittest.TextTestRunner):
    """
    A test runner like the standard test runner, but redirecting
    output to the database client.
    """

    def __init__(self, **kwargs):
        super(PlpyTestRunner, self).__init__(stream=PlpyInfoStream(), **kwargs)
