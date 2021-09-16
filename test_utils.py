import argparse
import pytest
import utils


def test_get_test_true():
    args = argparse.Namespace(test=True)
    test = utils.get_test(args)
    assert test is True


def test_get_username():
    args = argparse.Namespace(username='fakeuser')
    username = utils.get_username(args)
    assert username == 'fakeuser'


def test_get_password():
    args = argparse.Namespace(password='fakepassword')
    password = utils.get_password(args)
    assert password == 'fakepassword'


def test_get_sitename():
    args = argparse.Namespace(sitename='some_sandbox_sitename')
    sitename = utils.get_sitename(args)
    assert sitename == 'some_sandbox_sitename'


def test_settings_file():
    config = utils.config_load()
    assert config['default'].name == 'default'
