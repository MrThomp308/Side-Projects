from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

keyString = ''
purchasedTokens = {}

metaMaskDriver = None
pancakeSwapDriver = None
coinMarketCapDriver = None

def WindowNames(driver):
    return driver.window_handles

def ConnectMetaMaskWallet(createDriverWithProfile = True):
    success = False
    while(success == False):
        try:
            driver = CreateDriver(createDriverWithProfile)
            DriverGet(driver,"chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")

            classes = driver.find_elements(By.ID, 'app-content')

            inputs = []
            for div in classes:
                inputs.append(div.find_element(By.TAG_NAME, 'input'))
            
            for input in inputs:
                if(input.aria_role == 'textbox'):
                    input.send_keys('')

            inputs = []
            for div in classes:
                inputs.append(div.find_element(By.TAG_NAME, 'button'))

            for input in inputs:
                if(input.text == 'Unlock'):
                    input.click()
            
            print('\n\n\nMETAMASK CONNECTED!\n\n\n')
            success == True
        except:
            driver.close()
            success = False
        
    return driver

def ConnectPancakeSwap():
    driver = CreateDriver()
    DriverGet(driver,"https://pancakeswap.finance/swap")

    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        try:
            if(button.find_element(By.TAG_NAME, 'div').text == 'Connect Wallet'):
                print('Found!')
                button.click()
                break
        except:{}

    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        try:
            if(button.find_element(By.TAG_NAME, 'div').text == 'Metamask'):
                print('Found!')
                button.click()
                break
        except:{}
    print("PancakeSwap Connected!")
    return driver

#def OpenNewTab(url):
#    driver.execute_script("window.open('');")
#    tabLength = len(driver.window_handles)
#    driver.switch_to.window(driver.window_handles[tabLength - 1])
#    driver.get(url)

#def SwitchToTab(tabIndex):
#    driver.switch_to.window(driver.window_handles[tabIndex])
#    driver.refresh()

def CreateMetaMaskWallet():
    driver = CreateDriver()
    driver.get("https://www.google.com")
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
    tabs = list(WindowNames(driver))
    driver.switch_to.window(tabs[0])
    driver.close()
    driver.switch_to.window(tabs[1])
    
    #GETTING STARTED
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    #IMPORT WALLET
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        if(button.text == 'Import wallet'):
            button.click()
            break

    #AGREE TO TERMS
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        if(button.text == 'I Agree'):
            button.click()
            break

    #ENTER KEYS
    classes = driver.find_elements(By.CLASS_NAME, 'import-srp__srp-word')

    inputs = []
    for div in classes:
        inputs.append(div.find_element(By.TAG_NAME, 'input'))
    
    keys = keyString.split(' ')
    i = 0
    for input in inputs:
        input.click()
        input.send_keys(keys[i])
        i = i + 1

    classes = driver.find_elements(By.CLASS_NAME, 'create-new-vault__create-password')

    inputs = []
    for div in classes:
        inputs.append(div.find_elements(By.TAG_NAME, 'input'))

    for input in inputs[0]:
        input.send_keys('')

    checkClass = driver.find_element(By.CLASS_NAME, 'create-new-vault__terms')
    input = checkClass.find_element(By.TAG_NAME, 'input')
    input.click()

    submit = driver.find_element(By.TAG_NAME, 'button')
    submit.click()

def getCarat(carat):
    if('down' in str(carat)):
        return '-'
    else:
        return '+'

