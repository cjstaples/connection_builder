#  connection builder sample main
#
#

import sys
import time
import utils
from utils import get_webdriver


def main():
    # main / initial sanity
    #
    print('(cnxbld) main:')
    print()

    logger = utils.initialize_logger()
    logger.info('::: ')
    logger.info('::: starting test session :::')
    logger.info('::: initialize test session defaults :::')

    #   TODO: config -- write cnxbld.ini if it doesn't exist
    config = utils.config_load()

    logger.info('::: parse test session arguments :::')
    args = utils.parse_args()
    logger.info('::: ')

    sitename = utils.get_runtime_site(args, config, logger)
    username = utils.get_runtime_username(args, config, logger)
    password = utils.get_runtime_password(args, config, logger)
    logger.info('::: ')

    # TODO: test results output artifact
    # TODO: tie *validated* sitename to urlbase

    logger.info(':::    sitename: ' + sitename)
    logger.info('::: ')
    urlbase = 'https://wordpress.com/me'

    driver = get_webdriver(urlbase)
    driver.implicitly_wait(5)

    # TODO:  handle when already logged in
    # utils.login_check(driver)
    utils.login_site(driver, username, password)

    print('(cnxbld) SLEEPING::')
    time.sleep(5)
    driver.quit()

    print()
    print('(cnxbld) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
