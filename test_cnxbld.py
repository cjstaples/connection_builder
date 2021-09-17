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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# local imports
import utils

urlbase = 'https://wordpress.com/me'


class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(context):
        # can't assume Firefox
        # context.driver = webdriver.Firefox()
        context.driver = webdriver.Chrome()
        context.driver.implicitly_wait(15)
        context.driver.maximize_window()
        wait = WebDriverWait(context.driver, 15)

        # navigate to our test url
        context.driver.get(urlbase)
        # context.driver.title

        config = utils.config_load()
        sitename = config['default']['sitename']
        username = config['default']['username']
        password = config['default']['password']

        utils.login_site(context.driver, username, password)

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
        # TODO: Something more robust than explicit waits
        # fname = WebDriverWait(self.driver, 15).until(ec.text_to_be_present_in_element_value(By.ID, 'first_name'))
        fname = self.driver.find_element_by_id('first_name')
        time.sleep(5)
        fname_content = fname.get_attribute('value')
        assert fname_content != ""

    #   NOTE - Last Name value currently not populated
    @unittest.expectedFailure
    def test_field_lname_is_not_empty(self):
        #   verify some text present in last name, default post creation is empty
        lname = self.driver.find_element_by_id('last_name')
        time.sleep(5)
        lname_content = lname.get_attribute('value')
        assert lname_content != ""

    def test_field_aboutme_is_not_empty(self):
        #   verify some text present in about me / description, default post creation is empty
        aboutme = self.driver.find_element_by_id('description')
        time.sleep(5)
        aboutme_content = aboutme.get_attribute('value')
        assert aboutme_content != ""

    def test_hide_profile_is_disabled(self):
        #   verify this setting is at the default post creation value, disabled
        hide_profile_toggle = self.driver.find_element_by_id('inspector-toggle-control-0')
        time.sleep(5)
        hide_profile_toggle_setting = hide_profile_toggle.is_selected()
        assert hide_profile_toggle_setting is False

    def test_hide_profile_can_toggle(self):
        #   verify this setting can be toggled, i.e. control is live.
        #   post test leave disabled for simplicity
        hide_profile_toggle = self.driver.find_element_by_id('inspector-toggle-control-0')
        time.sleep(5)
        hide_profile_toggle.click()

        hide_profile_toggle_checked = self.driver.find_element_by_class_name('components-form-toggle.is-checked')
        hide_profile_toggle_checked.click()

        toggle_state = hide_profile_toggle.get_attribute('value')
        assert toggle_state == "foo"

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
