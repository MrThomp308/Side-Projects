from pydoc import classname
from re import S
from tkinter.filedialog import Open
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import urllib.request
import time
import os
import random
import subprocess
import undetected_chromedriver.v2 as uc

filePath = 'D:/ChainSawMan/RAW'

driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
options.add_argument("--start-maximized")
options.add_argument("--web-security=false")
options.add_argument("--incognito")
options.add_argument("--allow-running-insecure-content")
#options.add_extension("C:\\Users\\Michael\\ChromeDriver\\Extensions\\metamask.crx")
driver = webdriver.Chrome(executable_path=driverPath,options=options)

#driver = uc.Chrome()

def OpenSite(url, secs = 5):
    driver.get(url)
    print('OPEN ' + str(url))
    time.sleep(secs)

def GetElementBy(outerID, outerIDValue, innerID, innerIDValue):
    print('GETTING ELEMENT')
    elems = driver.find_elements(outerID,outerIDValue)
    for elem in elems:
        if(elem.get_attribute(innerID) == innerIDValue):
            print(elem.get_attribute(innerID))
            return elem

def GetElementsBy(outerID, outerIDValue, innerID, innerIDValue):
    print('GETTING ELEMENTS')
    returnedElements = []

    elems = driver.find_elements(outerID,outerIDValue)
    for elem in elems:
        if(elem.get_attribute(innerID) == innerIDValue):
            returnedElements.append(elem)

    return returnedElements

def SignIn():
    siteURL = 'https://onlyfans.com/'
    OpenSite(siteURL)

    signInElem = GetElementBy(By.TAG_NAME, 'A', 'class', 'g-btn m-rounded m-twitter m-md m-block m-icon-absolute m-mb-16')
    signInElem.click()

    signInElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'username_or_email')
    signInElem.send_keys('mrthomp5')

    signInElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'password')
    signInElem.send_keys('December1965')

    signInElem = GetElementBy(By.TAG_NAME, 'INPUT', 'type', 'submit')
    signInElem.click()

    print('END SIGN IN')

def ScrollForSeconds(seconds = 5):
    for i in range(seconds):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

def FindActive():
    siteURL = 'https://onlyfans.com/my/subscriptions/active?order_field=expire_date'
    OpenSite(siteURL)
    
    ScrollForSeconds(10)

    userNames = GetElementsBy(By.TAG_NAME, 'DIV', 'className', 'g-user-username')

    userNameList = []
    for userName in userNames:
        userNameList.append(userName.get_attribute('textContent').split('@')[1])

    print('END FIND ACTIVE')
    return userNameList

def ScrubMedia(userName):
    userName = str(userName).strip()
    siteURL = 'https://onlyfans.com/' + str(userName) + '/media'
    OpenSite(siteURL)
    ScrollForSeconds(60)

    mediaSquares = GetElementsBy(By.TAG_NAME, 'A', 'className', 'b-photos__item m-square')
   # mediaSquares.append(GetElementsBy(By.TAG_NAME, 'A', 'className', 'b-photos__item m-square m-video-item'))
    squareSites = []
    for mediaSquare in mediaSquares:
        squareSite = mediaSquare.get_attribute('href')
        if(squareSite not in squareSites):
            squareSites.append(squareSite)

    for squareSite in squareSites:
        OpenSite(squareSite)
        print('OPEN SQUARE SITE')
        
        imageElem = GetElementBy(By.TAG_NAME, 'IMG', 'className', 'img-responsive m-object-contain')
        try:
            imageURL = imageElem.get_attribute('currentSrc')
            urllib.request.urlretrieve(imageURL, str('D:/Scans' + '/' + userName + '_' + str(squareSite).split('/')[-2] + '.jpg'))
            print('SAVE IMAGE')
        except:
            try:
                imageElems = GetElementsBy(By.TAG_NAME, 'IMG', 'className', 'm-object-contain')

                i = 1
                for iE in imageElems:
                    imageURL = iE.get_attribute('currentSrc')
                    urllib.request.urlretrieve(imageURL, str('D:/Scans' + '/' + userName + '_' + str(squareSite).split('/')[-2] + '_' + str(i) + '.jpg'))
                    i = i + 1
            except Exception as e:
                print(str(e))

        print('GET IMAGE')

        

    print('END SCRUB MEDIA')

def main():
    print('MAIN')

    SignIn()
    userNames = FindActive()
    
    for userName in userNames[10:]:
        ScrubMedia(userName)
    

    print('END')


   

main()