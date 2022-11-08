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

import time
import os
import random
import subprocess

import GmailAPIConnect as GAPIC

driverPath = r'C:\Users\Michael\ChromeDriver\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
options.add_argument("--start-maximized")
options.add_argument("--web-security=false")
options.add_argument("--incognito")
#options.add_extension("C:\\Users\\Michael\\ChromeDriver\\Extensions\\metamask.crx")
driver = webdriver.Chrome(executable_path=driverPath,options=options)



def OpenSite(url, secs = 5, retryCount = 5):
    try:
        driver.get(url)
        print('OPEN ' + str(url))
        time.sleep(secs)
    except Exception as e:
        print(str(e))

        if(retryCount > 0):
            nRetryCount = retryCount - 1

            print('REBOOTING VPN')
            RebootVPN()

            print('RETRYING OPENSITE')
            OpenSite(url, retryCount=nRetryCount)

def OpenSiteNDriver(nDriver, url, secs = 5):
    nDriver.get(url)
    print('OPEN ' + str(url))
    time.sleep(secs)

def GetElementBy(outerID, outerIDValue, innerID, innerIDValue):
    print('GETTING ELEMENT')
    elems = driver.find_elements(outerID,outerIDValue)
    for elem in elems:
        if(elem.get_attribute(innerID) == innerIDValue):
            print(elem.get_attribute(innerID))
            return elem

def GetElementByNDriver(nDriver, outerID, outerIDValue, innerID, innerIDValue):
    print('GETTING ELEMENT')
    elems = nDriver.find_elements(outerID,outerIDValue)
    for elem in elems:
        if(elem.get_attribute(innerID) == innerIDValue):
            print(elem.get_attribute(innerID))
            return elem

def GenerateComment():
    print('GENERATE COMMENT')
    f = open('CommentFile.txt','r')
    commentList = f.readlines()
    comment = commentList[random.randint(0,len(commentList) - 1)]
    f.close()
    return comment

