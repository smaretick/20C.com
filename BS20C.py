# -*- coding: utf-8 -*-
#start BrowserStackLocal ./BrowserStackLocal --key MDKicy4nya2192zewKpz
#scottmaretick51@gmail.com Sm110751$
#sudo pip2 install pyobjc
#pip2 install pyobjc-core
#sudo pip2 install pyobjc-framework-Quartz
#pip2 install pyautogui
#sudo pip install rubicon-objc
#'browserstack.debug': 'true'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import unittest, time, re

desired_cap = {'browser': 'Chrome','browser_version': '80.0','os': 'OS X','os_version': 'High Sierra','project': '20C.com','browserstack.debug': 'true', 'resolution': '1600x1200'}

#desired_cap = {'browser': 'Firefox','browser_version': '62.0 beta','os': 'OS X','os_version': 'High #Sierra','project': #'20C.com','browserstack.debug': 'true'}

browser = webdriver.Remote(
    command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub',
    desired_capabilities= desired_cap)


#runs with either Firefox or Chrome
#CHROME
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size= 1360 x 1400')
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver"),chrome_options=options;)
#browser = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
print(browser.get_window_size())
browser.set_window_size(1360, 1400)
print(browser.get_window_size())
#browser = webdriver.Firefox()  
#browser.maximize_window()
browser.get("https://20c.com/")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1a.png');

#PAGING DOWN MAIN PAGE START
browser.execute_script("window.scrollTo(0,300);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1b.png');
browser.execute_script("window.scrollTo(300,600);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1c.png');
browser.execute_script("window.scrollTo(600,900);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1d.png');
browser.execute_script("window.scrollTo(900,1200);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1e.png');
browser.execute_script("window.scrollTo(1200,1500);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1f.png');
browser.execute_script("window.scrollTo(1500,1800);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1g.png');
browser.execute_script("window.scrollTo(1800,2100);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1h.png');
browser.execute_script("window.scrollTo(2100,2500);") #BO†TOM OF PAGE
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot1i.png');	
#PAGING DOWN MAIN PAGE END

print browser.title
#browser.window_handles
#browser.switch_to.active_element
#browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/nav/div/ul/li[1]/a").click() #PROJECTS 
#https://20c.com/projects
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2a.png');
#PAGING DOWN PROJECTS PAGE START
browser.execute_script("window.scrollTo(0,300);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2b.png');
browser.execute_script("window.scrollTo(300,600);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2c.png');
browser.execute_script("window.scrollTo(600,900);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2d.png');
browser.execute_script("window.scrollTo(900,1200);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2e.png');
browser.execute_script("window.scrollTo(1200,1500);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2f.png');
browser.execute_script("window.scrollTo(1500,1800);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2g.png');
browser.execute_script("window.scrollTo(1800,2100);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2h.png');
browser.execute_script("window.scrollTo(2100,2500);") #BO†TOM OF PAGE
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot2i.png');	
#PAGING DOWN PROJECTS PAGE END

browser.find_element_by_xpath("/html/body/div[1]/div/a").click() #GOT IT
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot3.png');

browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/nav/div/ul/li[2]/a").click() #CASE STUDY
#https://20c.com/case-study/tc
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4a.png');
#PAGING DOWN CASE STUDY PAGE START
browser.execute_script("window.scrollTo(0,300);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4b.png');
browser.execute_script("window.scrollTo(300,600);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4c.png');
browser.execute_script("window.scrollTo(600,900);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4d.png');
browser.execute_script("window.scrollTo(900,1200);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4e.png');
browser.execute_script("window.scrollTo(1200,1500);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4f.png');
browser.execute_script("window.scrollTo(1500,1800);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot¢g.png');
browser.execute_script("window.scrollTo(1800,2100);")
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4h.png');
browser.execute_script("window.scrollTo(2100,2500);") #BO†TOM OF PAGE
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot4i.png');	
#PAGING DOWN CASE STUDY PAGE END

browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[3]/div[3]/div/p/a").click() #SEE KEY SCREENSHOTS
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot5.png');

browser.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[6]/div[2]/div/a").click()#GET IN TOUCH
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot6.png');

browser.find_element_by_xpath("/html/body/div[2]/div/div[4]/div[2]/div[4]/a").click() #CONTACT US
time.sleep(10)
print browser.title
browser.save_screenshot('/Users/scottmaretick/Desktop/SCREENSHOTS/ScreenShot7.png');
browser.quit()
