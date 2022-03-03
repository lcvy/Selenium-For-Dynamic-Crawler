# Selenium-For-Dynamic-Crawler

## 平台以及爬取对象

单线程爬取：http://report.*********.com/report

平台：Pycharm

语言：Python

主要的库：Selenium

## 网页分析

前端Vue，需要进行点击触发监听事务才会有反馈

爬取PDF文件放在另外的域名网站内

需要进行逐一点击才能获取文件链接Response

偶尔网站更新时会刷新对应唯一的class名称

但位置不变

故使用绝对定位

## 功能文件分类

1. 点击动作 ---  对特定符合筛选条件进行定位
2. 记录动作 ---  写文件、创建文件夹进行记录
3. 刷新动作 ---  防止程序因网络不通而进行不能找到元素而进行报错

## 改进 & 未完成

太多太多了

改进方向 --- 刷新以及动作解耦

未完成 --- 提交的数据单是否存在隐参以及提交的json文件细节

---2021.10.13---
pyautogui --- Python默认GUI库，具有点击等动作
pyperclip --- 用于复制和粘贴剪贴板功能

例：
import pyperclip

pyperclip.copy('正在进行发中文试验') # 复制
pyautogui.hotkey('ctrl', 'v') # 按下组合键的方法，ctrl+v粘贴
pyautogui.press('enter') # 按下按键
