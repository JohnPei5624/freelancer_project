data <- read.csv(
  file = "E:/2018-0511/GA Project - Freelancer & Experiment/freelancer_data_1_4_v3filtered_only_awarded.csv")
data$F_Price_USD_per_hour <- as.numeric(data$F_Price_USD_per_hour)

str(data)
summary(data)

cor(data[,c(3:8)])

data$F_Country_Match <- as.factor(data$F_Country_Match)
data$F_awarded_binary <- as.factor(data$F_awarded_binary)
