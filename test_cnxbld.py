#  python utils for connection builder sample
#  utilities general catchall file
#

import configparser
import logging
from datetime import date, datetime


def get_sitename(args):
    if args.sitename:
        sitename = args.sitename
    return sitename


def config_load():
    config = configparser.ConfigParser()
    config['default'] = {}
    configfile = 'cnxbld.ini'

    try:
        config.read(configfile)
    except FileNotFoundError:
        config['default'] = {
            "api": "",
            "limit": "99",
            "test": "True",
        }
    return config