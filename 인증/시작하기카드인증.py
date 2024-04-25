from 변수 import 변수
import 설정
import common
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


#TC : 시작하기>카드인증
#log_73
def test_case_01(driver)->None:
    설정.waitElement(driver, 변수.앱이름).click()
    설정.waitElement(driver, 변수.로그인).click()
    time.sleep(4)
    설정.waitElement(driver, 변수.카드로인증).click()

def test_case_02(driver)->None:
    common.카드인증(driver)


def test_case_03(driver) -> None:  

    time.sleep(2) #간편번호설정=121212 / 재입력확인=121212
    # 간편번호설정 반복 횟수 설정
    num_iterations = 6
    for i in range(num_iterations):
        설정.waitElement(driver, 변수.비번xpath1).click()
        설정.waitElement(driver, 변수.비번xpath2).click()

    설정.waitElement(driver, 변수.지문닫기).click()







