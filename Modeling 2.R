
#################linear regression#############
#import data
data2<- read.csv(file = "E:/2018-0511/GA Project - Freelancer & Experiment/freelancer_data_2_0_selection_accuracy.csv")
summary(data2)
set.seed(1234)

#Model 1
freelancer.lm1<- lm(P_selection_accuracy ~ P_income_group + P_Rating + P_Reviews, 
                    data=data2)
summary(freelancer.lm1)


#Model 2
freelancer.lm2<- lm(P_selection_accuracy ~ P_income_group + P_Rating + P_Reviews + P_Repeat,
                    data=data2)
summary(freelancer.lm2)


#Model 3
freelancer.lm3<- lm(P_selection_accuracy ~ P_income_group + P_Rating + P_Reviews + P_Repeat + 
                      F_Country_Match + P_Repeat*F_Country_Match, 
                    data=data2)
summary(freelancer.lm3)

