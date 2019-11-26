## Project URL from 
## Freelancer.com
## Level 1_0 Scraping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_0_proj_url.csv'

urlName = r'https://www.freelancer.com/jobs/regions/?keyword=ended&status=all'
urlPart1 = r'https://www.freelancer.com/jobs/regions/'
urlPart2 = r'/?keyword=ended&status=all'



browser = webdriver.Chrome()
browser.get(urlName)
#browser.refresh()
time.sleep(1)
browser.implicitly_wait(1)

outFile = open(outFileLoc, 'a')



## Header
outFile.write('proj_heading,proj_url\n')

## Loop over pages
page = 0
while page < 50:
    page += 1
    urlFull = urlPart1 + str(page) + urlPart2
    browser.get(urlFull)  # Load page
    time.sleep(1)
    browser.implicitly_wait(1)
    
    ## Resolution
    soup = BeautifulSoup(browser.page_source, 'lxml')

    projList = soup.find_all(class_='JobSearchCard-item-inner')
    print('Page', page, '\t', len(projList), 'jobs')
    for projBlock in projList:
        projLinkBlock = projBlock.find(class_='JobSearchCard-primary-heading-link')
        projLink = projLinkBlock['href']
        projHead = projLinkBlock.get_text()

        projLink = projLink.replace(',','').replace('\n','').replace('\t','')
        projHead = projHead.replace(',','').replace('\n','').replace('\t','')
        try:
            outFile.write(projHead +','+ projLink +'\n')
        except:
            pass
        
outFile.close()

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
    
 

