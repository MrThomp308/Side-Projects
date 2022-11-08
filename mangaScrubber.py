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

filePath = 'D:/ChainSawMan/RAW'

driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
options.add_argument("--start-maximized")
options.add_argument("--web-security=false")
options.add_argument("--incognito")
#options.add_extension("C:\\Users\\Michael\\ChromeDriver\\Extensions\\metamask.crx")
driver = webdriver.Chrome(executable_path=driverPath,options=options)

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


def main():
    print('MAIN')

    siteURL = 'https://www.chainsaw-man-manga.online/manga/chainsaw-man-chapter-'
    chapterStart = 108
    chapterEnd = 109

    for i in range(chapterStart, chapterEnd):
        newURL = siteURL + str(i)
        OpenSite(newURL)

        imageDivs = GetElementsBy(By.TAG_NAME, 'IMG', 'className', 'article_ed__img')
        imageURLS = []
        for imageDiv in imageDivs:
            imageURL = imageDiv.get_attribute('src')
            imageURLS.append(imageURL)
        
        j = 1
        for imgURL in imageURLS:
            OpenSite(imgURL,1)
            fileName = str(i) + '_' + str(j) + '.jpg'

            urllib.request.urlretrieve(imgURL, str(filePath + '/' + fileName))
            
            j = j + 1

main()