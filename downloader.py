import time
from selenium import webdriver
import os
import shutil


pdf_save_folder = 'C:\\Users\\naoki\\PythonWorkSpace\\save'
tmp_folder      = 'C:\\Users\\naoki\\PythonWorkSpace\\tmp'

driver = webdriver.Chrome()

# driver.get('https://passnavi.evidus.com/search_univ/index.html?thema=myModal&name=&founder_flg=1&women_flg=&prefecture_id=8%2C9%2C10%2C11%2C12%2C13%2C14&fac_group_id=10&sub_group_id=29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C43%2C37%2C38%2C39%2C42%2C71%2C72%2C73&dif_deviation_low=&dif_deviation_hig=&order=name_asc%2Cprefecture_asc&search_mode=1')
# time.sleep(5)
driver.get('C:\\Users\\naoki\\PythonWorkSpace\\test.html')

# get univ list
univ_lst = {}
res_univ_lst = driver.find_elements_by_class_name('result-box')
for u in res_univ_lst:
    try:
        elm = u.find_element_by_class_name('name-area')
        elm = elm.find_element_by_tag_name('a')
        url = elm.get_attribute('href')
        univ_lst.update({elm.text: url})
    except:
        pass

# create pdf folder
if not os.path.isdir(pdf_save_folder):
    os.mkdir(pdf_save_folder)

# create tmp folder
os.mkdir(tmp_folder)

# create folder if not exist
os.chdir(pdf_save_folder)
exist_past_quest_lst = os.listdir(pdf_save_folder)
for univ in univ_lst:
    if not univ in exist_past_quest_lst:
        os.mkdir(univ)
        save_dest = os.getcwd()


# del tmp folder
shutil.rmtree(tmp_folder)

driver.quit()
