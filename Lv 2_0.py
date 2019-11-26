## Project info from 
## Freelancer.com
## Level 2_0 Scraping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_3_proj_url.csv'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\2_0_proj_url.csv'

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
outFile.write('employer,proj_heading,proj_url,emp_rating,emp_review,emp_loc,proj_id,proj_skills,proj_budget,proj_status,fcer_url,if_awarded\n')

## Loop over job URLs
while line != '':
    line = inFile.readline().replace('\n','')
    if line == '':
        break
    urlPart2 = line.split(',')[2]
    
    urlFull = urlPart1 + urlPart2
    browser.get(urlFull)  # Load page
    time.sleep(0.3)
    browser.implicitly_wait(0.3)
    
    ## Resolution
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # Employer: Star ratings, # of reviews
    try:
        empRatingElement = soup.find(class_='Rating Rating--labeled profile-user-rating PageProjectViewLogout-detail-reputation-item')
        empRating = empRatingElement['data-star_rating']
        empReview = empRatingElement.find(class_='Rating-review').get_text()
    except:
        continue
    empReview = empReview.replace(',','').replace('\n','').replace('\t','')
    empReview = empReview.replace(' ','').replace('reviews','').replace('(','').replace(')','')

    # Employer: Location
    empLoc = soup.find(itemprop='addressLocality').get_text()
    empLoc = empLoc.replace(',','').replace('\n','').replace('\t','')

    # Project: ID, Skills
    blockList = soup.find_all(class_='PageProjectViewLogout-detail-tags')
    '''
    if len(blockList) == 4:
        print('Skills, See more, Proj ID: OK')
    else:
        print('\nException!\n')
    '''
    projID = blockList[3].get_text()
    projID = projID.replace(',','').replace('\n','').replace('\t','')

    projSkillElements = blockList[0].find_all(class_='PageProjectViewLogout-detail-tags-link--highlight')
    projSkills = []
    for element in projSkillElements:
        skill = element.get_text()
        projSkills.append(skill)

    # Project: Budget
    projBudget = soup.find(class_='PageProjectViewLogout-header-byLine').get_text()
    projBudget = projBudget.replace(',','').replace('\n','').replace('\t','')

    #print(empRating, '\n', empReview, '\n', empLoc, '\n', projID, '\n', projSkills, '\n', projBudget, '\n')
    # Output
    skillString = ''
    for skill in projSkills:
        skillString = skillString + skill + '| '
    skillString = skillString[:-2]

    line = line +','+ empRating +','+ empReview +','+ empLoc +','+ projID +','+ skillString +','+ projBudget

    # All freelancers
    cardList = soup.find_all(class_='Card-body')

    # Awarded to
    awardedTo = soup.find(class_='PageProjectViewLogout-awardedTo-heading')
    if awardedTo == None:
        cardNum = 1
        awardedGuyLink = '-'
        line = line + ',pending'
    else:
        cardNum = 2
        awardedGuy = cardList[1].find(class_='FreelancerInfo-username')
        awardedGuyLink = awardedGuy['href']
        line = line + ',decided'
    #print(awardedGuyLink, '\n')
        # Output
        try:
            outFile.write(line +','+ awardedGuyLink +',Yes' +'\n')
        except:
            pass

    # Not awarded
    guysCard = cardList[cardNum]
    guyList = guysCard.find_all(class_='FreelancerInfo-username')
    guys = []
    for guyElement in guyList:
        try:
            guyLink = guyElement['href']
            guys.append(guyLink)
        except:
            continue
        # Output
        try:
            outFile.write(line +','+ guyLink +',No' +'\n')
        except:
            pass
    
    #print(guys, '\n')
    
        
inFile.close()
outFile.close()

#Card-body
#PageProjectViewLogout-section-link
#Rating Rating--labeled profile-user-rating PageProjectViewLogout-detail-reputation-item
#PageProjectViewLogout-detail-tags
#PageProjectViewLogout-header-byLine
#PageProjectViewLogout-awardedTo-heading


