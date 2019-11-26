## Project URL from 
## Freelancer.com
## Reinforcement Scraping - 'Other Projects From This Employer'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\freelancer_data_project_list.csv'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\freelancer_data_project_list_out.csv'

## Webdriver
urlName = r'https://www.freelancer.com/jobs/regions/?keyword=ended&status=all'
browser = webdriver.Chrome()
browser.get(urlName)
#browser.refresh()
time.sleep(1)
browser.implicitly_wait(1)


## Input & Output Files
inFile = open(inFileLoc, 'r')
outFile = open(outFileLoc, 'a')


## Header
line = inFile.readline().replace('\n','')
outFile.write(line +','+ 'proj_repeat\n')

## Loop over URLs
while line != '':
    proj_repeat = 0
    cardText = ''
    
    line = inFile.readline().replace('\n','')
    if line == '':
        break
    link = line.split(',')[1]

    browser.get(link)  # Load page
    time.sleep(0.3)
    browser.implicitly_wait(0.3)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    cardList = soup.find_all(class_='Card')
    for card in cardList:
        try:
            cardText = card.find(class_='Card-heading').get_text()
        except:
            cardText = ''
        if cardText != 'Other jobs from this employer':
            continue
        otherList = card.find_all(class_='StyledList-item')
        proj_repeat = len(otherList)
    outFile.write(line +','+ str(proj_repeat) +'\n')

inFile.close()
outFile.close()

'''
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


