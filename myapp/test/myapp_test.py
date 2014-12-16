from nose.tools import *
from myapp.farenheit import *
from myapp.users import *


def setup():
    print("setup!")


def teardown():
    print("tear down!")


def test_basic():
    """should be test"""
    assert True
