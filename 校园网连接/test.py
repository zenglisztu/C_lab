# from selenium import webdriver
# # from time import sleep
# # from selenium.webdriver.common.by import By
# #
# # browser = webdriver.Chrome('chromedriver.exe')
# # browser.maximize_window()
# # browser.get('https://pvp.qq.com/web201605/wallpaper.shtml')
# # sleep(2)
# # for i in range(31):
# #     if i < 1 :
# #         pass
# #     elif i < 10 :
# #         xp = '//*[@id="Page_Container_267733"]/a[12]'
# #         next_page = browser.find_element(By.XPATH,xp)
# #         next_page.click()
# #         sleep(0.5)
# #     else :
# #         xp = '//*[@id="Page_Container_267733"]/a[13]'
# #         next_page = browser.find_element(By.XPATH,xp)
# #         next_page.click()
# #         sleep(0.5)
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import re
# import account
# import numpy as np
# import xlwings as xw
# import os
#
# #sztu网址
# url = 'https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=jiaowu'
# #规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
# #实例化浏览器对象
# browser = webdriver.Chrome(executable_path='chromedriver.exe',options=option)
# browser.implicitly_wait(5)
# #打开登录网页
# browser.get(url)
# browser.maximize_window()
# #登录
# browser.find_element(By.ID,'j_username').send_keys(account.sztu_u)
# browser.find_element(By.ID,'j_password').send_keys(account.sztu_p)
# browser.find_element(By.ID,'loginButton').click()
# #找到课程信息查询
# browser.find_element(By.XPATH,'//*[@id="accordion"]/li[5]/div').click()
# browser.find_element(By.XPATH,'//*[@id="accordion"]/li[5]/ul/li[3]/div').click()
# browser.find_element(By.ID,'NEW_XSD_PYGL_XKGL_KCSEARCH').click()
# #切入iframe
# browser.switch_to.frame('Frame1')
# #利用正则表达式找出所有学院
# colleges = re.findall(pattern=r'<option.*?>(.*?)<',string=browser.page_source,flags=re.DOTALL)[1:]
# for college in colleges:
#     print(college)
#     #选择学院
#     select = Select(browser.find_element(By.ID,'kkyx'))
#     select.select_by_visible_text(college)
#     #查询
#     browser.find_element(By.XPATH,'//*[@id="search-form-content"]/div[4]/div/button[2]').click()
#     #切出iframe
#     browser.switch_to.default_content()
#     sleep(1)
#     #切入iframe
#     browser.switch_to.frame('Frame1')
#     browser.switch_to.frame('fcenter')
#     #利用正则表达式匹配出总页数
#     pages = re.findall(pattern=r'>/(\w+)页<',string=browser.page_source,flags=re.DOTALL)[0]
#     pages = int(pages)
#     print(pages)
#     # for page in range(pages):
#     #     if page < 1:
#     #         pass
#     #     elif page <2:
#     #         browser.find_element(By.XPATH,'//*[@id="Form1"]/div/a/i[1]').click()
#     #     else:
#     #         browser.find_element(By.XPATH, '//*[@id="Form1"]/div/a[2]/i[1]').click()
#     #     table_text = browser.page_source
#     #     table_content = re.findall(pattern=r'<td>(.*?)<', string=table_text, flags=re.DOTALL)
#     #     print(table_content)
#     #     sleep(1)
# # //*[@id="Form1"]/div/span[3]/i[2]
# # //*[@id="Form1"]/div/a[2]/i[1]
# # //*[@id="Form1"]/div/a[2]/i[1]
# #//*[@id="Form1"]/div/span[4]/i[1]
#     browser.switch_to.parent_frame()
# browser.quit()

