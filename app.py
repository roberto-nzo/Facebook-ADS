from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

# PATH = 'C:\Program Files (x86)\chromedriver.exe'
# driver = webdriver.Chrome(PATH)
# url = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=housing_ads&country=US&q=apparel&search_type=keyword_unordered&media_type=all'
# driver.get(url)
# sleep(30)
# for x in range(3):
#     driver.find_element_by_tag_name('body').send_keys(Keys.END)
#     sleep(7)

# with open('add.html', 'w', encoding='utf-8') as f:
#     f.write(str(driver.page_source))

with open('add.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

name_link_class = soup.find_all(class_='_8jgz _8jg_')
link_name_list = []

for x in name_link_class:
    dict_all = {}
    link = x.find('div', '_4ik4 _4ik5').text
    name_div = x.find('div', class_='_8jh2')
    name = name_div.find('div', class_='_4ik4 _4ik5').text
    dict_all['Company name'] = name
    dict_all['Website'] = link
    link_name_list.append(dict_all)
    temp_list = []
    for y in link_name_list:
        if y not in temp_list:
            temp_list.append(y)
    link_name_list = temp_list

    

add_df = pd.DataFrame(link_name_list)
add_df.to_csv('Facebook_Adds.csv', index=False)
print(add_df)