def refreshSymDict():
    print('\nREFRESHING SYMBOL DICTIONARY')

    driver = coinMarketCapDriver
    driver.refresh()
    #Switch To CoinMarketCap
    #SwitchToTab(1)

    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button/b[text()='No, thanks']"))).click()
    
    symbols =  [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td/a//p[@color='text']")))]
    network =  [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[9]")))]
    addedAgo = [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[10]")))]
    
    perf1 =    [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[5]")))]
    perf24 =   [my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[6]")))]
    perf1_carat =    [my_elem.get_attribute('class') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[5]//span//span")))]
    perf24_carat =   [my_elem.get_attribute('class') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[6]//span//span")))]
    
    href =     [my_elem.get_attribute('href') for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[contains(@class, 'cmc-table')]//tbody//tr//td[3]//a")))]

    symbolDict = {}
    i = 0
    for sym in symbols:
        if((getCarat(perf1_carat[i]) == '+') and (getCarat(perf24_carat[i]) == '+')):
            symbolDict.update({sym: {   'Network': network[i], 
                                        'Added Ago': addedAgo[i],
                                        'Perf 1': str(getCarat(perf1_carat[i]) + perf1[i]),
                                        'Perf 24': str(getCarat(perf24_carat[i]) + perf24[i]),
                                        'HREF': href[i]}})
        i = i + 1
    return symbolDict

def findEligibleTokens(symbolDict, eligibleAgo=30, eligibleValue='minutes'):
    driver = CreateDriver()
    print('FINDING ELIGIBLE TOKENS')
    if(len(symbolDict) < 1):
        print('Symbol Dictionary Empty! :(')
        return {}

    newSymbolDict = {}
    for sym in symbolDict:
        #symbolDict.get(sym).get('Added Ago') == str(str(hoursAgo) + ' hours ago') or 
        howManyAgo = int(str(symbolDict.get(sym).get('Added Ago')).split(' ')[0])
        if(str(eligibleValue) in symbolDict.get(sym).get('Added Ago')):
            if(howManyAgo <= eligibleAgo):
                if(symbolDict.get(sym).get('Network') == 'BNB'):
                    print(str(sym) + ': POTENTIAL')
                    newSymbolDict.update({sym: symbolDict.get(sym)})
            
        if(howManyAgo <= 24 and 'hours' in symbolDict.get(sym).get('Added Ago')):
            if(symbolDict.get(sym).get('Network') == 'BNB'):
                perf1 = str(symbolDict.get(sym).get('Perf 1'))[1:-1]
                perf24 = str(symbolDict.get(sym).get('Perf 24'))[1:-1]
                if(float(perf1) >= 10.0) or (float(perf24) >= 10.0):
                    print('MISSED THE BOAT. TRY LATER.')
                    return {}

        if(sym in purchasedTokens.keys()):
            newSymbolDict.update({sym: symbolDict.get(sym)})

    for sym in newSymbolDict:
        address = ''
        if(sym not in purchasedTokens):
            driver.get(str(newSymbolDict.get(sym).get('HREF')))

            addresses =  driver.find_elements(By.TAG_NAME,'a')
            for addres in addresses:
                adres = addres.get_attribute('href')
                if(adres is not None):
                    if('https://bscscan.com/token/' in adres):
                        address = str(adres).replace('https://bscscan.com/token/', '')
        else:
            address = purchasedTokens.get(sym).get('Address')

        isHoneyPot = detectHoneyPot(address)

        if(isHoneyPot == False):
            #Check to see if token is on PancakeSwap
            onPS = False

            #SwitchToTab(0)
            divs = driver.find_elements(By.ID,'swap-currency-output')
            for div in divs:
                button = div.find_element(By.TAG_NAME,'button')
                button.click()

            input = driver.find_element(By.ID,'token-search-input')
            input.send_keys(address)

            time.sleep(2)
            buttons = driver.find_elements(By.TAG_NAME,'button')
            for button in buttons:
                try:
                    if(button.text == 'Import'):
                        button.click()
                        break
                except Exception as e: {print(str(e))}

            time.sleep(2)
            inputs = driver.find_elements(By.TAG_NAME,'input')
            for input in inputs:
                if(input.aria_role == 'checkbox'):
                    try:
                        input.click()
                    except: {}

            time.sleep(2)
            buttons = driver.find_elements(By.TAG_NAME,'button')
            for button in buttons:
                try:
                    if(button.text == 'Import'):
                        button.click()
                        onPS = True
                        break
                except Exception as e: {print(str(e))}

            if(onPS):
                try:   
                    tempDict = symbolDict.get(sym)
                    tempDict.update({'Address': address})

                    symbolDict.update({sym: tempDict})
                    newSymbolDict.update({sym: symbolDict.get(sym)})

                    print(str(sym) + ': ELIGIBLE')
                except Exception as e: {}
            else:
                print(str(sym) + ' Not On PancakeSwap')

    if(len(newSymbolDict) < 1):
        print('New Symbol Dictionary Empty!')
    return newSymbolDict

def detectHoneyPot(address='0xed74bc5dc139356e08de28143996f5ef6e4334a4'):
    driver = CreateDriver()
    print('DETECTING HONEYPOT: ' + address)
    url = str('https://honeypot.is/?address=' + address)
    DriverGet(driver, url)
    status = [my_elem for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class, 'success')]")))]
    
    driver.close()

    if(len(status) > 0):
        print('NOT A HONEYPOT')
        return False
    else:
        print('POTENTIAL HONEYPOT')
        return True

def AttemptCoinPurchase(coinDict):
    driver = pancakeSwapDriver
    for coin, info in coinDict.items():
        print(str(coin) + ': ATTEMPTING COIN PURCHASE')

        #SwitchToTab(0)
        totalBNB = 0.0

        divs = driver.find_elements(By.ID,'swap-currency-input')
        for div in divs:
            moreDivs = div.find_elements(By.TAG_NAME,'div')
            for mDiv in moreDivs:
                if('Balance:' in str(mDiv)):
                    totalBNB = float(str(mDiv).split(': ')[1])
        if(totalBNB > 0.0):
            inputs = driver.find_elements(By.TAG_NAME, 'input')
            for input in inputs:
                title = input.get_attribute("title")
                if('Token Amount' in str(title)):
                    input.send_keys(totalBNB / 2.0)

            time.sleep(2)
            button = driver.find_element(By.ID,'swap-button')
            button.click()

def CreateDriver(withUserData = False):
    driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-web-security")
    options.add_argument("--start-maximized")
    options.add_argument("--web-security=false")

    if(withUserData):
        options.add_argument("--user-data-dir=C:\\Users\\Michael\\ChromeDriver\\User Data")
        options.add_argument("--profile-directory=Profile 1")

    #options.add_extension("C:\\Users\\Michael\\ChromeDriver\\Extensions\\metamask.crx")
    driver = webdriver.Chrome(executable_path=driverPath,options=options)
    return driver

def ConnectCoinMarketCap():
    driver = CreateDriver()
    driver.get("https://coinmarketcap.com/new/")
    return driver

def DriverGet(driverObj, url, waitTime = 5):
    driverObj.get(url)
    time.sleep(waitTime)

metaMaskDriver = ConnectMetaMaskWallet()
pancakeSwapDriver = ConnectPancakeSwap()
coinMarketCapDriver = ConnectCoinMarketCap()

eligibleTokenDict = {}
while(len(eligibleTokenDict) < 1):
    eligibleTokenDict = {}
    eligibleTokenDict = findEligibleTokens(refreshSymDict(),1,'hours')
    AttemptCoinPurchase(eligibleTokenDict)

    time.sleep(1 * 60)

#Figure out how to determine which coin to get if two coins appear within the same hour. (Preferably get the first one.)
#It might be beneficial to sort the entire dictionary by descending time

print('')