text = '''1.</p><p>1. 协方差的计算步骤：
2.          a. 求分别求两个指标A、B各自的平均值x1、x2；
          b. 分别将指标A、B中的数值减去各自的平均值x1、x2得到两组新的数值An、Bn；
          c. 将An、Bn中的数值按顺序两两配对并相乘，如果一对数值的乘积是正数表示正相关，负数表示负相关。由每对数值的乘积得到一组数值Sn；
          d. 求Sn的平均值，结果是正数表示整体上是正相关，负数表示整体上是负相关。
3.2. 协方差的结果为正数，则大多数据为正相关；结果为负数，则大多数据为负相关。协方差的大小受到原来指标的数据范围的影响，所以在数据集比较时往往会出现偏差，为了抵消数据范围的影响，使用协方差除以两个指标各自的标准差得到相关系数。
4.3. 回归分析（regression analysis）根据已有的各种数据自动总结出函数来描述指标之间的数值关系。利用分析函数可以对数据进行预测。
5.4 一元线性回归通过一个指标预测另一个指标，每条拟合线都可以写成一个一元线程方程，比如 y = 0.2x + 10 这种形式，找出所有方程中平方和最小的那个就是最理想的预测模型。一元线性回归以平方和最小值为标准进行筛选，这种方法也称为“最小二乘法”。
6.5 即使数据不相关，同样可以使用线性回归得到理想模型，但是这个模型是没有任何用处的。在做回归分析时需要先评价指标是否相关，比如使用相关系数评价，对具有相关性的数据做回归分析才有意义。
7.6 考虑到很多方面的因素，在做简单的线性回归时实际使用的是它的平方来表示模型的好坏，也就是R²（拟合优度）。R²越大，相关性越强，回归模型更有意义。在使用各种回归分析的时候不仅要看回回归模型本身，还一定要看R²是否是正数，是否接近于1。R²是单独的一个用来评价回归模型优劣的指标，当做简单线性回归分析时，R²恰好等于(相关系数)²，当做复杂回归分析时，R²则与(相关系数)²没有相等关系，最大值为+1，代表模型可以完美拟合真实数据，最小可以是负无穷大-∞，代表模型完全无法拟合数据。
'''

# byte = text.encode()
# print(byte)
#
# with open(r'./测试.txt','wb') as f:
#     f.write(byte)

#监测网络是否连接成功

# import time
# ret = os.system('ping baidu.com -n 1') == 0
# start = time.time()
# while not ret:
#     print('正在连接')
#     try:
#         # import 一键联网
#         pass
#     except:
#         pass
#     ret = os.system('ping baidu.com -n 1') == 0
#     print(time.time() - start)
#     if time.time() - start > 10:
#         print('连接超时')
#         break
# print(ret == 0)

# os.system(r'start C:\Users\曾立\Desktop\全国高等院校信息满意度.xlsx')

# ls = [2, 3, 4, 7, 8, 10, 21, 44, 56, 78, 94,93]
# print(min(ls[3:]))

# def f(m,n):
#     if m > n:
#         m,n = n,m
#     i = n
#     while True:
#         if (i%m == 0) and (i%n == 0):
#             break
#         i += 1
#     return i
# f(2,3)

# import random
# # rang1 = eval(input("请设置本局游戏的最小值："))
# # rang2= eval(input ("请设置本局游戏的最大值："))
# # num= random.randint(rang1,rang2)
# # guess = ''
# # print("数字猜谜游戏！")
# # i=0
# # while guess != num:
# #     i += 1
# #     guess=eval(input("请输人你猜的数字："))
# #     if guess == num:
# #         print("恭喜，你猜对了！")
# #     elif guess < num:
# #         print('你猜的数小了……')
# #     else:
# #         print('你猜的数大了……')
# # print('你总共猜了%d' %i+"次")
#
# from os.path import dirname
# print(dirname(__file__))

