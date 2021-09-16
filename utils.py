#  python utils for connection builder sample
#  utilities general catchall file
#
import argparse
import configparser
import imagehash
import logging
import urllib.request
from datetime import date, datetime
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url_base = 'https://wordpress.com/me'
url_login_redirect = 'https://wordpress.com/log-in?redirect_to=%2Fme'


def config_load():
    config = configparser.ConfigParser()
    config['default'] = {}
    configfile = 'cnxbld.ini'

    try:
        config.read(configfile)
    except FileNotFoundError:
        config['default'] = {
            "sitename": "https://wordpress.com/me",
            "password": "replace_password",
            "test": "True",
            "username": "replace_username",
        }
    return config


def find(driver, what, by=None):
    element = None
    if by is None:
        xpath = what.find("") >= 0
        by = By.XPATH if xpath else by.ID
    try:
        element = driver.find_element(by=by, value=what)
    except NoSuchElementException:
        print('(cnxbld) EXCEPTION::')
        driver.quit()
    return element


def get_image(url):
    img = Image.open(urllib.request.urlopen(url))
    return img


def get_image_hash(image):
    avg_hash = imagehash.average_hash(image)
    return avg_hash


def get_runtime_password(args, config, logger):
    # TODO:  obscure display of exposed password
    if args.password:
        password = get_password(args)
        pwd_obscured = get_password_obscured(password)
        logger.info(':::     password ' + str(pwd_obscured) + ' from args')
    elif config['default']['password']:
        password = config['default']['password']
        pwd_obscured = get_password_obscured(password)
        logger.info(':::     password value ' + str(pwd_obscured) + ' from config')
    else:
        logger.info(':::     password value not found, default set')
        password = ''
    return password


def get_runtime_site(args, config, logger):
    if args.sitename:
        sitename = get_sitename(args)
        logger.info(':::     sitename ' + str(sitename) + ' from args')
    elif config['default']['sitename']:
        sitename = config['default']['sitename']
        logger.info(':::     sitename value ' + str(sitename) + ' from config')
    else:
        logger.info(':::     sitename value not found, default set')
        sitename = ''
    return sitename


def get_runtime_username(args, config, logger):
    if args.username:
        username = get_username(args)
        logger.info(':::     username ' + str(username) + ' from args')
    elif config['default']['username']:
        username = config['default']['username']
        logger.info(':::     username value ' + str(username) + ' from config')
    else:
        logger.info(':::     username value not found, default set')
        username = 'needs_a_username_value'
    return username


def get_password(args):
    if args.password:
        password = args.password
    else:
        username = 'needs_password'
    return password


def get_password_obscured(password):
    obscured_pwd = password[:2]+'--**--'+password[-2:]
    return obscured_pwd


def get_sitename(args):
    if args.sitename:
        sitename = args.sitename
    return sitename


def get_username(args):
    if args.username:
        username = args.username
    else:
        username = 'needs_username'
    return username


def get_test(args):
    test = False
    if args.test:
        test = True
    return test


def get_webdriver(urlbase):
    # service = Service('/usr/local/bin/chromedriver')
    # service.start()
    # Initial version hard coded for Chromedriver, ideally to be multi platform
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(service.service_url)
    driver.get(urlbase)
    return driver


def login_check(driver):
    #   check for login redirect
    current_url = driver.current_url
    if current_url == url_login_redirect:
        login_site(driver)
    return


def login_site(driver):
    #   NOT RECOMMENDED PRACTICE
    #   INSECURE WORKAROUND
    #   NORMALLY, DO NOT DO THIS

    #
    #   CREDS GET AND POPULATE
    #
    username_field = driver.find_element_by_id("usernameOrEmail")
    username_field.send_keys('cjsatyahoo')

    continue_button = driver.find_element_by_class("button form-button is-primary")
    continue_button.click()

    password_field = driver.find_element_by_id("password")
    password_field.send_keys('cjs@@yah00')

    driver.get(url_base)
    return


def parse_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser(description='Sample Tests for Wordpress')
    # Required arguments

    # Optional arguments
    parser.add_argument('--sitename', '-s',
                        help='Target test sitename / url',
                        action='store_true', default=False)
    parser.add_argument('--test', '-t',
                        help='Show prospective changes without making updates to page',
                        action='store_true', default=False)
    parser.add_argument('--username', '-u',
                        help='Username credentials to enter',
                        action='store_true', default=False)
    parser.add_argument('--password', '-p',
                        help='Password credentials to enter',
                        action='store_true', default=False)

    args = parser.parse_args()
    return args


def initialize_logger():
    """

    :return:
    """
    #   TODO: switch to logging config file
    #   fileConfig('logging_config.ini')
    #   logger = logging.getLogger()

    logger = logging.getLogger('cnxbld')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('cnxbld.log', encoding='utf8')
    console_handler = logging.StreamHandler()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
