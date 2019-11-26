## Project URL from 
## Freelancer.com
## Level 1_1 Scraping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_0_proj_url.csv'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_1_proj_url.csv'

urlName = r'https://www.freelancer.com/jobs/regions/?keyword=ended&status=all'
urlPart1 = r'https://www.freelancer.com'
urlPart2 = ''



browser = webdriver.Chrome()
browser.get(urlName)
#browser.refresh()
time.sleep(1)
browser.implicitly_wait(1)

inFile = open(inFileLoc, 'r')
outFile = open(outFileLoc, 'a')



## Header
line = inFile.readline()
outFile.write('employer,proj_heading,proj_url\n')

## Loop over base URLs
employer = 0
while line != '':
    employer += 1
    line = inFile.readline().replace('\n','')
    if line == '':
        break
    urlPart2 = line.split(',')[1]
    outFile.write( str(employer) +','+ line +'\n')
    
    urlFull = urlPart1 + urlPart2
    browser.get(urlFull)  # Load page
    time.sleep(0.5)
    browser.implicitly_wait(0.5)
    
    ## Resolution
    soup = BeautifulSoup(browser.page_source, 'lxml')

    cardList = soup.find_all(class_='Card-body')
    print( len(cardList), 'cards on page')
    if len(cardList) <= 3:
        continue
    
    projBlock = cardList[ len(cardList)-2 ]
    projLinkBlockList = projBlock.find_all(class_='PageProjectViewLogout-section-link')

    for projLinkBlock in projLinkBlockList:
        projLink = projLinkBlock['href']
        projHead = projLinkBlock.get_text()

        projLink = projLink.replace(',','').replace('\n','').replace('\t','')
        projHead = projHead.replace(',','').replace('\n','').replace('\t','')
        try:
            outFile.write( str(employer) +','+ projHead +','+ projLink +'\n')
        except:
            pass
        
inFile.close()
outFile.close()

#Card-body
#PageProjectViewLogout-section-link



'''
    for i in range(2):
        ## Departure airport
        element1 = browser.find_element_by_xpath(".//*[@name='tbDeptAID']")
        element1.click()  # Clicking on the departure airport
        element1.clear()
        element1.send_keys( AP0 )  # Input departure airport code
        element1.send_keys(Keys.ENTER)
        time.sleep(0.5)

        ## Arrival airport
        element2 = browser.find_element_by_xpath("//*[@name='tbArrvAID']")
        element2.click()  # Clicking on the departure airport
        element2.clear()
        element2.send_keys( AP[i] )  # Input arrival airport code
        element2.send_keys(Keys.ENTER)
        time.sleep(0.2)

        ## Submit calculation
        element3 = browser.find_element_by_xpath("//*[@id='lbSubmit']")
        try:
            element3.click()
        except:
            time.sleep(2)
            element3.click()
'''
    
 

