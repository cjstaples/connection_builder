#   tests for main
#
#


import configparser
import logging
import pytest
from datetime import date, datetime


def test_get_true():
    # TODO:  remove placeholder
    test = True
    assert test is True


def test_navigation_sanity():
    #   verify webdriver instantiation and navigation to expected target
    #   TODO: fail other tests if this fails
    assert False


def test_field_fname_is_not_empty():
    #   verify some text present in first name, default post creation is empty
    assert False


def test_field_lname_is_not_empty():
    #   verify some text present in last name, default post creation is empty
    assert False


def test_field_aboutme_is_not_empty():
    #   verify some text present in last aboutme, default post creation is empty
    assert False


def test_hide_profile_is_disabled():
    #   verify this setting is at the default post creation value, disabled
    assert False


def test_hide_profile_can_toggle():
    #   verify this setting can be toggled, i.e. control is live.
    #   post test leave disabled for simplicity
    assert False


def test_profile_link_single():
    #   verify there is exactly one profile link
    #   fail if none found, or more than one found
    assert False


def test_gravatar_image_is_default():
    #   read or pull down image
    #   compare to reference image or link, preferably by image content
    assert False