# import PySimpleGUI as sg
# import re
#
# # 主题设置
# sg.theme('DarkTeal7')
#
# # 布局设置
# layout = [
#     [sg.Text('待转化的文件是：', font=("微软雅黑", 12)),
#      sg.Text('', key='filename', size=(50, 1), font=("微软雅黑", 10), text_color='blue')],
#     [sg.Text('程序操作记录', justification='center')],
#     [sg.Output(size=(80, 20), font=("微软雅黑", 10))],
#     [sg.FileBrowse('选择文件', key='file', target='filename'), sg.Button('开始转化'), sg.Button('关闭程序')]
# ]
#
# # 创建窗口
# window = sg.Window('pdf转word工具，作者@微信公众号：可以叫我才哥', layout, font=("微软雅黑", 15),
#                    default_element_size=(50, 1))
#
# # 事件循环
# while True:
#     event, values = window.read()
#     if event in (None, '关闭程序'):
#         break
#     if event == '开始转化':
#         if values['file'] and re.findall(r'\.(\S+)', values['file'])[0] == 'pdf':
#             fileName = values['file']
#             pdf_to_word(fileName)
#             print('\n----------转化完毕----------\n')
#         else:
#             print('文件未选取或文件非pdf文件\n请先选择文件')
#
# window.close()

# from pdf2docx import Converter
#
# pdf_file = r'C:\Users\曾立\Desktop\新建文件夹\番禺区小学每周一古诗文内容（2022年9月24修订，下发学校）.pdf'
# docx_file = r'C:\Users\曾立\Desktop\新建文件夹\sample.docx'
#
# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file, start=91, end=102)
# cv.close()

# import subprocess
# cmd = 'start C:\myprojects\enhance\PdfToWord.py'
# screenData = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
# while True:
#     line = screenData.stdout.readline()
#     print(line.decode('gbk').strip("b'"))
#     if line == b'' or subprocess.Popen.poll(screenData) == 0:
#         screenData.stdout.close()
#         break



# from selenium import webdriver
# from time import sleep,time
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
#
# #主页网址
# user_url = 'http://47.98.217.39/lfradius/login.php?c=login&a=showlogin'
#
# #UA伪装
# header = {
#     'cookie': 'ttcid=66e29ab116954f398591df390e08ffb518; d_ticket=eaf0ec68c3a65f33bb9ede0ab78e39fe00dee; odin_tt=7e68f4c6fb6f21cecb92ff5d105d2563115ca9a23909babeb0af081a62149490d8a1786ed61e4209899d833efb66b8dc862c710499ef99a7ccdfaa82d546b59a; sid_guard=e8d81e25f59b66d3e2f573130924dc76%7C1646993490%7C5184000%7CTue%2C+10-May-2022+10%3A11%3A30+GMT; ttwid=1%7CNoAgiKral9Fe9V8rFlIMCbP_t7wFvcOXqBU1XksiFKY%7C1668320892%7C2208072d9589fa50ac026a5dfb92d26ab9d0a90312c103419f2bdd15a35fb096; s_v_web_id=verify_laez6qcb_8g1YcTTV_sRZC_4oK8_AgCp_COsU141mRcPj; passport_csrf_token=301b7affd1a4207203343978812e1989; passport_csrf_token_default=301b7affd1a4207203343978812e1989; xgplayer_user_id=866431456838; douyin.com; csrf_session_id=3b061c842cdb8d2086ae73959c58cc2d; AB_LOGIN_GUIDE_TIMESTAMP=%221669288065596%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221124%22; __ac_nonce=0637f65f1008cc6c297a8; __ac_signature=_02B4Z6wo00f01rlicBgAAIDBcd65B4N-jA65R3SAAM00pnlziACn1ON.32OA5BdEq9r.5L7ikNGIoEQoFIWgXRaWzgfXfVl8.6-DZMK9NNlgULUd6qiPK.HJy1UetZMImcqzTGLgKnfFtVPL80; strategyABtestKey=%221669293585.112%22; msToken=eJdz2vm-hDJd9EzoPRI5rvm0ESAJsIKovsOhOdAi-B1FO64Js_OTjImc2SwKatXEBHD0gH37pia4ise5r6yo4H3rAlj9uJVsZLv3lbxc3QOsHBCIfV6umIInJmzbugM=; home_can_add_dy_2_desktop=%221%22; tt_scid=gqMrwo-OlTlp6rlDZVRd4Qc8qDg7qV334RLaLi7qB0dHWifcO0xoagtiFpdM3wmd48a5; msToken=2HH-ftY7l0W1Ok55TkpHjbl2e8y5b5Avo64G7BjeFeLnXg6jQ_JCnT6dUYu5VH2emsQvuP9iWZE8iyk4yBfHbV0P1yi_gWOw5mR01ZgAhzAOY3Lp7wbrqm4-Km5cyxE=',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
#
# #规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
#
# #无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--window-size=1920,1080")
#
# #监测计算机是否连网成功
# ret = False
#
# # 记录开始时间
# start = time()
# while not ret:
#     print('正在尝试连接..........')
#     try:
#         # 创建谷歌浏览器对象
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[1]/div/div/input').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[2]/div/div/input').send_keys('sztu@123456')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[3]/div/input').click()
#         #连网
#         browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(5)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     except:
#         url = 'http://uim.sztu.edu.cn/accounts/login/?next=/o/authorize/%3Fclient_id%3D1ooiwJOvupSHwT41DxN4VfZNzzhXE8qOYFXrNFyy%26redirect_uri%3Dhttp%253A%252F%252F172.19.0.5%252Fsrun_portal_sso%26response_type%3Dcode%26state%3DSrun%2BPortal'
#         # 创建谷歌浏览器对象
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('sztu@123456')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="userForm"]/div[3]/button').click()
#         #连网
#         #browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(5)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     #判断连接是否超时
#     elapsed_time = time() - start
#     if elapsed_time > 60:
#         print('连接超时，退出本次连接！')
#         break
#
#     # 监测计算机是否连网成功
#     ret = os.system('ping baidu.com -n 1') == 0
#
# # # 终止浏览器驱动进程
# # os.system(r'taskkill /im chromedriver.exe /f')
# # #终止谷歌浏览器进程
# # os.system(r'taskkill /im chrome.exe /f')


