from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time
import traceback
from urllib.parse import urlencode
import requests
import re
import schedule
import argparse


# 模拟打卡相关部分
user_name = "chuanjg19" # 校园网用户名
password = "19460614" # 校园网密码
JLU_CHECK_URL = "https://ehall.jlu.edu.cn/jlu_portal/index" # 健康打卡系统登录页
SAVE_PATH = os.path.abspath('.')



# 截图上传相关部分
st_number = "2019XXXXXX" # 学号
st_name = "川建国" # 姓名
XZC_URL = "http://www.xzc.cn/"
XZC_CODE = "11111111111"


def jlu_check(screenshot=False, file_path=SAVE_PATH, i = ):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(browser, 20)
        browser.get(JLU_CHECK_URL)

        ###  login in
        # get login page element
        user_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        pw_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_bt = wait.until(EC.element_to_be_clickable((By.ID, "login-submit")))
        # interact with login page
        user_input.send_keys(user_name)
        pw_input.send_keys(password)
        login_bt.click()


        ### more
        # more
        more_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".student-tabList > ul > li:nth-of-type(7) > a")))
        more_link.click()

        ### check
        # find everyday check
        check_link = wait.until(EC.element_to_be_lickable((By.CSS_SELECTOR, 'div.alk-servvice-nav > h2.alk-service-nav-title > a[title="研究生每日打卡"]')))
        check_link.click()

        # handle
        handle_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".guide_title_center > .bt_2")))
        handle_link.click()
        # fill in and configure
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle != browser.current_window_handle:
                browser.close()
                browser.switch_to_window(newhandle)
                break

        # submit
        submit_bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.form_command_bar > li.command_button > a.command_button_content")))
        submit_bt.click()

        # dialog process
        ok_bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dialog_footer > .dialog_button.default.fr")))
        ok_bt.click()
        success = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dialog_footer > button.dialog_button.default.fr")))

        print(time.strftime("%Y-%m-%d %H:%M:%S check success!", time.localtime()))

        ### screenshot
        if screenshot:
            body = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html")))
            time.sleep(2) # wait until the ok dialog display
            file_name = time.strftime("%Y%m%d-%H.png", time.localtime())
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            abs_file_path = os.path.join(os.path.abspath(file_path), file_name)
            body.screenshot(abs_file_path)
            return abs_file_path
        else:
            return None
        
    except TimeoutException:
        # print("Timeout! Please wait a minute and try again!")
        # return None
        time.sleep(60*30)
        if time.localtime().tm_hour in [7, 11, 17, 21]
            return jlu_check(file_path, screenshot)
        else:
            print("network problem! several tries all failed!")
    except NoSuchElementException:
        print("Source code has been changed. Please edit this code to fit it and try again!")
        return None
    except BaseException as e:
        traceback.print_exc(e)
        return None
    finally:
        browser.close()



def jlu_check_old(screenshot=False, file_path=SAVE_PATH):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(browser, 20)
        browser.get(JLU_CHECK_URL)

        ###  login in
        # get login page element
        user_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        pw_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_bt = wait.until(EC.element_to_be_clickable((By.ID, "login-submit")))
        # interact with login page
        user_input.send_keys(user_name)
        pw_input.send_keys(password)
        login_bt.click()


        ### check
        # check
        check_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".student-tabList > ul > li:nth-of-type(5) > a")))
        check_link.click()
        # handle
        handle_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".guide_title_center > .bt_2")))
        handle_link.click()
        # fill in and configure
        handles = browser.window_handles
        for newhandle in handles:
            if newhandle != browser.current_window_handle:
                browser.close()
                browser.switch_to_window(newhandle)
                break

        # browser.switch_to_window(browser.window_handles[1])
        agree_box = wait.until(EC.element_to_be_clickable((By.ID, "V1_CTRL82")))
        confirm_bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.command_button > a.command_button_content")))
        agree_box.click()
        confirm_bt.click()
        ok_bt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dialog_footer > .dialog_button.default.fr")))
        ok_bt.click()
        success = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dialog_footer > button.dialog_button.default.fr")))
        print(time.strftime("%Y%m%d check success!", time.localtime()))
        if screenshot:
            body = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html")))
            time.sleep(2) # wait until the ok dialog display
            file_name = time.strftime("%Y%m%d.png", time.localtime())
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            abs_file_path = os.path.join(os.path.abspath(file_path), file_name)
            body.screenshot(abs_file_path)
            return abs_file_path
        else:
            return None
        
    except TimeoutException:
        # print("Timeout! Please wait a minute and try again!")
        # return None
        time.sleep(60*10)
        return jlu_check(file_path, screenshot)
    except NoSuchElementException:
        print("Source code has been changed. Please edit this code to fit it and try again!")
        return None
    except BaseException as e:
        traceback.print_exc(e)
        return None
    finally:
        browser.close()

def upload_screenshot(file):

    session = requests.Session()
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
        "Referer" : XZC_URL + XZC_CODE,
    }

    # index page
    result1 = session.get(XZC_URL + XZC_CODE, headers=headers)
    
    # preview picture page
    result2 = session.get(
        XZC_URL + "index.php?mod=attach&op=preview",
        headers=headers
    )

    # upload picture page
    params = {
        'op' : 'ajax',
        'do' : 'fileupload'
    }
    result3 = session.post(
        XZC_URL + '?' + urlencode(params), 
        headers=headers, 
        files={"files[]" : open(file, 'rb')}
    )

    # preview uploaded picture page
    img = result3.json().get('files')[0].get('data').get('img')
    result4 = session.get(XZC_URL + img, headers=headers)

    # submit page
    params = {
        'op' : 'fileupload'
    }
    formhash = re.search('formhash\"\s+value=\"(\w+)\"\s+/>', result1.text).group(1)
    aids = result3.json().get('files')[0].get('data').get('aid')
    file_names = result3.json().get('files')[0].get('data').get('filename')
    data = {
        'formhash' : formhash,
        'postsubmit' : 'true',
        'sid' : XZC_CODE,
        'cname' : st_number,
        'uname' : st_name,
        'aids[]' : aids,
        'filenames[]' : file_names
    }
    result5 = session.post(XZC_URL + '?' + urlencode(params), data=data, headers=headers)
    



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--screenshot', action='store_true', default=False, 
                        help='get a screenshot and upload it')
    parser.add_argument('--everyday', action='store_true', default=False,
                        help='run task everyday')

    args = parser.parse_args()
    def task():
        abs_file_path = jlu_check(screenshot=args.screenshot)
        if abs_file_path:
            upload_screenshot(abs_file_path)

    if args.everyday:
        # hour = int(7 + int(st_number[-2:]) / 60)
        minute = int(st_number[-2:]) % 10

        schedule.every().day.at("{:0>2d}:{:0>2d}".format(7, minute)).do(task)
        schedule.every().day.at("{:0>2d}:{:0>2d}".format(11, minute)).do(task)
        schedule.every().day.at("{:0>2d}:{:0>2d}".format(17, minute)).do(task)
        schedule.every().day.at("{:0>2d}:{:0>2d}".format(21, minute)).do(task)
        # schedule.every().day.at("{:0>2d}:{:0>2d}".format(15, 27)).do(task)

        while True:
            schedule.run_pending()
            time.sleep(30)

    else:
        task()