def GenerateName():
    print('GENERATE NAME')
    firstNames = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas', 'Henry', 'Theodore', 'Jack', 'Levi', 'Alexander', 'Jackson', 'Mateo', 'Daniel', 'Michael', 'Mason', 'Sebastian', 'Ethan', 'Logan', 'Owen', 'Samuel', 'Jacob', 'Asher', 'Aiden', 'John', 'Joseph', 'Wyatt', 'David', 'Leo', 'Luke', 'Julian', 'Hudson', 'Grayson', 'Matthew', 'Ezra', 'Gabriel', 'Carter', 'Isaac', 'Jayden', 'Luca', 'Anthony', 'Dylan', 'Lincoln', 'Thomas', 'Maverick', 'Elias', 'Josiah', 'Charles', 'Caleb', 'Christopher', 'Ezekiel', 'Miles', 'Jaxon', 'Isaiah', 'Andrew', 'Joshua', 'Nathan', 'Nolan', 'Adrian', 'Cameron', 'Santiago', 'Eli', 'Aaron', 'Ryan', 'Angel', 'Cooper', 'Waylon', 'Easton', 'Kai', 'Christian', 'Landon', 'Colton', 'Roman', 'Axel', 'Brooks', 'Jonathan', 'Robert', 'Jameson', 'Ian', 'Everett', 'Greyson', 'Wesley', 'Jeremiah', 'Hunter', 'Leonardo', 'Jordan', 'Jose', 'Bennett', 'Silas', 'Nicholas', 'Parker', 'Beau', 'Weston', 'Austin', 'Connor', 'Carson', 'Dominic', 'Xavier', 'Jaxson', 'Jace', 'Emmett', 'Adam', 'Declan', 'Rowan', 'Micah', 'Kayden', 'Gael', 'River', 'Ryder', 'Kingston', 'Damian', 'Sawyer', 'Luka', 'Evan', 'Vincent', 'Legend', 'Myles', 'Harrison', 'August', 'Bryson', 'Amir', 'Giovanni', 'Chase', 'Diego', 'Milo', 'Jasper', 'Walker', 'Jason', 'Brayden', 'Cole', 'Nathaniel', 'George', 'Lorenzo', 'Zion', 'Luis', 'Archer', 'Enzo', 'Jonah', 'Thiago', 'Theo', 'Ayden', 'Zachary', 'Calvin', 'Braxton', 'Ashton', 'Rhett', 'Atlas', 'Jude', 'Bentley', 'Carlos', 'Ryker', 'Adriel', 'Arthur', 'Ace', 'Tyler', 'Jayce', 'Max', 'Elliot', 'Graham', 'Kaiden', 'Maxwell', 'Juan', 'Dean', 'Matteo', 'Malachi', 'Ivan', 'Elliott', 'Jesus', 'Emiliano', 'Messiah', 'Gavin', 'Maddox', 'Camden', 'Hayden', 'Leon', 'Antonio', 'Justin', 'Tucker', 'Brandon', 'Kevin', 'Judah', 'Finn', 'King', 'Brody', 'Xander', 'Nicolas', 'Charlie', 'Arlo', 'Emmanuel', 'Barrett', 'Felix', 'Alex', 'Miguel', 'Abel', 'Alan', 'Beckett', 'Amari', 'Karter', 'Timothy', 'Abraham', 'Jesse', 'Zayden', 'Blake', 'Alejandro', 'Dawson', 'Tristan', 'Victor', 'Avery', 'Joel', 'Grant', 'Eric', 'Patrick', 'Peter', 'Richard', 'Edward', 'Andres', 'Emilio', 'Colt', 'Knox', 'Beckham', 'Adonis', 'Kyrie', 'Matias', 'Oscar', 'Lukas', 'Marcus', 'Hayes', 'Caden', 'Remington', 'Griffin', 'Nash', 'Israel', 'Steven', 'Holden', 'Rafael', 'Zane', 'Jeremy', 'Kash', 'Preston', 'Kyler', 'Jax', 'Jett', 'Kaleb', 'Riley', 'Simon', 'Phoenix', 'Javier', 'Bryce', 'Louis', 'Mark', 'Cash', 'Lennox', 'Paxton', 'Malakai', 'Paul', 'Kenneth', 'Nico', 'Kaden', 'Lane', 'Kairo', 'Maximus', 'Omar', 'Finley', 'Atticus', 'Crew', 'Brantley', 'Colin', 'Dallas', 'Walter', 'Brady', 'Callum', 'Ronan', 'Hendrix', 'Jorge', 'Tobias', 'Clayton', 'Emerson', 'Damien', 'Zayn', 'Malcolm', 'Kayson', 'Bodhi', 'Bryan', 'Aidan', 'Cohen', 'Brian', 'Cayden', 'Andre', 'Niko', 'Maximiliano', 'Zander', 'Khalil', 'Rory', 'Francisco', 'Cruz', 'Kobe', 'Reid', 'Daxton', 'Derek', 'Martin', 'Jensen', 'Karson', 'Tate', 'Muhammad', 'Jaden', 'Joaquin', 'Josue', 'Gideon', 'Dante', 'Cody', 'Bradley', 'Orion', 'Spencer', 'Angelo', 'Erick', 'Jaylen', 'Julius', 'Manuel', 'Ellis', 'Colson', 'Cairo', 'Gunner', 'Wade', 'Chance', 'Odin', 'Anderson', 'Kane', 'Raymond', 'Cristian', 'Aziel', 'Prince', 'Ezequiel', 'Jake', 'Otto', 'Eduardo', 'Rylan', 'Ali', 'Cade', 'Stephen', 'Ari', 'Kameron', 'Dakota', 'Warren', 'Ricardo', 'Killian', 'Mario', 'Romeo', 'Cyrus', 'Ismael', 'Russell', 'Tyson', 'Edwin', 'Desmond', 'Nasir', 'Remy', 'Tanner', 'Fernando', 'Hector', 'Titus', 'Lawson', 'Sean', 'Kyle', 'Elian', 'Corbin', 'Bowen', 'Wilder', 'Armani', 'Royal', 'Stetson', 'Briggs', 'Sullivan', 'Leonel', 'Callan', 'Finnegan', 'Jay', 'Zayne', 'Marshall', 'Kade', 'Travis', 'Sterling', 'Raiden', 'Sergio', 'Tatum', 'Cesar', 'Zyaire', 'Milan', 'Devin', 'Gianni', 'Kamari', 'Royce', 'Malik', 'Jared', 'Franklin', 'Clark', 'Noel', 'Marco', 'Archie', 'Apollo', 'Pablo', 'Garrett', 'Oakley', 'Memphis', 'Quinn', 'Onyx', 'Alijah', 'Baylor', 'Edgar', 'Nehemiah', 'Winston', 'Major', 'Rhys', 'Forrest', 'Jaiden', 'Reed', 'Santino', 'Troy', 'Caiden', 'Harvey', 'Collin', 'Solomon', 'Donovan', 'Damon', 'Jeffrey', 'Kason', 'Sage', 'Grady', 'Kendrick', 'Leland', 'Luciano', 'Pedro', 'Hank', 'Hugo', 'Esteban', 'Johnny', 'Kashton', 'Ronin', 'Ford', 'Mathias', 'Porter', 'Erik', 'Johnathan', 'Frank', 'Tripp', 'Casey', 'Fabian', 'Leonidas', 'Baker', 'Matthias', 'Philip', 'Jayceon', 'Kian', 'Saint', 'Ibrahim', 'Jaxton', 'Augustus', 'Callen', 'Trevor', 'Ruben', 'Adan', 'Conor', 'Dax', 'Braylen', 'Kaison', 'Francis', 'Kyson', 'Andy', 'Lucca', 'Mack', 'Peyton', 'Alexis', 'Deacon', 'Kasen', 'Kamden', 'Frederick', 'Princeton', 'Braylon', 'Wells', 'Nikolai', 'Iker', 'Bo', 'Dominick', 'Moshe', 'Cassius', 'Gregory', 'Lewis', 'Kieran', 'Isaias', 'Seth', 'Marcos', 'Omari', 'Shane', 'Keegan', 'Jase', 'Asa', 'Sonny', 'Uriel', 'Pierce', 'Jasiah', 'Eden', 'Rocco', 'Banks', 'Cannon', 'Denver', 'Zaiden', 'Roberto', 'Shawn', 'Drew', 'Emanuel', 'Kolton', 'Ayaan', 'Ares', 'Conner', 'Jalen', 'Alonzo', 'Enrique', 'Dalton', 'Moses', 'Koda', 'Bodie', 'Jamison', 'Phillip', 'Zaire', 'Jonas', 'Kylo', 'Moises', 'Shepherd', 'Allen', 'Kenzo', 'Mohamed', 'Keanu', 'Dexter', 'Conrad', 'Bruce', 'Sylas', 'Soren', 'Raphael', 'Rowen', 'Gunnar', 'Sutton', 'Quentin', 'Jaziel', 'Emmitt', 'Makai', 'Koa', 'Maximilian', 'Brixton', 'Dariel', 'Zachariah', 'Roy', 'Armando', 'Corey', 'Saul', 'Izaiah', 'Danny', 'Davis', 'Ridge', 'Yusuf', 'Ariel', 'Valentino', 'Jayson', 'Ronald', 'Albert', 'Gerardo', 'Ryland', 'Dorian', 'Drake', 'Gage', 'Rodrigo', 'Hezekiah', 'Kylan', 'Boone', 'Ledger', 'Santana', 'Jamari', 'Jamir', 'Lawrence', 'Reece', 'Kaysen', 'Shiloh', 'Arjun', 'Marcelo', 'Abram', 'Benson', 'Huxley', 'Nikolas', 'Zain', 'Kohen', 'Samson', 'Miller', 'Donald', 'Finnley', 'Kannon', 'Lucian', 'Watson', 'Keith', 'Westin', 'Tadeo', 'Sincere', 'Boston', 'Axton', 'Amos', 'Chandler', 'Leandro', 'Raul', 'Scott', 'Reign', 'Alessandro', 'Camilo', 'Derrick', 'Morgan', 'Julio', 'Clay', 'Edison', 'Jaime', 'Augustine', 'Julien', 'Zeke', 'Marvin', 'Bellamy', 'Landen', 'Dustin', 'Jamie', 'Krew', 'Kyree', 'Colter', 'Johan', 'Houston', 'Layton', 'Quincy', 'Case', 'Atreus', 'Cayson', 'Aarav', 'Darius', 'Harlan', 'Justice', 'Abdiel', 'Layne', 'Raylan', 'Arturo', 'Taylor', 'Anakin', 'Ander', 'Hamza', 'Otis', 'Azariah', 'Leonard', 'Colby', 'Duke', 'Flynn', 'Trey', 'Gustavo', 'Fletcher', 'Issac', 'Sam', 'Trenton', 'Callahan', 'Chris', 'Mohammad', 'Rayan', 'Lionel', 'Bruno', 'Jaxxon', 'Zaid', 'Brycen', 'Roland', 'Dillon', 'Lennon', 'Ambrose', 'Rio', 'Mac', 'Ahmed', 'Samir', 'Yosef', 'Tru', 'Creed', 'Tony', 'Alden', 'Aden', 'Alec', 'Carmelo', 'Dario', 'Marcel', 'Roger', 'Ty', 'Ahmad', 'Emir', 'Landyn', 'Skyler', 'Mohammed', 'Dennis', 'Kareem', 'Nixon', 'Rex', 'Uriah', 'Lee', 'Louie', 'Rayden', 'Reese', 'Alberto', 'Cason', 'Quinton', 'Kingsley', 'Chaim', 'Alfredo', 'Mauricio', 'Caspian', 'Legacy', 'Ocean', 'Ozzy', 'Briar', 'Wilson', 'Forest', 'Grey', 'Joziah', 'Salem', 'Neil', 'Remi', 'Bridger', 'Harry', 'Jefferson', 'Lachlan', 'Nelson', 'Casen', 'Salvador', 'Magnus', 'Tommy', 'Marcellus', 'Maximo', 'Jerry', 'Clyde', 'Aron', 'Keaton', 'Eliam', 'Lian', 'Trace', 'Douglas', 'Junior', 'Titan', 'Cullen', 'Cillian', 'Musa', 'Mylo', 'Hugh', 'Tomas', 'Vincenzo', 'Westley', 'Langston', 'Byron', 'Kiaan', 'Loyal', 'Orlando', 'Kyro', 'Amias', 'Amiri', 'Jimmy', 'Vicente', 'Khari', 'Brendan', 'Rey', 'Ben', 'Emery', 'Zyair', 'Bjorn', 'Evander', 'Ramon', 'Alvin', 'Ricky', 'Jagger', 'Brock', 'Dakari', 'Eddie', 'Blaze', 'Gatlin', 'Alonso', 'Curtis', 'Kylian', 'Nathanael', 'Devon', 'Wayne', 'Zakai', 'Mathew', 'Rome', 'Riggs', 'Aryan', 'Avi', 'Hassan', 'Lochlan', 'Stanley', 'Dash', 'Kaiser', 'Benicio', 'Bryant', 'Talon', 'Rohan', 'Wesson', 'Joe', 'Noe', 'Melvin', 'Vihaan', 'Zayd', 'Darren', 'Enoch', 'Mitchell', 'Jedidiah', 'Brodie', 'Castiel', 'Ira', 'Lance', 'Guillermo', 'Thatcher', 'Ermias', 'Misael', 'Jakari', 'Emory', 'Mccoy', 'Rudy', 'Thaddeus', 'Valentin', 'Yehuda', 'Bode', 'Madden', 'Kase', 'Bear', 'Boden', 'Jiraiya', 'Maurice', 'Alvaro', 'Ameer', 'Demetrius', 'Eliseo', 'Kabir', 'Kellan', 'Allan', 'Azrael', 'Calum', 'Niklaus', 'Ray', 'Damari', 'Elio', 'Jon', 'Leighton', 'Axl', 'Dane', 'Eithan', 'Eugene', 'Kenji', 'Jakob', 'Colten', 'Eliel', 'Nova', 'Santos', 'Zahir', 'Idris', 'Ishaan', 'Kole', 'Korbin', 'Seven', 'Alaric', 'Kellen', 'Bronson', 'Franco', 'Wes', 'Larry', 'Mekhi', 'Jamal', 'Dilan', 'Elisha', 'Brennan', 'Kace', 'Van', 'Felipe', 'Fisher', 'Cal', 'Dior', 'Judson', 'Alfonso', 'Deandre', 'Rocky', 'Henrik', 'Reuben', 'Anders', 'Arian', 'Damir', 'Jacoby', 'Khalid', 'Kye', 'Mustafa', 'Jadiel', 'Stefan', 'Yousef', 'Aydin', 'Jericho', 'Robin', 'Wallace', 'Alistair', 'Davion', 'Alfred', 'Ernesto', 'Kyng', 'Everest', 'Gary', 'Leroy', 'Yahir', 'Braden', 'Kelvin', 'Kristian', 'Adler', 'Avyaan', 'Brayan', 'Jones', 'Truett', 'Aries', 'Joey', 'Randy', 'Jaxx', 'Jesiah', 'Jovanni', 'Azriel', 'Brecken', 'Harley', 'Zechariah', 'Gordon', 'Jakai', 'Carl', 'Graysen', 'Kylen', 'Ayan', 'Branson', 'Crosby', 'Dominik', 'Jabari', 'Jaxtyn', 'Kristopher', 'Ulises', 'Zyon', 'Fox', 'Howard', 'Salvatore', 'Turner', 'Vance', 'Harlem', 'Jair', 'Jakobe', 'Jeremias', 'Osiris', 'Azael', 'Bowie', 'Canaan', 'Elon', 'Granger', 'Karsyn', 'Zavier', 'Cain', 'Dangelo', 'Heath', 'Yisroel', 'Gian', 'Shepard', 'Harold', 'Kamdyn', 'Rene', 'Rodney', 'Yaakov', 'Adrien', 'Kartier', 'Cassian', 'Coleson', 'Ahmir', 'Darian', 'Genesis', 'Kalel', 'Agustin', 'Wylder', 'Yadiel', 'Ephraim', 'Kody', 'Neo', 'Ignacio', 'Osman', 'Aldo', 'Abdullah', 'Cory', 'Blaine', 'Dimitri', 'Khai', 'Landry', 'Palmer', 'Benedict', 'Leif', 'Koen', 'Maxton', 'Mordechai', 'Zev', 'Atharv', 'Bishop', 'Blaise', 'Davian']
    lastNames = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Martinez','Hernandez','Lopez','Gonzalez','Wilson','Anderson','Thomas','Taylor','Moore','Jackson','Martin','Lee','Perez','Thompson','White','Harris','Sanchez','Clark','Ramirez','Lewis','Robinson','Walker','Young','Allen','King','Wright','Scott','Torres','Nguyen','Hill','Flores','Green','Adams','Nelson','Baker','Hall','Rivera','Campbell','Mitchell','Carter','Roberts']
    #emailThings = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com']
    emailThings = ['@gmail.com']
    firstName = firstNames[random.randint(0, len(firstNames) - 1)]
    lastName = lastNames[random.randint(0, len(lastNames) - 1)]
    numSuffix = random.randint(10,99)
    emailThing = emailThings[random.randint(0, len(emailThings) - 1)]

    email = str(firstName) + str(lastName) + str(numSuffix) + str(emailThing)
    email = str('verifymesenpai69+') + str(email)
    return [firstName, lastName, email]

