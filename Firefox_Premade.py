import sys
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

profile_address = r"C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\4252a2dq.default-release"

def main():
    if len(sys.argv) == 4:
        execute(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Please include url, Company ID and Integration Key")
def execute(url, company_id, integration_key):
    ffprofile = webdriver.FirefoxProfile(profile_address)
    print("loaded 1")
    browser = webdriver.Firefox(firefox_profile=ffprofile)
    print("loaded 2")
    browser.get(url)

    wait = WebDriverWait(browser, 100)

    men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()[contains(.,'Resource')]]")))

    resource = browser.find_element_by_xpath("//span[text()[contains(.,'Resource')]]/parent::node()")
    resource.click()
    en_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()[contains(.,'Resource')]]")))
    manage = browser.find_element_by_xpath("//span[text()[contains(.,'Manage added data sources')]]/parent::node()")
    manage.click()

    every = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,".row.datasource-item.layout-row")))

    for a in range(6):
        edit_button = wait.until(ec.visibility_of_all_elements_located((By.XPATH, ".//div[contains(@class, 'edit-btn')]")))
        edit_button[a].click()
        input = wait.until(ec.visibility_of_all_elements_located((By.XPATH, ".//input[contains(@class, 'ng-pristine ng-untouched ng-valid md-input ng-not-empty')]")))
        input[0].clear()
        input[0].send_keys(company_id + Keys.ENTER)
        input[1].clear()
        input[1].send_keys(integration_key + Keys.ENTER)
        reconnector = browser.find_element_by_xpath("//span[text()[contains(.,'Reconnect')]]/parent::node()//parent::node()").click()
        applier = wait.until(ec.visibility_of_element_located((By.XPATH, ".//span[text()[contains(.,'Apply')]]/parent::node()")))
        applier.click()
        donner = wait.until(ec.visibility_of_element_located((By.XPATH, ".//span[text()[contains(.,'Done')]]/parent::node()")))
        donner.click()

    print("finished")

if __name__ == "__main__":
    main()
