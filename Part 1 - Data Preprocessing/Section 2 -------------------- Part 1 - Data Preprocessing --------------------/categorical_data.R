
#**Import the data set**

#**set the working directory**

setwd("C:/Pradeep/Project/Learning/ML A-Z/P1 Data Preprocessing/Machine-Learning-A-Z/Part 1 - Data Preprocessing")


#**Import the data set**

dataset=read.csv("data.csv")


#**print the data set**

print(dataset)

#**Matrix creation is not required in R**


## Take care of missing data

dataset$Age = ifelse(is.na(dataset$Age),
                     ave((dataset$Age),FUN = function(x) mean(x,na.rm = TRUE))
                     ,dataset$Age)



dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave((dataset$Salary),FUN = function(x) mean(x,na.rm = TRUE))
                        ,dataset$Salary)


## Encoding the categorical data

dataset$Country=factor(dataset$Country,levels = c("France","Spain","Germany"),labels = c(1,2,3))

print(dataset$Country)

dataset$Purchased=factor(dataset$Purchased,levels = c("Yes","No"),labels = c(0,1))

print(dataset$Purchased)