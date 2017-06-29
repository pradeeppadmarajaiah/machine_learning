#**Import the data set**
setwd("C:/Pradeep/Project/Learning/ML A-Z/P1 Data Preprocessing/Machine-Learning-A-Z/Part 2 - Regression/Section 4 - Simple Linear Regression/Simple_Linear_Regression_sample/")
real_dataset=read.csv("Salary_Data.csv")

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
real_split = sample.split(real_dataset$Salary, SplitRatio = 2/3)
real_training_set = subset(real_dataset, real_split == TRUE)
real_test_set = subset(real_dataset, real_split == FALSE)


# Fitting Simple Linear Regression to the Training Set
real_regressor=lm(formula = Salary ~ YearsExperience,data = real_training_set)
summary(real_regressor)

# Predicting the test results
real_y_pred=predict(real_regressor,newdata=real_test_set)

#Visualizing training test results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x=real_training_set$YearsExperience,y = real_training_set$Salary),
             colour="red"
  )+
  geom_line(aes(x=real_training_set$YearsExperience,predict(real_regressor,newdata = real_training_set)),
            colour ="blue"
  )+
  ggtitle("Salary vs Exp (Training set)") +
  ylab("Years") +
  xlab("Exp")


#Visualizing training test results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x=real_test_set$YearsExperience,y = real_test_set$Salary),
             colour="red"
  )+
  geom_line(aes(x=real_training_set$YearsExperience,predict(real_regressor,newdata = real_training_set)),
            colour ="blue"
  )+
  ggtitle("Salary vs Exp (Test set)") +
  ylab("Years") +
  xlab("Exp")


