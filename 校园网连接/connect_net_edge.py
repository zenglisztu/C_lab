from selenium import webdriver
from time import sleep,time
from selenium.webdriver.common.by import By
import os
import sys
from pathlib import Path
import re

# 宿舍主页网址
user_url_s = 'http://47.98.217.39/lfradius/login.php?c=login&a=showlogin'
# 公共区域主页网址
user_url_c = 'http://172.19.0.5'

def red_id_password():
    print("正在读取账号信息..........")
    #获取文件绝对路径
    file = list(Path(os.path.abspath(sys.argv[0])).parent.glob('*.txt*'))[0]
    # 读取账号及密码
    with open(file, 'r', encoding='utf-8') as f:
        cnt = f.read()
        id_ls = re.findall(r'[:：](.+)\n', cnt)

    return id_ls


if __name__ == '__main__':
    id_cnt = red_id_password()
    #宿舍区域账号及密码
    id1 = id_cnt[0].replace(" ",'')
    password1 = id_cnt[1].replace(" ",'')

    #公共区域账号及密码
    id2 = id_cnt[2].replace(" ",'')
    password2 = id_cnt[3].replace(" ",'')
    #print(id1,password1,id2,password2)
    #监测计算机是否连网成功
    ret = False
    # 记录开始时间
    start = time()
    # 创建Edge浏览器对象
    browser = webdriver.Edge(executable_path=r'msedgedriver.exe')
    while not ret:
        print('正在尝试连接..........')
        try:
            # browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option)
            #窗口最大化
            #browser.maximize_window()
            browser.implicitly_wait(5)
            # 打开网页
            browser.get(user_url_s)
            # 输入账号密码
            browser.find_element(By.XPATH, '//*[@id="__user_login"]/div[2]/div/div[1]/div/div/input').send_keys(id1)
            browser.find_element(By.XPATH, '//*[@id="__user_login"]/div[2]/div/div[2]/div/div/input').send_keys(password1)
            # 登录
            browser.find_element(By.XPATH, '//*[@id="__user_login"]/div[2]/div/div[3]/div/input').click()
            # 连网
            browser.find_element(By.XPATH, '//*[@id="bs-navbar"]/div/button[1]').click()
            sleep(5)

            # 关闭浏览器
            browser.quit()
            print('连接成功！')
            # 跳出循环
            break

        except:

            # 连接网络
            try:
                #url = 'http://uim.sztu.edu.cn/accounts/login/?next=/o/authorize/%3Fclient_id%3D1ooiwJOvupSHwT41DxN4VfZNzzhXE8qOYFXrNFyy%26redirect_uri%3Dhttp%253A%252F%252F172.19.0.5%252Fsrun_portal_sso%26response_type%3Dcode%26state%3DSrun%2BPortal'
                # 创建谷歌浏览器对象
                # browser = webdriver.Chrome(executable_path=r'C:\myprojects\enhance\chromedriver.exe',options=option,chrome_options=chrome_options)
                # browser = webdriver.Edge(executable_path=r'msedgedriver.exe')
                # browser.maximize_window()
                # browser.implicitly_wait(5)
                #
                # # 打开网页
                # browser.get(user_url_c)
                # 统一认证
                # browser.find_element(By.XPATH,'//*[@id="app"]/section/div[1]/div[5]/div[2]/span').click()
                # 输入账号密码
                browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(id2)
                browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password2)
                # 登录
                browser.find_element(By.XPATH, '//*[@id="login-account"]').click()
                # 连网
                # browser.find_element(By.XPATH,'//*[@id="bs-navbar"]/div/button[1]').click()
                sleep(5)

                # 关闭浏览器
                browser.quit()
                print('连接成功！')
                # 跳出循环
                break
            except:
                pass

        #判断连接是否超时
        elapsed_time = time() - start
        if elapsed_time > 60:
            print('连接超时，退出本次连接！')
            break

        # 监测计算机是否连网成功
        ret = os.system('ping baidu.com -n 1') == 0