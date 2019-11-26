## Project info from 
## Freelancer.com
## Level 2_0 Scraping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\2_0_proj_url_test.csv'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\3_0_proj_url.csv'

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
line = inFile.readline().replace('\n','')
outFile.write(line)

## Loop over job URLs
while line != '':
    line = inFile.readline().replace('\n','')
    if line == '':
        break
    urlPart2 = line.split(',')[10]
    
    urlFull = urlPart1 + urlPart2
    browser.get(urlFull)  # Load page
    time.sleep(0.1)
    browser.implicitly_wait(0.1)
    
    ## Resolution
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # Location
    try:
        fcerLoc = soup.find(itemprop='addressLocality').get_text()
        fcerLoc = fcerLoc.replace(',','').replace('\n','').replace('\t','')
        fcerLoc = fcerLoc.replace('\'','').replace('\"','')
    except:
        fcerLoc = '-'

    try:
        fcerNat = soup.find(itemprop='addressCountry').get_text()
        fcerNat = fcerNat.replace(',','').replace('\n','').replace('\t','')
        fcerNat = fcerNat.replace('\'','').replace('\"','')
    except:
        fcerNat = '-'
    
    # Date joined
    dateJoin = soup.find(class_='profile-membership-length').get_text()
    dateJoin = dateJoin.replace(',','').replace('\n','').replace('\t','')
    dateJoin = dateJoin.replace('\'','').replace('\"','')

    # Recommendation
    recom = soup.find(class_='profile-recommendation').get_text()
    recom = recom.replace(',','').replace('\n','').replace('\t','')
    recom = recom.replace('\'','').replace('\"','')

    # Price
    price = soup.find(class_='profile-hourly-rate').get_text()
    price = price.replace(',','').replace('\n','').replace('\t','')
    price = price.replace('\'','').replace('\"','')

    # Rating
    fcerRatingBlock = soup.find(class_='Rating Rating--labeled profile-user-rating')
    try:
        fcerRating = fcerRatingBlock['data-star_rating']
    except:
        fcerRating = '-'

    # Review
    fcerReview = soup.find(class_='Rating-review').get_text()
    fcerReview = fcerReview.replace(',','').replace('\n','').replace('\t','')
    fcerReview = fcerReview.replace('\'','').replace('\"','')

    # Earnings
    fcerEarnings = soup.find(class_='Earnings-label').get_text()
    fcerEarnings = fcerEarnings.replace(',','').replace('\n','').replace('\t','')
    fcerEarnings = fcerEarnings.replace('\'','').replace('\"','')

    # Stats
    stats = soup.find(class_='item-stats').get_text()
    print(stats)

    # Certifications
    fcerCer
    

    # Top Skills
    fcerSkills 
    
        
inFile.close()
outFile.close()

#Card-body
#PageProjectViewLogout-section-link
#Rating Rating--labeled profile-user-rating PageProjectViewLogout-detail-reputation-item
#PageProjectViewLogout-detail-tags
#PageProjectViewLogout-header-byLine
#PageProjectViewLogout-awardedTo-heading


