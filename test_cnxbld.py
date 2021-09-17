#   tests for main
#
#
import time
from datetime import date, datetime
from selenium import webdriver
import configparser
import logging
import pytest
import unittest

# local imports
import utils

urlbase = 'https://wordpress.com/me'


class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(context):
        # can't assume Firefox
        # context.driver = webdriver.Firefox()
        context.driver = webdriver.Chrome()
        context.driver.implicitly_wait(5)
        context.driver.maximize_window()

        # navigate to our test url
        context.driver.get(urlbase)
        # context.driver.title

        config = utils.config_load()
        sitename = config['default']['sitename']
        username = config['default']['username']
        password = config['default']['password']

        utils.login_site(context.driver, username, password)
        # utils.login_check(context.driver)
        # username_field = context.driver.find_element_by_id("usernameOrEmail")
        # username_field.send_keys('cjsatyahoo')
        #
        # continue_button = context.driver.find_element_by_class_name("button.form-button.is-primary")
        # continue_button.click()
        #
        # password_field = context.driver.find_element_by_id("password")
        # password_field.send_keys('CJS@@yah00')
        # continue_button.click()

    def test_navigation_sanity(self):
        #   verify webdriver instantiation and navigation to expected target
        #   TODO: fail other tests if this fails
        # driver = utils.get_webdriver(urlbase)
        current_url = self.driver.current_url
        print('(cnxtst) WAITING::')
        time.sleep(5)
        self.driver.quit()
        assert current_url == urlbase

    def test_field_fname_is_not_empty(self):
        #   verify some text present in first name, default post creation is empty
        fname = self.driver.find_element_by_id('first_name')
        fname_content = fname.text
        assert fname_content != ""

    def test_field_lname_is_not_empty(self):
        #   verify some text present in last name, default post creation is empty
        #   TODO:  CALL THIS OUT AS AN EXPECTED FAILURE IF WE LEAVE LAST NAME BLANK
        lname = self.driver.find_element_by_id('last_name')
        lname_content = lname.text
        assert lname_content != ""

    def test_field_aboutme_is_not_empty(self):
        #   verify some text present in about me / description, default post creation is empty
        aboutme = self.driver.find_element_by_id('description')
        aboutme_content = aboutme.text
        assert aboutme_content != ""

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

        gravatar_current = self.driver.find_element_by_class_name('gravatar')
        gravatar_current_url = gravatar_current.get_attribute("src")

        img_default = utils.get_image(gravatar_default_url)
        img_current = utils.get_image(gravatar_current_url)
        hash_default = utils.get_image_hash(img_default)
        hash_current = utils.get_image_hash(img_current)
        hash_diff = hash_default - hash_current
        assert hash_diff == 0

    @classmethod
    def tearDownClass(context):
        # close our browser window
        context.driver.quit()


if __name__ == "__main__":
    unittest.main()
