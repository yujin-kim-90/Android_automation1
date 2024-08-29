#인증 > 간편번호(공동인증서 인증)
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
from 변수 import 변수
from 변수 import 변수_인증
from 변수 import secure_keypad
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
    )
    appium_server_url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)
    yield driver
    driver.quit()

#tc_id: log_20
def test_공동인증서수단선택(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(20)
    # driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    # time.sleep(10)
    driver.find_element(By.ID, 변수_인증.다른로그인방법id).click()
    time.sleep(3)
    driver.find_element(By.ID, 변수_인증.로그인방법_인증서id).click()
    time.sleep(3)

def test_공동인증서로그인(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(5)
    driver.find_element(By.ID, 변수_인증.공동인증서로그인id).click()
    time.sleep(5)
    common.공동인증서비번(driver)
    driver.find_element(By.ID, 변수_인증.공동인증서확인id).click()
    time.sleep(10)