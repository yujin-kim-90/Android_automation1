import 변수
import 변수_로그인
import OpenCV
import pytest
import time
import os

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

#여기서 현재경로 보여주고
currentPath = '%s/' % os.getcwd()
screenshotPath = currentPath + '%s-screenshot.png'


# tc_id: log_03
def test_case_01(driver)->None:
    driver.find_element(By.XPATH, 변수.앱이름).click()
    time.sleep(10)
    driver.find_element(By.ID, 변수.로그인id).click()
    time.sleep(3)
    driver.save_screenshot(screenshotPath)
    for i in range(5):
        for i in range(3):
            name = 'card_setting_1.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            name = 'card_setting_2.png'
            driver.tap([OpenCV.Matching.detectimage(name)])
            time.sleep(2)
        j=1
        if j <3:
            As
            assert driver.find_element(By.ID, 변수_로그인.간편번호불일치text_id).text == '간편번호가 일치하지 않습니다.('+j+'/5)'
        elif 3<=j<5:
            assert driver.find_element(By.ID, 변수_로그인.간편번호불일치text_id).text == '간편번호가 일치하지 않습니다.(' + j+ '/5) 5회 연속 잘못 입력 시 이용이 제한됩니다.'
        else:
            assert driver.find_element(By.ID,변수_로그인.간편번호불일치text_id).text == '간편번호를 연속 5회 잘못 입력으로 이용할 수 없습니다. 본인인증 후 간편번호를 재설정해 주세요.'
        driver.find_element(By.ID, 변수_로그인.간편번호불일치_확인_id).click()