def WriteObjToFile(fileName, obj):
    objString = str(obj)
    objString = objString.replace(' ', '')
    objString = objString.replace(',', '\t')
    f = open(fileName, 'a')
    f.write(objString)
    f.close()

def ReturnObjFromFile(fileName, randomObj = True):
    f = open(fileName,'r')
    nameObjs = f.readline()
    nameObjs = nameObjs.replace('][', ']\n[')
    nameObjs = nameObjs.replace('\t', ',')
    nameObjs = nameObjs.split('\n')
    nameObj = None

    if(randomObj):
        nameObj = nameObjs[random.randint(0,len(nameObjs) - 1)]

    nameObj = nameObj.replace('[','')
    nameObj = nameObj.replace(']','')
    nameObj = nameObj.replace('\'', '')
    nameObj = nameObj.split(',')
    return nameObj

def LogIn():
    #Click Log In
    signInElem = GetElementBy(By.TAG_NAME, 'IMG', 'title', 'Login')
    signInElem.click()

    #Get Email From File
    nameObj = ReturnObjFromFile('NameFile.txt')
    email = nameObj[2]

    #Input Email
    signInElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'username')
    signInElem.send_keys(email)

    #Input Password
    passwordElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'password')
    passwordElem.send_keys('Password69')

    #Click Submit
    submitElem = GetElementBy(By.TAG_NAME, 'FORM', 'id', 'kc-form-login')
    submitElem.submit()

    print('FINISHED LOGGING IN')
    return nameObj

