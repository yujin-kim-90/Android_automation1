from 변수 import 변수
from 변수 import 변수_인증
from 변수 import 변수_결제
import common
import pytest
import time
import os

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

#tc_id: Pay_01
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.개발계앱).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수_결제.로그인페이지_로카페이id).click()
    driver.find_element(By.ID, 변수_결제.로카페이시작하기id).click()
    common.휴대폰인증(driver)
