## Project URL from 
## Freelancer.com
## Data Processing - Variables

import pandas as pd
import numpy as np
from pandas import ExcelWriter

inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\freelancer_data_1_1.xlsx'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\freelancer_data_1_1_out.xls'

## Input
mainDF = pd.read_excel(inFileLoc)


## Skill Matching
mainDF['P_Skills_Number'] = np.nan
mainDF['F_Skill_Score_1'] = np.nan
mainDF['F_Skill_Score_2'] = np.nan

varList = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
    varList[i] = 'Skill_' + str(varList[i])

row = -1
while True:
    row += 1
    try:
        skillsReq = str(mainDF['P_Skill'][row])
    except:
        break
    
    if len(skillsReq) < 1:
        continue
    skillsReqList = skillsReq.split(',')
    skillsReqNo = len(skillsReqList)

    skillScore1 = 0
    skillScore2 = 0
    for skill in skillsReqList:
        for var in varList:
            if skill == mainDF[var][row]:
                score = mainDF[var + '_e'][row]
                skillScore1 += score/skillsReqNo
                skillScore2 += 1

    mainDF.set_value(row, 'P_Skills_Number', skillsReqNo)
    mainDF.set_value(row, 'F_Skill_Score_1', skillScore1)
    mainDF.set_value(row, 'F_Skill_Score_2', skillScore2)

#print(mainDF[0:30])


## Geo Matching
mainDF['F_Country_Match'] = np.nan

row = -1
while True:
    row += 1
    try:
        empNat = mainDF['P_country'][row].lower().replace(' ','')
    except:
        break

    freNat = mainDF['F_Location_Country'][row].lower().replace(' ','')
    if freNat == empNat:
        mainDF.set_value(row, 'F_Country_Match', 1)
    else:
        mainDF.set_value(row, 'F_Country_Match', 0)

#print(mainDF[0:100])


## Output to Excel
writer = ExcelWriter(outFileLoc)
mainDF.to_excel(writer, 'data')
writer.save()
    
