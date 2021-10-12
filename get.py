import time
import refresh


# def GetPageFloderNow(driver,k,p1,p2):
#     b = 0
#     while b == 0:
#         try:
#             time.sleep(1)
#             page_floder_now = int(driver.find_element_by_xpath(
#                 "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
#                 "li[@class='number active']").text)
#             time.sleep(1)
#             b = 1
#         except:
#             refresh.refreshFolder(driver,k,p1,p2)
#
#     return page_floder_now

def GetPageFolderMax(driver):
    b = 0
    while b == 0:
        try:
            text = []
            time.sleep(1)
            sentry = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_elements_by_xpath(
                "li")
            time.sleep(1)
            sentry_1 = 1
            for sentry_2 in sentry:
                if sentry_2.text == '':
                    continue
                text.insert(sentry_1, int(sentry_2.text))

            page_folder_all = max(text)
            b = 1
        except:
            pass

    return int(page_folder_all)

def GetFloderMax(driver,k,p1,p2,FolderNow):
    b = 0
    while b == 0:
        try:
            FloderMax = 0
            time.sleep(1)
            sentry_1 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]"
            ).find_elements_by_class_name("report-list-item")
            time.sleep(1)
            for sentry_2 in sentry_1:
                FloderMax = FloderMax + 1
            b = 1
        except:
            refresh.refreshFolder(driver,k,p1,p2,FolderNow)

    return FloderMax

# def GetPageFileNow(driver,k,p1,p2,p3,p4):
#    b = 0
#    while b == 0:
#        try:
#            time.sleep(1)
#            page_file_now = int(driver.find_element_by_xpath(
#                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_element_by_xpath(
#                "li[@class='number active']").text)
#            b = 1
#        except:
#            refresh.refreshFile(driver,k,p1,p2,p3,p4)
#
#    return int(page_file_now)

def GetFileMax(driver,k,p1,p2,p3,p4,FolderNow,FileNow):
    b = 0
    while b == 0:
        try:
            time.sleep(1)
            FileMax = 0
            sentry_1 = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[1]"
            ).find_elements_by_xpath("./div[@class='report-list-item']")
            for sentry_2 in sentry_1:
                FileMax = FileMax + 1
            b = 1
        except:
            refresh.refreshFile(driver,k,p1,p2,p3,p4,FolderNow,FileNow)

    return FileMax
def GetPageFileMax(driver):
    b = 0
    while b == 0:
        try:
            time.sleep(1)
            text = []
            time.sleep(1)
            sentry = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/ul").find_elements_by_xpath(
                "li")
            sentry_1 = 1
            for sentry_2 in sentry:
                if sentry_2.text == '':
                    continue
                text.insert(sentry_1, int(sentry_2.text))

            page_file_all = max(text)
            b = 1
        except:
            pass

    return page_file_all