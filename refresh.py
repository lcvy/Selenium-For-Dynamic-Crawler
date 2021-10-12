import time
import click
import check
import get
# from selenium import webdriver

def refreshFile(driver,k,PageFolderNow,PageFolderMax,PageFileNow,PageFileMax,FolderNow,FileNow):
    b = 0
    while b == 0:
        try:
            driver.refresh()
            time.sleep(1)

            sentry_2 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[" + str(k) + "]")
            driver.execute_script("arguments[0].scrollIntoView();", sentry_2)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            sentry_2.find_element_by_xpath("./label/span[2]").click()

            time.sleep(1)
            check.Check_clickPageforFolder(driver,PageFolderNow,PageFolderMax,k,FolderNow)
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[" + str(
                    FolderNow) + "]/div[1]").click()
            time.sleep(1)
            check.Check_clickPageforFile(driver,PageFileNow,PageFileMax,k,PageFolderNow,PageFolderMax,FolderNow,FileNow)
            time.sleep(1)
            b = 1
            return 0
        except:
            return 1


def refreshFolder(driver,k,PageFolderNow,PageFolderMax,FolderNow):
    b = 0
    while b == 0:
        try:
            driver.refresh()
            time.sleep(1)

            sentry_2 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[" + str(k) + "]")
            driver.execute_script("arguments[0].scrollIntoView();", sentry_2)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            sentry_2.find_element_by_xpath("./label/span[2]").click()

            time.sleep(1)

            check.Check_clickPageforFolder(driver, PageFolderNow, PageFolderMax)
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=2000")
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[" + str(
                    FolderNow) + "]/div[1]").click()

            b = 1
        except:
            pass

def refreshByK(driver,k):
    b = 0
    while b == 0:
        try:
            driver.refresh()
            time.sleep(1)

            sentry_2 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[" + str(k) + "]")
            driver.execute_script("arguments[0].scrollIntoView();", sentry_2)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            sentry_2.find_element_by_xpath("./label/span[2]").click()

            time.sleep(1)
            b = 1

        except:
            pass