import sys
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

country_codes = {"ca": r"https://datastudio.google.com/u/1/reporting/92fa2e32-43dc-4b8a-a272-c3039e0fc647/page/oNLSB",
    "us":r"https://datastudio.google.com/u/1/reporting/3e64b619-50c9-44cf-b452-23487bb76e8c/page/oNLSB"}

def main():
    if len(sys.argv) == 4:
        if sys.argv[1].lower() in country_codes:
            execute(sys.argv[1], sys.argv[2], sys.argv[3])
        else:
            print("Include a value country code from the following list: " + ", ".join(country_codes))
    else:
        print("Please include Country Code, Company ID and Integration Key")
def execute(country_code, company_id, integration_key):
    ffprofile = webdriver.FirefoxProfile(r"C:\Users\User\AppData\Roaming\Mozilla\Firefox\Profiles\4252a2dq.default-release")
    print("loaded 1")
    browser = webdriver.Firefox(firefox_profile=ffprofile)
    print("loaded 2")
    browser.get(country_codes[country_code])

    wait = WebDriverWait(browser, 100)
    there = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR,".alignHolder")))

    action = webdriver.ActionChains(browser)
    #header_area = wait.until(ec.visibility_of_element_located((By.XPATH, ".//header-zone")))
    for a in range(5):
        time.sleep(3)
        action.move_to_element_with_offset(there,a,a).click().perform()
        print("performed " + str(a))
    copy_button = wait.until(ec.visibility_of_element_located((By.XPATH, ".//button[contains(@aria-label, 'Make a copy of this report')]")))
    copy_button.click()
    copy_report_button = wait.until(ec.visibility_of_element_located((By.XPATH, ".//button[text()[contains(.,'Copy Report')]]")))
    copy_report_button.click()

    first_window = browser.current_window_handle

    while len(browser.window_handles) == 1:
        print("Try Again")
        time.sleep(3)
    for each in browser.window_handles:
        print("La ma " + each)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
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
