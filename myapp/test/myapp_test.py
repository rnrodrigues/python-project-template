from nose.tools import *


def setup():
    print("setup!")


def teardown():
    print("tear down!")


def test_basic():
    """should be test"""
    assert True