# import tkinter as tk
#
#
# class CourseTable:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Course Schedule")
#
#         # 创建表格
#         self.table = tk.Table(master, rows=4, cols=4)
#         self.table.pack()
#
#         # 添加表头
#         self.table.insert(tk.END, 0, "Course Name")
#         self.table.insert(tk.END, 1, "Teacher Name")
#         self.table.insert(tk.END, 2, "Time")
#         self.table.insert(tk.END, 3, "Venue")
#
#         # 添加课程信息
#         for i in range(4):
#             row = tk.Row(self.table)
#             cell = tk.Label(row, text=f"{i + 1}.{self.table.get(i, 0)}")
#             cell.grid(row=i + 1, column=0, columnspan=4)
#
#             # 添加课程时间和地点
#             for j in range(4):
#                 cell = tk.Entry(row, width=2)
#                 cell.grid(row=i + 1, column=j + 1)
#                 cell.insert(0, f"{self.table.get(i, j + 1)}:{self.table.get(i, j + 2)}")
#
#                 # 添加课程信息
#         for i in range(4):
#             row = tk.Row(self.table)
#             cell = tk.Label(row, text=f"{i + 1}.{self.table.get(i, 0)}")
#             cell.grid(row=i + 1, column=0, columnspan=4)
#
#             # 添加课程时间和地点
#             for j in range(4):
#                 cell = tk.Entry(row, width=2)
#                 cell.grid(row=i + 1, column=j + 1)
#                 cell.insert(0, f"{self.table.get(i, j + 1)}:{self.table.get(i, j + 2)}")
#
#                 # 显示表格
#         self.table.grid(row=0, column=0, columnspan=4)
#
#         # 创建按钮
#         self.create_button()
#
#     def create_button(self):
#         # 创建按钮
#         button = tk.Button(self.master, text="Add", command=self.add_course)
#         button.grid(row=0, column=0, columnspan=4)
#
#     def add_course(self):
#         # 添加课程信息
#         course_name = tk.StringVar()
#         teacher_name = tk.StringVar()
#         time = tk.StringVar()
#         venue = tk.StringVar()
#
#         # 添加课程信息
#         for i in range(4):
#             row = tk.Row(self.table)
#             cell = tk.Label(row, text=f"{i + 1}.{self.table.get(i, 0)}")
#             cell.grid(row=i + 1, column=0, columnspan=4)
#
#             # 添加课程时间和地点
#             for j in range(4):
#                 cell = tk.Entry(row, width=2)
#                 cell.grid(row=i + 1, column=j + 1)
#                 cell.insert(0, f"{self.table.get(i, j + 1)}")

