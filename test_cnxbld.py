#   tests for main
#
#


import configparser
import logging
import pytest
import unittest
from datetime import date, datetime

import utils

urlbase = 'https://wordpress.com/me'


class TestSample(unittest.TestCase):

    def test_navigation_sanity(self):
        #   verify webdriver instantiation and navigation to expected target
        #   TODO: fail other tests if this fails
        driver = utils.get_webdriver(urlbase)
        print('(cnxtst) WAITING::')
        current_url = driver.current_url
        driver.implicitly_wait(5)
        driver.quit()
        assert current_url == urlbase

    def test_field_fname_is_not_empty(self):
        #   verify some text present in first name, default post creation is empty
        driver = utils.get_webdriver(urlbase)
        driver.implicitly_wait(5)
        print('(cnxtst) WAITING::')

        fname = driver.find_element_by_id('first_name')
        fname_content = fname.text
        driver.quit()
        assert fname_content is not None

    def test_field_lname_is_not_empty(self):
        #   verify some text present in last name, default post creation is empty
        driver = utils.get_webdriver(urlbase)
        driver.implicitly_wait(5)
        print('(cnxtst) WAITING::')

        lname = driver.find_element_by_id('last_name')
        lname_content = lname.text
        driver.quit()
        assert lname_content is not None

    def test_field_aboutme_is_not_empty(self):
        #   verify some text present in about me / description, default post creation is empty
        driver = utils.get_webdriver(urlbase)
        driver.implicitly_wait(5)
        print('(cnxtst) WAITING::')

        aboutme = driver.find_element_by_id('description')
        aboutme_content = aboutme.text
        driver.quit()
        assert aboutme_content is not None

    def test_hide_profile_is_disabled(self):
        #   verify this setting is at the default post creation value, disabled
        assert False

    def test_hide_profile_can_toggle(self):
        #   verify this setting can be toggled, i.e. control is live.
        #   post test leave disabled for simplicity
        assert False

    def test_profile_link_single(self):
        #   verify there is exactly one profile link
        #   fail if none found, or more than one found
        assert False

    def test_gravatar_image_is_default(self):
        compare_tolerance = 1
        gravatar_default_url = 'https://1.gravatar.com/avatar/435fe27bc5ddac453ada2f42329ee237?s=400&d=mm'

        #   TODO:  read or pull down current image
        gravatar_current_url = 'https://1.gravatar.com/avatar/435fe27bc5ddac453ada2f42329ee237?s=400&d=mm'

        img_default = utils.get_image(gravatar_default_url)
        img_current = utils.get_image(gravatar_current_url)
        hash_default = utils.get_image_hash(img_default)
        hash_current = utils.get_image_hash(img_current)
        hash_diff = hash_default - hash_current
        assert hash_diff == 0


if __name__ == "__main__":
    unittest.main()
