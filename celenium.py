
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome('./chrome/chromedriver.exe')


# In[2]:


driver.implicitly_wait(3)


# In[3]:


driver.get('http://www.taxnet.co.kr/member/login.asp')


# In[4]:


elem = driver.find_element_by_name('userid').send_keys('qkrtmsk0930')
elem = driver.find_element_by_name('pwd')
elem.send_keys('qkrtmsk0930')
elem.submit()


# In[5]:


driver.get('http://www.taxnet.co.kr/tax/josebub/generalLaw/general_List.asp?mflag=1&naviNum=1&pageNum=1')


# In[6]:


driver.execute_script("PopupGo('023500LW.010');")


# In[7]:


driver.switch_to_window(driver.window_handles[1])


# In[8]:


k = 2018253669


# In[10]:


for i in range (0, 220):
    try :
        driver.execute_script("PageGoView('023500LW.010','"+str(k+i)+"',0);")
    except WebDriverException :
        print('aa')

    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find("div", {"id" : "DivPrintArea"})
    # a.findAll("div",{"class": "clsLP1"})#
    try :
        print(a.text)
    except AttributeError :
        i = i-1

