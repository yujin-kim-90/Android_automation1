#인증 > 간편번호(휴대폰 인증)
#import OpenCV
import pytest
import time
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import common
import requests
from 변수 import 변수
from 변수 import 변수_인증

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
def test_금융메인(driver)->None:
    driver.find_element(By.XPATH, 변수.운영앱).click()
    time.sleep(20)
    common.xyTouch(driver,265,339)





