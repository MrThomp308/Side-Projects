from re import S
from tkinter.filedialog import Open
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import random

driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
options.add_argument("--start-maximized")
options.add_argument("--web-security=false")
options.add_argument("--user-data-dir=C:\\Users\\Michael\\ChromeDriver\\User Data")
options.add_argument("--profile-directory=Profile 1")
#options.add_extension("C:\\Users\\Michael\\ChromeDriver\\Extensions\\metamask.crx")
driver = webdriver.Chrome(executable_path=driverPath,options=options)

def ConnectPrintify():
    driver.get("https://www.printify.com/app/store/products/1")
    print('Printified')

def UploadTeeshirtDirect(path):
    driver.get("https://printify.com/app/editor/12/29")
    time.sleep(5)

    myDeviceButtons = driver.find_elements(By.TAG_NAME, 'editor-perspectives')
    myDeviceButtons = driver.find_elements(By.TAG_NAME, 'input')

    myDeviceButtons[0].send_keys(path)

    time.sleep(10)
    myColorDropDown = driver.find_element(By.TAG_NAME,'DROP-DOWN')
    myColorDropDown.click()

    myColorButtons = myColorDropDown.find_elements(By.TAG_NAME,'BUTTON')

    acceptedColors = '0,1,2,3,7,24,30,31,32'.split(',')
    for color in acceptedColors:
        myColorButtons[int(color)].click()

    buttons = driver.find_elements(By.TAG_NAME,'BUTTON')
    for button in buttons:
        if('Save product' in button.text):
            button.click()
            break
    
    time.sleep(5)

    print('Uploaded')

def UploadSweatshirtDirect(path):
    driver.get("https://printify.com/app/editor/49/3")
    time.sleep(5)

    myDeviceButtons = driver.find_elements(By.TAG_NAME, 'editor-perspectives')
    myDeviceButtons = driver.find_elements(By.TAG_NAME, 'input')

    myDeviceButtons[0].send_keys(path)

    time.sleep(10)
    myColorDropDown = driver.find_element(By.TAG_NAME,'DROP-DOWN')
    myColorDropDown.click()

    myColorButtons = myColorDropDown.find_elements(By.TAG_NAME,'BUTTON')

    acceptedColors = '0,1,2,3,6,7,11,19,20'.split(',')
    for color in acceptedColors:
        myColorButtons[int(color)].click()

    buttons = driver.find_elements(By.TAG_NAME,'BUTTON')
    for button in buttons:
        if('Save product' in button.text):
            button.click()
            break
    
    time.sleep(5)

    print('Uploaded')

def ReadyForPublish():
    unpublishedLeft = True

    driver.get('https://printify.com/app/store/products/1')
    time.sleep(5)

    dropdownSelect = driver.find_elements(By.TAG_NAME,'PFY-DROPDOWN-SELECT')
    for ddS in dropdownSelect:
        inputs = ddS.find_elements(By.TAG_NAME,'input')
        for input in inputs:
            if(input.get_attribute('id') == 'status'):
                input.click()

    selectByOptions = driver.find_elements(By.TAG_NAME,'PFY-DROPDOWN-OPTION')
    for selectOption in selectByOptions:
        print(selectOption.get_attribute('innerText'))
        if(selectOption.get_attribute('innerText').strip() == 'Unpublished'):
            selectOption.click()
            time.sleep(3)
            break

    listItems = driver.find_elements(By.TAG_NAME,'PFA-PRODUCTS-LIST-ITEM')
    llLength = len(listItems)
    while llLength > 0:
        item = listItems[0]
        status = item.find_element(By.TAG_NAME,'SMALL').text
        print(status)

        if(status == 'Unpublished'):
            item.find_element(By.TAG_NAME,'PFY-LINK').click()
            print('CLICKED')
            time.sleep(5)

            mockupClasses = driver.find_elements(By.CLASS_NAME,'active-cameras')
            colorMockups = mockupClasses[1].find_elements(By.TAG_NAME,'PFA-MOCKUP')
            selection = random.randint(0,len(colorMockups)-1)
            driver.execute_script("arguments[0].click()",colorMockups[selection].find_element(By.CLASS_NAME,'radio-radio'))
            #colorMockups[selection].click()
            time.sleep(2)

            goodMockups = []
            mockups = mockupClasses[0].find_elements(By.TAG_NAME,'PFA-MOCKUP')
            for mockup in mockups:
                if(mockup.text == 'Person 1' or mockup.text == 'Person 3'):
                    goodMockups.append(mockup)
            selection = random.randint(0,len(goodMockups)-1)
            goodMockups[selection].click()
            time.sleep(5)

            productTitle = driver.find_element(By.CLASS_NAME,'input-product-title').find_element(By.TAG_NAME,'input')
            productTitle.send_keys(' - Spooky Season Shirts for Men and Women - Halloween, Cute Shirts, Queer Small Business Shirt')

            productDesc = driver.find_element(By.TAG_NAME,'PFA-PRODUCT-DESCRIPTION-EDITOR').find_element(By.TAG_NAME,'TEXTAREA')
            productDesc.send_keys('\n\nHalloween, Fall, Spooky Season, Unisex, Men, Women, Queer Business')
            
            driver.find_element(By.CLASS_NAME,'publish-btn-tooltip').find_element(By.TAG_NAME,'button').click()
            print('MOVING ON')
            time.sleep(5)

            dropdownSelect = driver.find_elements(By.TAG_NAME,'PFY-DROPDOWN-SELECT')
            for ddS in dropdownSelect:
                inputs = ddS.find_elements(By.TAG_NAME,'input')
                for input in inputs:
                    if(input.get_attribute('id') == 'status'):
                        input.click()

            selectByOptions = driver.find_elements(By.TAG_NAME,'PFY-DROPDOWN-OPTION')
            for selectOption in selectByOptions:
                print(selectOption.get_attribute('innerText'))
                if(selectOption.get_attribute('innerText').strip() == 'Unpublished'):
                    selectOption.click()
                    time.sleep(3)
                    break

            listItems = driver.find_elements(By.TAG_NAME,'PFA-PRODUCTS-LIST-ITEM')
            llLength = len(listItems)
    print('READY FOR PUBLISHING')

ConnectPrintify()

canvaPath = 'C:\\Users\\Michael\\Downloads\\Canva Designs\\Upload Queue'
finishedPath = 'C:\\Users\\Michael\\Downloads\\Canva Designs\\Upload Finished'
pathItems = os.listdir(canvaPath)

for item in pathItems:
    if('.png' in item):
        completePath = canvaPath + '\\' + item
        UploadSweatshirtDirect(completePath)
        UploadTeeshirtDirect(completePath)
        completeFinishedPath = finishedPath + '\\' + item
        os.replace(completePath, completeFinishedPath)

ReadyForPublish()
print('END')