"""
Setup script for plpydbapi
"""

from setuptools import setup
from setuptools.command.test import test as _test


class test(_test):
    """Override test command to run psql with SQL test script"""

    def run(self):
        import subprocess
        import sys
        sys.exit(subprocess.call(['psql',
                                  '-X',
                                  '-d', 'postgres',
                                  '-v', 'langname=plpython{0}u'.format(sys.version[0])],
                                 stdin=open('test/run_test_plpydbapi_dbapi20.sql')))


setup(
    name='plpydbapi',
    version='0.20121018',
    py_modules=['plpydbapi'],
    packages=['test'],
    cmdclass={'test': test},

    description='DB-API compatible interface on top of PL/Python',
    author='Peter Eisentraut',
    author_email='peter@eisentraut.org',
    url='https://github.com/petere/plpydbapi',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

    setup_requires=["setuptools_git"],
    )
