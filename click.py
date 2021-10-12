import time
import refresh


def clickFile(driver,k,p1,p2,p3,p4,FolderNow,FileNow):
    b = 0
    while b == 0:
        try:
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]").click()
            time.sleep(0.5)
            b = 1
        except:
            refresh.refreshFile(driver,k,p1,p2,p3,p4,FolderNow,FileNow)

def clickFilewithout(driver):

        driver.execute_script("var q=document.documentElement.scrollTop=0")
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]").click()
        time.sleep(0.5)
        b = 1



def clickFolder(driver,k,p1,p2,FolderNow):
    b = 0
    while b == 0:
        try:
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]").click()
            time.sleep(0.5)
            b = 1
        except:
            refresh.refreshFolder(driver,k,p1,p2,FolderNow)

def clickFolderwithout(driver):
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]").click()
        time.sleep(0.5)
        b = 1



def clickPageforFile(driver,pageNow,pageMax):
    if pageNow > pageMax:
        return
    sentry = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul"
    ).find_element_by_xpath(
        "./li[@class='number active']"
    ).text
    if pageNow == int(sentry):
        return
    b = 1
    sentry_3 = 2

    while b > 0:
        time.sleep(1)
        driver.execute_script("var q=document.documentElement.scrollTop=2000")
        c = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_elements_by_xpath(
            "li[@class = 'number']")
        text = []
        time.sleep(1)
        sentry_1 = 1
        for sentry_2 in c:
            text_1 = sentry_2.text
            if text_1 == '':
                continue
            text.insert(sentry_1, int(text_1))
            sentry_1 = sentry_1 + 1
        if pageNow in text:

            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=2000")
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
                "//li[contains(text(),\"" + str(pageNow) + "\")]").click()
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            b = 0
        else:
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=2000")
            sentry = 2

            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
                    "//li[contains(text(),\"" + str(sentry_3) + "\")]").click()
                sentry_3 = sentry_3 + 2
            except:
                clickFilewithout(driver)
                pass
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            time.sleep(2)

def clickPageforFolder(driver,pageNow,pageMax):
    if pageNow > pageMax:
        return
    sentry = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul"
    ).find_element_by_xpath(
        "./li[@class='number active']"
    ).text
    if pageNow == int(sentry):
        return

    b = 1
    sentry_3 = 2
    while b > 0:
        time.sleep(1)
        c = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").\
            find_elements_by_xpath(
            "li[@class = 'number']")
        text = []
        time.sleep(1)
        sentry_1 = 1
        for sentry_2 in c:
            text_1 = sentry_2.text
            if text_1 == '':
                continue
            text.insert(sentry_1, int(text_1))
            sentry_1 = sentry_1 + 1


        if pageNow in text:
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=2000")
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
                "//li[contains(text(),\"" + str(pageNow) + "\")]").click()
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            b = 0
        else:
            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=2000")
            time.sleep(1)


            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
                    "//li[contains(text(),\"" + str(sentry_3) + "\")]").click()
                sentry_3 = sentry_3 + 2
            except:
                clickFolderwithout(driver)
                pass

            time.sleep(1)
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            time.sleep(1)