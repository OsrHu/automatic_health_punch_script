# -*- coding: utf-8 -*-
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

myusername = ""  #登录账号
mypassword = ""  #登录密码
localtion = "浙江省 杭州市 西湖区"  #所在地区
localtions = localtion.split(' ')

#driver.maximize_window() #将窗口最大化

while 1:
    driver = webdriver.Chrome()  #模拟浏览器打开网站
    driver.get(
        "http://ca.zucc.edu.cn/cas/login?service=http%3A%2F%2Fyqdj.zucc.edu.cn%2Ffeiyan_api%2Fh5%2Fhtml%2Fdaka%2Fdaka.html"
    )
    try:
        #找到登录框，输入账号密码
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(
            myusername)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            mypassword)
        time.sleep(2)
        #模拟点击登录
        driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[5]/div/input[1]').click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        #输入地区
        # pag=driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input')
        # driver.execute_script("arguments[0].removeAttribute('readonly')",pag)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[3]/div[2]/div/div/input').click()
        for i in range(0, len(localtions)):
            driver.find_element_by_xpath(
                '//*[@class="picker-items-col-wrapper"]/div[text()="{}"]'.
                format(localtions[i])).click()
            time.sleep(1)
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[4]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[5]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[6]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[7]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[9]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[11]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[12]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[13]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[14]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[15]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[16]/div[2]/div/div/li[1]/label/div[2]/div'
        ).click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[2]/label/div[2]/div'
        ).click()
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="question-form"]/ul/li[17]/div[2]/div/div/li[10]/label/div[2]/div').click()
        # time.sleep(2)
        #模拟点击签到
        driver.find_element_by_partial_link_text('提交').click()
        time.sleep(2)
        print("签到成功")
        driver.quit()
        break
        # driver.quit()
    except Exception as e:
        driver.quit()
        print("签到失败")
        traceback.print_exc()
