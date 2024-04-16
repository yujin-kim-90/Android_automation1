from 변수 import 변수
from 변수 import 변수_홈금융
import 설정
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



def test_case_01(driver)->None: #home_25
    설정.waitElement(driver, 변수.앱이름).click()
    time.sleep(3)
    설정.waitElement(driver, 변수_홈금융.금융).click()
    text1 = driver.find_element(By.XPATH, 변수_홈금융.금융).text
    assert text1 == "금융"

# def test_case_02(driver)->None: #home_27
#     설정.waitElement(driver, 변수_홈.금융배너).click()
#     text1 = driver.find_element(By.XPATH, 변수_홈.금융배너).text
#     assert text1 == "당신을 응원하는 금융, Your Big Fan 로카머니"


def test_case_03(driver)->None: #home_28
    설정.waitElement(driver, 변수_홈금융.대환대출).click()
    text1 = driver.find_element(By.XPATH, 변수_홈금융.대환대출).text
    assert text1 == "LOCA MONEY-대환대출"
    driver.press_keycode(4)
    time.sleep(2)

def test_case_04(driver) -> None:  # home_29
    설정.waitElement(driver, 변수_홈금융.장기카드대출).click()
    text1 = driver.find_element(By.XPATH, 변수_홈금융.장기카드대출).text
    assert text1 == "장기카드대출"

    driver.press_keycode(4)

    time.sleep(2)

    driver.swipe(300, 500, 300, 100, duration=800)  # 아래로 스크롤

def test_case_05(driver) -> None:  # home_29
    설정.waitElement(driver, 변수_홈금융.단기카드대출).click()
    text1 = driver.find_element(By.XPATH, 변수_홈금융.단기카드대출).text
    assert text1 == "단기카드대출"




