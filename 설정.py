import pytest
import time
# import config

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait


# 기다렸다가 클릭하는 함수 wait_Element / wait_Elements
def waitElement(driver, xpath):
    location = xpath
    try:
        element:WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print("Error: Timeout")
        return False
# def waitElements(driver, xpath):
#     location = xpath
#     waitElement(driver, location)
#     return driver.find_elements(By.XPATH, location)

# appium 세팅
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

#  설정 메뉴 이동 확인(PJ50-536)
def test_case_01(driver)->None:
    waitElement(driver, config.execute_app).click()
    time.sleep(10)
    waitElement(driver, config.menu_button).click()
    waitElement(driver, config.setting_button).click()
# 앱 최신정보 확인(PJ50-594)
def test_case_02(driver)->None:
    time.sleep(3)
    driver.swipe(300, 1000, 300, 100, duration=800)
    version=driver.find_element(By.XPATH, config.version_text).text
    assert version == config.current_ver, "true"
# 내 정보 관리 변경
def test_case_03(driver)->None:
    waitElement(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageButton').click()
    waitElement(driver, '//android.view.View[@content-desc="내정보관리"]').click()
    time.sleep(3)
    waitElement(driver, '//android.view.View[@content-desc="서류발급신청"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="4"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="4"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="1"]').click()
    waitElement(driver, '//android.widget.ImageView[@content-desc="4"]').click()

