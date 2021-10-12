import time
import os
import selenium
from selenium import webdriver


def Login():
    # os.mkdir("../report")
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome()
    driver.get('http://report.seedsufe.com/report');
    driver.maximize_window()

    time.sleep(3)  # Let the user actually see something!

    name = ""
    password = ""
    ##待补充

    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div/div[1]").click()
    time.sleep(2)
    # driver.find_element_by_class_name("el-radio-button__inner").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/label[2]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/input").send_keys(name)

    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div[2]/div/input").send_keys(password)
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/button").click()
    time.sleep(3)

    # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/ul/li[6]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div/ul/li[8]").click()
    # time.sleep(3)
    # #  补充
    # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div/ul/li[7]").click()
    time.sleep(3)
    # driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div/ul/li[7]").click()
    # time.sleep(3)
    return driver