#
# from selenium import webdriver
# from time import sleep,time
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
#
# #主页网址
# user_url = 'http://47.98.217.39/lfradius/login.php?c=login&a=showlogin'
#
# #UA伪装
# header = {
#     'cookie': 'ttcid=66e29ab116954f398591df390e08ffb518; d_ticket=eaf0ec68c3a65f33bb9ede0ab78e39fe00dee; odin_tt=7e68f4c6fb6f21cecb92ff5d105d2563115ca9a23909babeb0af081a62149490d8a1786ed61e4209899d833efb66b8dc862c710499ef99a7ccdfaa82d546b59a; sid_guard=e8d81e25f59b66d3e2f573130924dc76%7C1646993490%7C5184000%7CTue%2C+10-May-2022+10%3A11%3A30+GMT; ttwid=1%7CNoAgiKral9Fe9V8rFlIMCbP_t7wFvcOXqBU1XksiFKY%7C1668320892%7C2208072d9589fa50ac026a5dfb92d26ab9d0a90312c103419f2bdd15a35fb096; s_v_web_id=verify_laez6qcb_8g1YcTTV_sRZC_4oK8_AgCp_COsU141mRcPj; passport_csrf_token=301b7affd1a4207203343978812e1989; passport_csrf_token_default=301b7affd1a4207203343978812e1989; xgplayer_user_id=866431456838; douyin.com; csrf_session_id=3b061c842cdb8d2086ae73959c58cc2d; AB_LOGIN_GUIDE_TIMESTAMP=%221669288065596%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221124%22; __ac_nonce=0637f65f1008cc6c297a8; __ac_signature=_02B4Z6wo00f01rlicBgAAIDBcd65B4N-jA65R3SAAM00pnlziACn1ON.32OA5BdEq9r.5L7ikNGIoEQoFIWgXRaWzgfXfVl8.6-DZMK9NNlgULUd6qiPK.HJy1UetZMImcqzTGLgKnfFtVPL80; strategyABtestKey=%221669293585.112%22; msToken=eJdz2vm-hDJd9EzoPRI5rvm0ESAJsIKovsOhOdAi-B1FO64Js_OTjImc2SwKatXEBHD0gH37pia4ise5r6yo4H3rAlj9uJVsZLv3lbxc3QOsHBCIfV6umIInJmzbugM=; home_can_add_dy_2_desktop=%221%22; tt_scid=gqMrwo-OlTlp6rlDZVRd4Qc8qDg7qV334RLaLi7qB0dHWifcO0xoagtiFpdM3wmd48a5; msToken=2HH-ftY7l0W1Ok55TkpHjbl2e8y5b5Avo64G7BjeFeLnXg6jQ_JCnT6dUYu5VH2emsQvuP9iWZE8iyk4yBfHbV0P1yi_gWOw5mR01ZgAhzAOY3Lp7wbrqm4-Km5cyxE=',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
#
# #规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
#
# #无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--window-size=1920,1080")
#
# #监测计算机是否连网成功
# ret = False
#
# # 记录开始时间
# start = time()
# while not ret:
#     print('正在尝试连接..........')
#     try:
#         # 创建谷歌浏览器对象
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[1]/div/div/input').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[2]/div/div/input').send_keys('sztu@123456')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[3]/div/input').click()
#         #连网
#         browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(1)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     except:
#         url = 'http://uim.sztu.edu.cn/accounts/login/?next=/o/authorize/%3Fclient_id%3D1ooiwJOvupSHwT41DxN4VfZNzzhXE8qOYFXrNFyy%26redirect_uri%3Dhttp%253A%252F%252F172.19.0.5%252Fsrun_portal_sso%26response_type%3Dcode%26state%3DSrun%2BPortal'
#         # 创建谷歌浏览器对象
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#         #统一认证
#         #browser.find_element(By.XPATH,'//*[@id="app"]/section/div[1]/div[5]/div[2]/span').click()
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('SZtu@012019')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="login-account"]').click()
#         #连网
#         #browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(1)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     #判断连接是否超时
#     elapsed_time = time() - start
#     if elapsed_time > 60:
#         print('连接超时，退出本次连接！')
#         break
#
#     # 监测计算机是否连网成功
#     ret = os.system('ping baidu.com -n 1') == 0

