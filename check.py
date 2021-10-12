import click
import refresh

def Check_clickPageforFolder(driver,pageNow,pageMax,k,FolderNow):
    b = 0
    while b == 0:
        try:
            click.clickPageforFolder(driver,pageNow,pageMax)
            b = 1

        except:
            refresh.refreshFolder(driver,k,pageNow,pageMax,FolderNow)
            pass

def Check_clickPageforFile(driver,pageNow,pageMax,k,PageFolderNow,PageFolderMax,FolderNow,FileNow):
    b = 0
    while b == 0:
        try:
            click.clickPageforFile(driver,pageNow,pageMax)
            b = 1
        except:
            refresh.refreshFile(driver,pageNow,pageMax,k,PageFolderNow,PageFolderMax,FolderNow,FileNow)
            pass