def VerifyEmail(vEmail):
    try:
        verifyURL = GAPIC.VerifyEmail(email=vEmail)
        nDriver = webdriver.Chrome(executable_path=driverPath,options=options)
        OpenSiteNDriver(nDriver,verifyURL,10)
        nDriver.close()
    except Exception as e:
        print(str(e))

    print('VERIFIED EMAIL')

def SignUp():
    #Click Sign In
    signInElem = GetElementBy(By.TAG_NAME, 'IMG', 'title', 'Sign Up')
    signInElem.click()

    #Generate Name and Email
    nameObj = GenerateName()
    WriteObjToFile('NameFile.txt', nameObj)

    #Populate Email
    emailElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'email')
    emailElem.send_keys(nameObj[2])

    #Create Password
    password = 'Password69'
    passwordElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'password')
    passwordElem.send_keys(password)

    #Confirm Password
    passwordElem = GetElementBy(By.TAG_NAME, 'INPUT', 'id', 'password-confirm')
    passwordElem.send_keys(password)

    #Click Register
    registerElem = GetElementBy(By.TAG_NAME, 'INPUT', 'type', 'submit')
    registerElem.click()

    #Click Sub Option
    time.sleep(5)
    driver.get('https://www.clickasnap.com/myaccount/settings/subscribe/0')

    #Populate Name
    passwordElem = GetElementBy(By.TAG_NAME, 'INPUT', 'name', 'channel_title')
    passwordElem.send_keys(str(nameObj[0] + ' ' + str(nameObj[1])))

    #Populate User URL
    passwordElem = GetElementBy(By.TAG_NAME, 'INPUT', 'name', 'username')
    passwordElem.send_keys(str(str(nameObj[2].split('@')[0])).split('+')[1])

    #Click Validate
    registerElem = GetElementBy(By.TAG_NAME, 'SPAN', 'textContent', 'Check')
    registerElem.click()
    time.sleep(5)

    #Click Confirm
    registerElem = GetElementBy(By.TAG_NAME, 'BUTTON', 'value', 'Confirm')
    registerElem.click()
    time.sleep(10)

    print('FINISHED SIGN UP')
    return nameObj

