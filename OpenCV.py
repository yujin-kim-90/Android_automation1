import pytest
import os

#import setting
#import config
import cv2
import time, datetime
import numpy as np


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
def test_screenshot(test_directory):
    screenshotPath = test_directory + 'screenshot.png'
    return screenshotPath

class Matching():
    def detectimage(driver,name):
        if not os.path.exists(test()):
            os.makedirs(test())

        wait = WebDriverWait(driver, 20)

        detectImagePath = '/Users/channy/PycharmProjects/QA/Android_automation1/assets/' + name

        driver.save_screenshot(test_screenshot(test()))

        sourceimage = cv2.imread(test_screenshot(test()))
        template = cv2.imread(detectImagePath)

        # original_gray=cv2.cvtColor(sourceimage,cv2.COLOR_BGR2GRAY)
        # template_gray=cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        #
        # w, h = template_gray.shape[::-1]
        # result=cv2.matchTemplate(original_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        #
        # # 매칭 결과에서 가장 높은 값을 찾음
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #
        # # 템플릿의 너비와 높이
        # template_width, template_height = template_gray.shape[::-1]
        #
        # # 매칭 결과를 표시할 사각형의 좌상단, 우하단 좌표 계산
        # top_left = max_loc
        # bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        #
        # center = (top_left[0] + int(w / 2), top_left[1] + int(h / 2))
        #
        # # 원본 이미지에 매칭된 영역을 사각형으로 표시
        # cv2.rectangle(sourceimage, top_left, bottom_right, (0, 255, 0), 2)

        w, h, _ = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF_NORMED')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('max_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))

        color = (0, 0, 255)
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectshotPath = test_screenshot(test())[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, sourceimage)

        return center