import 변수
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


#TC : 로그인 및 인증 = 카드로 인증
def test_case_01(driver)->None: #log24
    설정.waitElement(driver, 변수.앱이름).click()
    설정.waitElement(driver, 변수.로그인).click()
    time.sleep(4)
    설정.waitElement(driver, 변수.카드로인증).click()

def test_case_02(driver)->None: #log26
    #아래 비번입력 (간단히 배열로 정리 예정)
    설정.waitElement(driver, 변수.비번xpath5).click() #카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath3).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath4).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath2).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath9).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath2).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath9).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath7).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath0).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath0).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath0).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath3).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath6).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath0).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath0).click()  # 카드번호='5342929700036003'
    설정.waitElement(driver, 변수.비번xpath3).click()  # 카드번호='5342929700036003'

    #유효기간입력.
    # 설정.waitElement(driver, 변수.유효기간xpath).click()
    time.sleep(3) #0125카드유효기간
    common.xyTouch(driver, 400, 2173) #0입력
    common.xyTouch(driver, 140, 1658) #1입력
    common.xyTouch(driver, 412, 1658) #2입력
    common.xyTouch(driver, 404, 1827) #5입력

    time.sleep(2) #cvc=955
    설정.waitElement(driver, 변수.비번xpath9).click()
    설정.waitElement(driver, 변수.비번xpath5).click()
    설정.waitElement(driver, 변수.비번xpath5).click()

    time.sleep(2) #카드비번=1212
    설정.waitElement(driver, 변수.비번xpath1).click()
    설정.waitElement(driver, 변수.비번xpath2).click()

def test_case_03(driver) -> None:  # log27

    time.sleep(2) #간편번호설정=121212 / 재입력확인=121212
    # 간편번호설정 반복 횟수 설정
    num_iterations = 6
    for i in range(num_iterations):
        설정.waitElement(driver, 변수.비번xpath1).click()
        설정.waitElement(driver, 변수.비번xpath2).click()

    설정.waitElement(driver, 변수.지문닫기).click()







