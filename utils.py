import configparser
import logging
from datetime import date, datetime


def config_load():
    config = configparser.ConfigParser()
    config['default'] = {}
    configfile = 'cnxbld.ini'

    try:
        config.read(configfile)
    except FileNotFoundError:
        config['default'] = {
            "sitename": "https://wordpress.com/me",
            "test": "True",
        }
    return config


def get_sitename(args):
    if args.sitename:
        sitename = args.sitename
    return sitename


def get_test(args):
    test = False
    if args.test:
        test = True
    return test

