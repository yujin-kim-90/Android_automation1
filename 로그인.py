import 변수
import 설정
import random
import pytest
import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait

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

#로그인 > 로그인(간편번호)
def test_case_01(driver)->None:
    설정.waitElement(driver, 변수.앱이름).click()
    설정.waitElement(driver, 변수.로그인xpath).click()
    for i in range(0,5):
        for i in range(0,6):
            설정.waitElement(driver, '//android.widget.ImageView[@content-desc="1"]').click()
        driver.find_element(By.ID, 변수.간편번호불일치Id).click()
        #설정.waitElement(driver, 변수.간편번호불일치xpath).click()