def DetermineAction(yesChance = 1, noChance = 1):
    yesOrNo = []
    for i in range(0,yesChance):
        yesOrNo.append(True)

    for i in range(0,noChance):
        yesOrNo.append(False)

    return yesOrNo[random.randint(0,len(yesOrNo) - 1)]

def DoStuffOnPage(currentNameObj = None):
    try:
        #Follow
        determination = DetermineAction()
        if(determination):
            driver.refresh()
            GetElementBy(By.TAG_NAME, 'SPAN', 'textContent', 'Follow').click()
        print('FOLLOW ' + str(determination))
    except Exception as e:
        print('ERROR FOLLOWING')
        print(str(e))
        return

    #Get Gallery
    gallery = GetElementBy(By.TAG_NAME, 'DIV', 'className', 'grid largegrid justified-gallery loaded')
    print('GOT GALLERY')

    #Split Gallery
    splitGallery = gallery.find_elements(By.TAG_NAME, 'A')
    print('SPLIT GALLERY')

    #Actions With Split Gallery
    hrefList = []
    for elem in splitGallery:
        if(DetermineAction()):
            hrefList.append(elem.get_attribute('href'))

    #View Page
    currentURL = driver.current_url
    for href in hrefList:
        viewTime = random.randint(10, 20)
        OpenSite(href, viewTime)
        
        try:
            #LIKE
            if(DetermineAction(1,2)):
                #Determine If Already Liked
                likedElem = GetElementBy(By.TAG_NAME, 'SPAN', 'textContent', 'Liked')

                if(likedElem == None):
                    elem = GetElementBy(By.TAG_NAME, 'FORM', 'className', 'like_form')
                    elem.submit()
                    print('LIKED')

            #COMMENT
            if(DetermineAction(1,3)):
                #Determine If Already Liked
                commentNameElem = GetElementBy(By.TAG_NAME, 'A', 'className', 'name')

                if(commentNameElem != None):
                    commentName = commentNameElem.get_attribute('textContent')
                    if(commentName != str(currentNameObj[0] + ' ' + currentNameObj[1])):
                        elem = GetElementBy(By.TAG_NAME, 'TEXTAREA', 'name', 'comment')
                        elem.send_keys(GenerateComment())

                        #SUBMIT COMMENT
                        submitElem = GetElementBy(By.TAG_NAME, 'FORM', 'className', 'ajax_form add-comment-form  mb15')
                        submitElem.submit()
                else:
                    elem = GetElementBy(By.TAG_NAME, 'TEXTAREA', 'name', 'comment')
                    elem.send_keys(GenerateComment())

                    #SUBMIT COMMENT
                    submitElem = GetElementBy(By.TAG_NAME, 'FORM', 'className', 'ajax_form add-comment-form  mb15')
                    submitElem.submit()

        except Exception as e:
            print('ERROR LIKING OR COMMENTING')
            print(str(e))
            return
            

    OpenSite(currentURL)

