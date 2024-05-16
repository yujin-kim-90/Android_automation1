from 변수 import 변수
from 변수 import 변수_회원가입
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


def test_case_01(driver)->None: #mem_01(탈퇴케이스)
    #로그인 완료 상태에서 실행/홈 위치 상태
    설정.waitElement(driver, 변수.앱이름운영).click()
    설정.waitElement(driver, 변수_회원가입.전체탭).click()
    time.sleep(4)
    설정.waitElement(driver, 변수_회원가입.검색).click()
    설정.waitElement(driver, 변수_회원가입.검색입력).click()
    설정.waitElement(driver, 변수_회원가입.검색입력).send_keys("탈퇴")






