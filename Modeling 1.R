library(ggplot2)
library(lattice)
library(caret)
library(dplyr)
library(mice)
library(VIM)
library(usdm)
library(leaps)

#################logit regression#############
#import data
data<- read.csv(file = "E:/2018-0511/GA Project - Freelancer & Experiment/freelancer_data_1_4_v2filtered_only_awarded.csv")

summary(data)
data$F_Price_USD_per_hour <- as.numeric(data$F_Price_USD_per_hour)
data$F_Country_Match <- as.factor(data$F_Country_Match)

#Model 1
freelancer.glm1<- glm( F_awarded_binary ~P_Rating+P_Reviews+P_income_group
                 , data=data, family = binomial())
summary(freelancer.glm1)

# Model 2
freelancer.glm2<- glm( F_awarded_binary ~P_Rating+P_Reviews+P_income_group+F_Rating+ F_Review+ F_Country_Match+
                         F_Price_USD_per_hour+F_Skill_Score_1+ F_AmountEarned+ F_Months_Till_Sep_2018+ F_Recommendation+P_Repeat
                         
                       , data=data, family = binomial())
summary(freelancer.glm2)

#Model 3
freelancer.glm3<- glm( F_awarded_binary ~P_Rating+P_Reviews+P_income_group+F_Rating+ F_Review+ F_Country_Match+
                         F_Price_USD_per_hour+F_Skill_Score_1+ F_AmountEarned+ F_Months_Till_Sep_2018+ F_Recommendation+P_Repeat+
                         F_Rating*P_Repeat+ F_Review*P_Repeat+ F_Country_Match*P_Repeat+
                         F_Price_USD_per_hour*P_Repeat+F_Skill_Score_1*P_Repeat+ F_AmountEarned*P_Repeat+
                         F_Months_Till_Sep_2018*P_Repeat+ F_Recommendation*P_Repeat
                       
                       , data=data, family = binomial())
summary(freelancer.glm3)




#################linear regression#############
#import data
data2<- read.csv(file = "E:/Fordham/design lab/RP/freelancer/freelancer_data_2_0_selection_accuracy.csv")

summary(data2)

set.seed(1234)

#Model 1
freelancer.lm1<- lm(P_selection_accuracy ~ P_income_group+ P_Rating+ P_Reviews+ P_Repeat, data=data2)

summary(freelancer.lm1)


#Model 2

freelancer.lm2<- lm(P_selection_accuracy ~ P_income_group+ P_Rating+ P_Reviews+ P_Repeat+
                      P_income_group*P_Reviews+ P_Rating*P_Reviews+ P_Reviews*P_Reviews
                      , data=data2)

summary(freelancer.lm2)

