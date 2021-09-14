#  webdriver sample
#  messing around with options
#  e.g.
#
#

import sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def main():
    # main / initial sanity
    #
    print('(cnxbld) main:')
    print()

    # TODO: url as parameter / setting
    urlbase = 'https://wordpress.com/me'

    # TODO: test results output artifact
    #
    # service = Service('/usr/local/bin/chromedriver')
    # service.start()

    # Initial version hard coded for Chromedriver, ideally to be multi platform
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Remote(service.service_url)

    driver.get(urlbase)
    time.sleep(5)

    driver.quit()

    print()
    print('(cnxbld) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
