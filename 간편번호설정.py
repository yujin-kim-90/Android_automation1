import 변수
import 설정
import OpenCV
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
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.시작하기_로그인Id).click()
    time.sleep(3)
    driver.find_element(By.XPATH, 변수.로그인xpath).click()
    time.sleep(3)
    driver.find_element(By.ID, 변수.로그인_이름Id).send_keys(변수.고객명)
    driver.find_element(By.ID, 변수.로그인_주민번호Id).send_keys(변수.생년월일)
    driver.find_element(By.ID, 변수.로그인_주민뒷자리Id).click()
    time.sleep(3)
    name= '1_keypad_login.png'
    driver.tap([OpenCV.Matching.detectimage(name)])
    driver.find_element(By.XPATH, 변수.로그인_통신사).click()
    driver.find_element(By.ID, 변수.로그인_간편번호_인증요청).click()









