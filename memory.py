import os
import time
import selenium
import refresh


def MemoryFile(driver, sentry_2, foldname,foldname_1,sentry,k,p1,p2,p3,p4,FolderNow,FileNow):

    time.sleep(1)
    b = 0
    while b == 0:
        try:
            word = sentry_2.find_element_by_xpath(
                "./div[1]/span"
            ).text
            driver.execute_script("var q=document.documentElement.scrollTop=" + str(-50 + 120 * sentry) + "")
            b = 1

        except:
            refresh.refreshFile(driver,k,p1,p2,p3,p4,FolderNow,FileNow)

    b = 1
    while b == 1:
        try:
            time.sleep(1)
            sentry_2.find_element_by_xpath(
                "./div[1]").click()
            time.sleep(1)
            b = 0
        except:
            a = "未能识别地址"
            with open(foldname + "/url.txt", "a", encoding="utf-8") as file:
                file.write(word + "\n" + a + "\r\n")
            return
    time.sleep(1)
    n = driver.window_handles

    b = 1
    while b == 1:
        try:
            n = driver.window_handles
            time.sleep(1)
            driver.switch_to.window(n[-1])
            time.sleep(1)
            sentry = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/iframe")
            time.sleep(0.5)
            a = sentry.get_attribute('src').strip('http://report.seedsufe.com/PDF/web/viewer.html?file=')
            a = ("https://b")+a+(".pdf")
            b = 0
        except:
            a = "未能成功选择到窗口"
            driver.switch_to.window(n[-1])
            driver.close()
            driver.switch_to.window(n[0])
            with open(foldname + "/url.txt", "a", encoding="utf-8") as file:
                file.write(a + "\n" +" out="+ word+"\n")
            return

    n = driver.window_handles
    while len(n) >= 2:
        b = 0
        while b == 0:
            try:
                n = driver.window_handles
                driver.switch_to.window(n[-1])
                time.sleep(0.5)
                driver.close()
                n = driver.window_handles
                b = 1
            except:
                pass
        time.sleep(1)

    b = 0
    while b == 0:
        try:
            n = driver.window_handles
            driver.switch_to.window(n[0])
            b = 1
        except:
            pass

    with open(foldname + "/url.txt", "a", encoding="utf-8") as file:
        file.write(a + "\n" +" out="+ word+"\n")
    with open("url.txt","a",encoding="utf-8")as file:
        file.write(a + "\n" +" out="+ word+"\n"+" dir="+foldname_1+'\n')