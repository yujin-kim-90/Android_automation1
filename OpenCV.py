import pytest
import os

#import setting
#import config
import cv2
import time, datetime


from appium import webdriver
from appium.options.android import UiAutomator2Options

from selenium.webdriver.support.wait import WebDriverWait

import 간편번호설정


# appium 세팅
@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2'
    )

    appium_server_url = 'http://localhost:4723/wd/hub'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.press_keycode(3)

    yield driver
    driver.quit()
#opencv 이미지 만들기
class TS():
    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

def test():
    currentPath = '%s/' % os.getcwd()
    test_Directory = currentPath + '/'
    return test_Directory
class Matching():
    def detectimage(name):
        currentPath = '%s/' % os.getcwd()
        #test_Directory = currentPath + '/'

        if not os.path.exists(currentPath):
            os.makedirs(currentPath)

        wait = WebDriverWait(driver, 20)

        screenshotPath = currentPath + '%s-screenshot.png'
        detectImagePath = '/Users/yujin/PycharmProjects/Android_automation/assets/' + name

        driver.save_screenshot(screenshotPath)

        sourceimage = cv2.imread(screenshotPath, 0)
        template = cv2.imread(detectImagePath, 0)

        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('max_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))

        color = (0, 0, 255)
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenshotPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, sourceimage)

        return center

    #
    #
    # # 이미지 찾아 중앙을 tap 한다.
    #
    # driver.save_screenshot(screenshotPath)
    # Matching.detectimage(self, screenshotPath, detectImagePath)
#
# def test_case_01(self, ):
#     ts=TS()
#     setting.wait_Element(driver, config.execute_app).click()
#     time.sleep(1)
#     setting.wait_Element(driver, '//android.widget.Button[@content-desc="로그인 버튼"]').click()
#     time.sleep(3)
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.Button').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText').send_keys("안추도")
#     setting.wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.EditText').send_keys("920124")
#     setting.wait_Element(driver, '//android.widget.LinearLayout[@content-desc="주민등록번호의 뒷자리 하나를 입력하세요"]').click()
#
#     #----- 주민번호 뒷자리 누르기
#     matching = Matching()
#
#     # 스크린샷을 저장할 폴더를 생성합니다.
#     currentPath = '%s/' % os.getcwd()
#     test_Directory = currentPath + '/'
#
#     if not os.path.exists(test_Directory):
#         os.makedirs(test_Directory)
#
#     wait = WebDriverWait(driver, 20)
#
#
#     # 이미지 찾아 중앙을 tap 한다.
#     screenshotPath = test_Directory + '%s-screenshot.png'
#     detectImagePath = '/Users/yujin/PycharmProjects/android_auto/assets/1_keypad_login.png'
#     driver.save_screenshot(screenshotPath)
#
#     center = matching.detectimage(screenshotPath, detectImagePath)
#     driver.tap([center])
#     time.sleep(1)
#     setting.wait_Element(driver, '//android.widget.ImageButton[@content-desc="닫기"]').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button').click()
#     setting.wait_Element(driver,'//android.widget.EditText[@content-desc="인증 번호 입력"]').send_keys("345665")
#     time.sleep(2)
#
#     for i in (0,2):
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
#         setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="4"]').click()
#         time.sleep(1)
#
#     setting.wait_Element(driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.Button').click()
#
#     time.sleep(3)
#     #카드 비번
#     setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="1"]').click()
#     setting.wait_Element(driver, '//android.widget.ImageView[@content-desc="2"]').click()
#     time.sleep(5)
#
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[1]').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView').click()
#     setting.wait_Element(driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView[2]').click()
#
#
#
#
