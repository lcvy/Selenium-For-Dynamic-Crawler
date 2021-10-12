import os
import time
import check

import login
import memory
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

#
import get
import time
import click
import refresh


class go:
    j = 0
    driver = login.Login()
    sentry_1 = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]").\
        find_elements_by_class_name(
        "collapse-list-item")
    for i in sentry_1:
        j = j + 1
    ##统计好侧边数量
    k = 106
    xwl_1 = 1
    xwl_2 = 1

    while k <= j:
        ###获取栏目名称
        try:
            driver.execute_script("var q=document.documentElement.scrollTop=0")
            sentry_2 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[" + str(k) + "]")
            driver.execute_script("arguments[0].scrollIntoView();", sentry_2)
            time.sleep(0.5)
        except:
            refresh.refreshByK(driver,k)

        title_1 = sentry_2.find_element_by_xpath(
            "./label/span[2]").text
        try:
            os.mkdir("../reporter/" + title_1)
        except:
            pass

        # action = ActionChains(driver)
        # action.move_by_offset(100,300)
        # driver.execute_script("window.scrollBy(0,200)")

        driver.execute_script("arguments[0].scrollIntoView();", sentry_2)
        driver.execute_script("var q=document.documentElement.scrollTop=0")
        sentry_2.find_element_by_xpath("./label/span[2]").click()
        ###########

        ###初始化
        time.sleep(1)
        PageFloderMax = get.GetPageFolderMax(driver)
        if PageFloderMax >= 3:
            PageFloderMax = 3
        if xwl_1 == 1:
            PageFloderNow = 3
            xwl_1 = 0
        else:
            PageFloderNow = 1
        ##########

        while PageFloderNow <= PageFloderMax :
            ###初始化
            if xwl_2 == 1:
                FolderNow = 2
                xwl_2 = 0
            else:
                FolderNow = 1

            FolderMax = get.GetFloderMax(driver,k,PageFloderNow,PageFloderMax,FolderNow)

            ##########
            click.clickFolder(driver,k,PageFloderNow,PageFloderMax,FolderNow)
            check.Check_clickPageforFolder(driver,PageFloderNow,PageFloderMax,k,FolderNow)

            while FolderNow <= FolderMax:
                ###定位元素,创建文件夹
                time.sleep(1)

                b = 0
                while b == 0:
                    try:
                        sentry_2 = driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[" + str(
                                FolderNow) + "]/div[1]")
                        b = 1
                    except:
                        refresh.refreshFolder(driver,k,PageFloderNow,PageFloderMax,FolderNow)


                title_2 = sentry_2.find_element_by_xpath("./span").text
                os.mkdir("../reporter/" + title_1 + "/" + title_2)
                fold_name = "../reporter/" + title_1 + "/" + title_2
                fold_name_1 = "./reporter/" + title_1 + "/" + title_2
                ##########

                b = 0
                while b == 0:
                    try:
                        sentry_2.click()
                        b = 1
                    except:
                        refresh.refreshFolder(driver,k,PageFloderNow,PageFloderMax,FolderNow)

                ###初始化元素
                PageFileNow = 1
                PageFileMax = get.GetPageFileMax(driver)

                ##########

                while PageFileNow <= PageFileMax:
                    ###初始化
                    FileNow = 1
                    FileMax = get.GetFileMax(driver,k,PageFloderNow,PageFloderMax,PageFileNow,PageFileMax,FolderNow,FileNow)
                    ##########

                    while FileNow <= FileMax:  ##选择文件
                        b = 0
                        while b == 0:
                            try:
                                sentry_2 = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[" + str(
                                        FileNow) + "]")
                                b = 1
                            except:
                                b = refresh.refreshFile(driver,k,PageFloderNow,PageFloderMax,PageFileNow,PageFileMax,FolderNow,FileNow)

                        memory.MemoryFile(driver, sentry_2, fold_name,fold_name_1, FileNow,k,PageFloderNow,PageFloderMax,PageFileNow,PageFileMax,FolderNow,FileNow)
                        # click.clickFile(driver,k,PageFloderNow,PageFloderMax,PageFileNow,PageFileMax,FolderNow,FileNow)
                        FileNow = FileNow + 1

                    ###跳出FileNow循环
                    PageFileNow = PageFileNow + 1
                    check.Check_clickPageforFile(driver, PageFileNow, PageFileMax,k,PageFloderNow,PageFloderMax,FolderNow,FileNow)


                FolderNow = FolderNow + 1
                click.clickFolder(driver,k,PageFloderNow,PageFloderMax,FolderNow)
                time.sleep(1)
                check.Check_clickPageforFolder(driver,PageFloderNow,PageFloderMax,k,FolderNow)
                # if FolderNow > FolderMax:
                #     exit(0)


            PageFloderNow = PageFloderNow + 1
            check.Check_clickPageforFolder(driver, PageFloderNow, PageFloderMax,k,FolderNow)

        # exit(0)
        k = k + 1
