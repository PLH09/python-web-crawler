%reset -f
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import csv
url='https://mops.twse.com.tw/mops/web/t108sb19_q1'
driverpath=r'C:\Users\User\anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver-v0.29.1-win64\geckodriver.exe'
options=Options()
#在背景執行
options.add_argument("--headless")
browser=webdriver.Firefox(firefox_options=options,
                          executable_path=driverpath)
browser.get(url)

#%%
#輸入股票代碼
ticker = 2330
code=browser.find_element_by_css_selector('#co_id')
code.send_keys(ticker)
time.sleep(3)
#click
browser.find_element_by_css_selector('#search_bar1 > div > input[type=button]').click()
time.sleep(3)
#點擊詳細資料
browser.find_element_by_css_selector('#t108sb22_fm1 > table > tbody > tr.even > td:nth-child(5) > input[type=button]').click()
#%%
#轉換頁面
all_handles = browser.window_handles
now_handle=browser.current_window_handle
#print(now_handle)
time.sleep(2)
#彈出兩個介面,跳轉到不是主窗體介面
for handle in all_handles:
    if handle!=now_handle:   
       browser.switch_to_window(handle)
       html=browser.find_element_by_css_selector('#table01 > center > table > tbody')
       df=html.text
       #print(df)
#str to list
dfs=df.split()
#%%
#寫入csv檔
with open('2330data.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(dfs)
    print('已完成')