# # 终止浏览器驱动进程
# os.system(r'taskkill /im chromedriver.exe /f')
# #终止谷歌浏览器进程
# os.system(r'taskkill /im chrome.exe /f')



























# ##Chrome浏览器
# from selenium import webdriver
# from time import sleep,time
# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
#
# #主页网址
# user_url = 'http://47.98.217.39/lfradius/login.php?c=login&a=showlogin'
#
# #UA伪装
# header = {
#     'cookie': 'ttcid=66e29ab116954f398591df390e08ffb518; d_ticket=eaf0ec68c3a65f33bb9ede0ab78e39fe00dee; odin_tt=7e68f4c6fb6f21cecb92ff5d105d2563115ca9a23909babeb0af081a62149490d8a1786ed61e4209899d833efb66b8dc862c710499ef99a7ccdfaa82d546b59a; sid_guard=e8d81e25f59b66d3e2f573130924dc76%7C1646993490%7C5184000%7CTue%2C+10-May-2022+10%3A11%3A30+GMT; ttwid=1%7CNoAgiKral9Fe9V8rFlIMCbP_t7wFvcOXqBU1XksiFKY%7C1668320892%7C2208072d9589fa50ac026a5dfb92d26ab9d0a90312c103419f2bdd15a35fb096; s_v_web_id=verify_laez6qcb_8g1YcTTV_sRZC_4oK8_AgCp_COsU141mRcPj; passport_csrf_token=301b7affd1a4207203343978812e1989; passport_csrf_token_default=301b7affd1a4207203343978812e1989; xgplayer_user_id=866431456838; douyin.com; csrf_session_id=3b061c842cdb8d2086ae73959c58cc2d; AB_LOGIN_GUIDE_TIMESTAMP=%221669288065596%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221124%22; __ac_nonce=0637f65f1008cc6c297a8; __ac_signature=_02B4Z6wo00f01rlicBgAAIDBcd65B4N-jA65R3SAAM00pnlziACn1ON.32OA5BdEq9r.5L7ikNGIoEQoFIWgXRaWzgfXfVl8.6-DZMK9NNlgULUd6qiPK.HJy1UetZMImcqzTGLgKnfFtVPL80; strategyABtestKey=%221669293585.112%22; msToken=eJdz2vm-hDJd9EzoPRI5rvm0ESAJsIKovsOhOdAi-B1FO64Js_OTjImc2SwKatXEBHD0gH37pia4ise5r6yo4H3rAlj9uJVsZLv3lbxc3QOsHBCIfV6umIInJmzbugM=; home_can_add_dy_2_desktop=%221%22; tt_scid=gqMrwo-OlTlp6rlDZVRd4Qc8qDg7qV334RLaLi7qB0dHWifcO0xoagtiFpdM3wmd48a5; msToken=2HH-ftY7l0W1Ok55TkpHjbl2e8y5b5Avo64G7BjeFeLnXg6jQ_JCnT6dUYu5VH2emsQvuP9iWZE8iyk4yBfHbV0P1yi_gWOw5mR01ZgAhzAOY3Lp7wbrqm4-Km5cyxE=',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
#
# #规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
#
# #无头浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--window-size=1920,1080")
#
# #监测计算机是否连网成功
# ret = False
#
# # 记录开始时间
# start = time()
# while not ret:
#     print('正在尝试连接..........')
#     try:
#         # 创建谷歌浏览器对象
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[1]/div/div/input').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[2]/div/div/input').send_keys('sztu@123456')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[3]/div/input').click()
#         #连网
#         browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(1)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     except:
#         url = 'http://uim.sztu.edu.cn/accounts/login/?next=/o/authorize/%3Fclient_id%3D1ooiwJOvupSHwT41DxN4VfZNzzhXE8qOYFXrNFyy%26redirect_uri%3Dhttp%253A%252F%252F172.19.0.5%252Fsrun_portal_sso%26response_type%3Dcode%26state%3DSrun%2BPortal'
#         # 创建谷歌浏览器对象
#         #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
#         browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
#         browser.maximize_window()
#         browser.implicitly_wait(5)
#
#         #打开网页
#         browser.get(user_url)
#         #统一认证
#         #browser.find_element(By.XPATH,'//*[@id="app"]/section/div[1]/div[5]/div[2]/span').click()
#         #输入账号密码
#         browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('202240191061')
#         browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('SZtu@012019')
#         #登录
#         browser.find_element(By.XPATH,'//*[@id="login-account"]').click()
#         #连网
#         #browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
#         sleep(1)
#
#         #关闭浏览器
#         browser.quit()
#         print('连接成功！')
#         #跳出循环
#         break
#
#     #判断连接是否超时
#     elapsed_time = time() - start
#     if elapsed_time > 60:
#         print('连接超时，退出本次连接！')
#         break
#
#     # 监测计算机是否连网成功
#     ret = os.system('ping baidu.com -n 1') == 0
#
# # # 终止浏览器驱动进程
# # os.system(r'taskkill /im chromedriver.exe /f')
# # #终止谷歌浏览器进程
# # os.system(r'taskkill /im chrome.exe /f')