def RebootVPN():
    StartVPN(10)
    StopVPN(10)

def StartVPN(sleepTime = 15):
    os.system('cmd.exe /c "start C:\\Users\\Michael\\Downloads\\psiphon3.exe"')
    time.sleep(sleepTime)

def StopVPN(sleepTime = 15):
    os.system("taskkill /f /im psiphon3.exe")
    os.system("taskkill /f /im msedge.exe")
    time.sleep(sleepTime)

def main():
    siteURL = 'https://www.clickasnap.com'

    print('MAIN')

    OpenSite(siteURL)

    #Sign Up Or Log In
    nameObj = None
    if(DetermineAction(11,2)):
        print('SIGNING UP')
        nameObj = SignUp()
        VerifyEmail(nameObj[2])
    else:
        print('LOGGIN IN')
        nameObj = LogIn()

    profileSite = 'https://www.clickasnap.com/mrthompsonphotog'
    OpenSite(profileSite)
    driver.refresh()

    DoStuffOnPage(nameObj)

    print('END')

    driver.close()


###########################
for i in range(0,10):
    #subprocess.call('C:\\Users\\Michael\\Downloads\\psiphon3.exe')
    StartVPN()

    main()
    driver = webdriver.Chrome(executable_path=driverPath,options=options)
    currentNameObj = None
    
    StopVPN()