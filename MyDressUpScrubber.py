from audioop import add
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

import time
import json
import urllib.request
from PIL import Image
from os import listdir
from os.path import isfile, join
import os

#Global Crap
driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'

#filePath = 'C:/MyDressUpDarling/RAW/'
filePath = 'C:/HowHeavyAreTheDumbBellsYouLife/RAW'
#mangaURL = "https://dressupdarling.online/manga/my-dress-up-darling-chapter-"
mangaURL = "https://r.mangaowls.com/reader/61116/984213?tr=VKy9Ub4bRvF%2BHTgj7xJujQ%3D%3D&s=aHR0cHM6Ly9tYW5nYW93bC5uZXQ%3D"

def saveAsPDF():
    print('SAVING AS PDF')

    onlyfiles = [f for f in listdir(filePath) if isfile(join(filePath, f))]
    print(onlyfiles)

    #RENAME
    #for fN in onlyfiles:
    #    nfN = str(fN).replace('00', '0')
    #    nfN = fN
    #    nfN = str(fN).replace('-','')
    #    nfN = str(nfN).replace('.jpg','')
    #    nfN = str(nfN).replace('.png','')
    #    nfNL = str(nfN).split('_')
    #    for i in range(0, len(nfNL)):
    #        if(len(nfNL[i]) > 2):
    #            nfNL[i] = str(nfNL[i])[1:]
    #    nfN = str('-' + str(nfNL[0]) + '_' + str(nfNL[1]) + '.jpg')
    #    os.rename(str(filePath + fN), str(filePath + nfN))

    #imageList = []
    #imP = None
    #i = 0
    #for fN in onlyfiles:
    #    imR = Image.open(str(filePath + fN))
    #    imC = imR.convert('RGB')
    #    imageList.append(imC)
    #    
    #    if(i == 0):
    #        imP = imC
    #    i = i + 1
    #print(imageList)
    #imP.save(str(filePath + 'MyDressUpDarlingComplete.pdf'), save_all=True, append_images=imageList)

def myDressUpProcess():
    for i in range(30,75):
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.minimize_window()

        #MY DRESS UP DARLING
        driver.get(mangaURL+str(i)+"/")
        #imageList =  [my_elem.get_attribute('src') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'separator')]//a//img")))]
        imageList = driver.find_elements_by_tag_name('img')
        imageList = [my_elem.get_attribute('src') for my_elem in imageList]
        for imageUrl in imageList:
            if('Chapter' not in imageUrl):
                continue

            driver.get(imageUrl)
            imageUrlStr = str(imageUrl).replace('/','_')
            imageUrlStr = str(imageUrlStr).replace(':','_')
            #imageUrlStr = str(imageUrlStr).replace('jpg','png')
            #imageUrlStr = str(imageUrlStr).replace('jpeg','png')
            imageUrlStr = str(imageUrlStr).split('Chapter')[-1]
            fileName = str(imageUrlStr)

            #driver.save_screenshot('C:/MyDressUpDarling/RAW/' + str(imageUrlStr))
            urllib.request.urlretrieve(imageUrl, str(filePath + fileName))

        #HOW HEAVE ARE THE DUMBBELLS YOU LIFT
        driver.close()
        print('Page: ' + str(i))

def shikimoriProcess():
    filePath = 'C:/ShikimorisNotJustACutie/RAW'
    mangaURL = 'https://shikimorisnotjustacutie.online/'
    chapterDictionary = {}

    #driver = webdriver.Chrome(executable_path=driverPath)
    driver = Chrome(use_subprocess=True)
    driver.minimize_window()

    driver.get(mangaURL+"/")
    liList = driver.find_elements(by=By.TAG_NAME, value='li')
    for li in liList:
         aList = li.find_elements(by=By.TAG_NAME, value='a')
         for aElem in aList:
            aText = aElem.text
            if('Chapter' not in aText):
                continue
            aURL = aElem.get_attribute('href')
            chapterNum = str(float(str(str(aText).split('Chapter ')[1].split(' –')[0]))).rjust(6,'0')
            chapterDictionary.update({chapterNum:aURL})
    
    chapterNumList = list(chapterDictionary.keys())
    chapterNumList.sort()
    for chapterNum in chapterNumList:
        cN = float(str(chapterNum).lstrip('0'))
        if(cN <= 115):
            continue

        print(chapterNum)
        driver.get(chapterDictionary.get(chapterNum))
        
        properAListFound = False
        aList = driver.find_elements(by=By.TAG_NAME, value='a')

        i = 0
        for aElem in aList:
            aHREF = aElem.get_attribute('href')
            if('CHAPTER' not in aHREF.upper()):
                continue
            if('.JPG' not in aHREF.upper()):
                continue

            print(aHREF)
            fileName = str(chapterNum) + '_' + str(i + 1).rjust(3,'0') + '.jpg'
            urllib.request.urlretrieve(aHREF, str(filePath + '/' + fileName))
            properAListFound = True
            i = i + 1

        if(properAListFound == False):
            imgList = driver.find_elements(by=By.TAG_NAME, value='img')
            i = 0
            for aElem in imgList:
                aHREF = aElem.get_attribute('src')
                if('CHAPTER' not in aHREF.upper()):
                    continue
                if('.JPG' not in aHREF.upper()):
                    continue

                print(aHREF)
                fileName = str(chapterNum) + '_' + str(i + 1).rjust(3,'0') + '.jpg'
                try:
                    urllib.request.urlretrieve(aHREF, str(filePath + '/' + fileName))
                except Exception as e:
                    print(str(e))
                    
                properAListFound = True
                i = i + 1

    driver.close()

def dumbbellProcess():
    chapterDictionary = {}

    #driver = webdriver.Chrome(executable_path=driverPath)
    driver = Chrome(use_subprocess=True)
    driver.minimize_window()

    driver.get(mangaURL+"/")
    selectList = driver.find_elements(by=By.TAG_NAME, value='select')

    for select in selectList:
        selectID = select.get_attribute('id')
        if(selectID != 'selectChapter'):
            continue

        chapterList = select.find_elements(by=By.TAG_NAME, value='option')
        #title, url
        for chapter in chapterList:
            chapterTitle = chapter.get_attribute('title')
            chapterURL = chapter.get_attribute('url')
            chapterNum = str(float(str(chapterTitle).split('Chapter ')[1].split(' :')[0])).rjust(6, '0')
            chapterDictionary.update({str(chapterNum):str(chapterURL)})

        chapterNumList = list(chapterDictionary.keys())
        chapterNumList.sort()
        for chapterNum in chapterNumList:
            cN = float(chapterNum.lstrip('0'))
            if(cN <= 144):
                continue
            chapterURL = str(mangaURL.split('/reader')[0]) + str(chapterDictionary.get(chapterNum))
            print(chapterURL)

            driver.get(chapterURL)
            imageList = driver.find_elements(by=By.TAG_NAME, value='img')

            imageSrcList = []
            for imageElem in imageList:
                className = imageElem.get_attribute('class')
                if(className != 'owl-lazy'):
                    continue
                
                imageUrl = imageElem.get_attribute('data-src')
                imageSrcList.append(imageUrl)
            
            i = 0
            for imageSrc in imageSrcList:
                driver.get(imageSrc)
                fileName = str(chapterNum) + '_' + str(i + 1).rjust(3,'0') + '.jpg'

                urllib.request.urlretrieve(imageSrc, str(filePath + '/' + fileName))
                i = i + 1


    driver.close()

def main():
    print('STARTING MAIN PROCESS')

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    shikimoriProcess()
    

main()