#edge浏览器
from selenium import webdriver
from time import sleep,time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

#主页网址
user_url = 'http://47.98.217.39/lfradius/login.php?c=login&a=showlogin'

#UA伪装
header = {
    'cookie': 'ttcid=66e29ab116954f398591df390e08ffb518; d_ticket=eaf0ec68c3a65f33bb9ede0ab78e39fe00dee; odin_tt=7e68f4c6fb6f21cecb92ff5d105d2563115ca9a23909babeb0af081a62149490d8a1786ed61e4209899d833efb66b8dc862c710499ef99a7ccdfaa82d546b59a; sid_guard=e8d81e25f59b66d3e2f573130924dc76%7C1646993490%7C5184000%7CTue%2C+10-May-2022+10%3A11%3A30+GMT; ttwid=1%7CNoAgiKral9Fe9V8rFlIMCbP_t7wFvcOXqBU1XksiFKY%7C1668320892%7C2208072d9589fa50ac026a5dfb92d26ab9d0a90312c103419f2bdd15a35fb096; s_v_web_id=verify_laez6qcb_8g1YcTTV_sRZC_4oK8_AgCp_COsU141mRcPj; passport_csrf_token=301b7affd1a4207203343978812e1989; passport_csrf_token_default=301b7affd1a4207203343978812e1989; xgplayer_user_id=866431456838; douyin.com; csrf_session_id=3b061c842cdb8d2086ae73959c58cc2d; AB_LOGIN_GUIDE_TIMESTAMP=%221669288065596%22; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20221124%22; __ac_nonce=0637f65f1008cc6c297a8; __ac_signature=_02B4Z6wo00f01rlicBgAAIDBcd65B4N-jA65R3SAAM00pnlziACn1ON.32OA5BdEq9r.5L7ikNGIoEQoFIWgXRaWzgfXfVl8.6-DZMK9NNlgULUd6qiPK.HJy1UetZMImcqzTGLgKnfFtVPL80; strategyABtestKey=%221669293585.112%22; msToken=eJdz2vm-hDJd9EzoPRI5rvm0ESAJsIKovsOhOdAi-B1FO64Js_OTjImc2SwKatXEBHD0gH37pia4ise5r6yo4H3rAlj9uJVsZLv3lbxc3QOsHBCIfV6umIInJmzbugM=; home_can_add_dy_2_desktop=%221%22; tt_scid=gqMrwo-OlTlp6rlDZVRd4Qc8qDg7qV334RLaLi7qB0dHWifcO0xoagtiFpdM3wmd48a5; msToken=2HH-ftY7l0W1Ok55TkpHjbl2e8y5b5Avo64G7BjeFeLnXg6jQ_JCnT6dUYu5VH2emsQvuP9iWZE8iyk4yBfHbV0P1yi_gWOw5mR01ZgAhzAOY3Lp7wbrqm4-Km5cyxE=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

#规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')

#无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

#监测计算机是否连网成功
ret = False

# 记录开始时间
start = time()
while not ret:
    print('正在尝试连接..........')
    try:
        # 创建Edge浏览器对象
        browser = webdriver.Edge(executable_path=r'msedgedriver.exe',options=option,chrome_options=chrome_options)
        #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
        browser.maximize_window()
        browser.implicitly_wait(5)

        #打开网页
        browser.get(user_url)

        #输入账号密码
        browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[1]/div/div/input').send_keys('202240191061')
        browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[2]/div/div/input').send_keys('sztu@123456')
        #登录
        browser.find_element(By.XPATH,'//*[@id="__user_login"]/div[2]/div/div[3]/div/input').click()
        #连网
        browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
        sleep(1)

        #关闭浏览器
        browser.quit()
        print('连接成功！')
        #跳出循环
        break

    except:
        url = 'http://uim.sztu.edu.cn/accounts/login/?next=/o/authorize/%3Fclient_id%3D1ooiwJOvupSHwT41DxN4VfZNzzhXE8qOYFXrNFyy%26redirect_uri%3Dhttp%253A%252F%252F172.19.0.5%252Fsrun_portal_sso%26response_type%3Dcode%26state%3DSrun%2BPortal'
        # 创建谷歌浏览器对象
        #browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
        browser = webdriver.Edge(executable_path=r'msedgedriver.exe')
        browser.maximize_window()
        browser.implicitly_wait(5)

        #打开网页
        browser.get(user_url)
        #统一认证
        #browser.find_element(By.XPATH,'//*[@id="app"]/section/div[1]/div[5]/div[2]/span').click()
        #输入账号密码
        browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('202240191061')
        browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('SZtu@012019')
        #登录
        browser.find_element(By.XPATH,'//*[@id="login-account"]').click()
        #连网
        #browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
        sleep(1)

        #关闭浏览器
        browser.quit()
        print('连接成功！')
        #跳出循环
        break

    #判断连接是否超时
    elapsed_time = time() - start
    if elapsed_time > 60:
        print('连接超时，退出本次连接！')
        break

    # 监测计算机是否连网成功
    ret = os.system('ping baidu.com -n 1') == 0

# # 终止浏览器驱动进程
# os.system(r'taskkill /im chromedriver.exe /f')
# #终止谷歌浏览器进程
# os.system(r'taskkill /im chrome.exe /f')



# from selenium import webdriver  # 引入模块
# driver = webdriver.Edge()  # 引入edge驱动
# driver.get("https://www.baidu.com/")  # 打开百