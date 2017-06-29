#**Import the data set**
setwd("C:/Pradeep/Project/Learning/ML A-Z/P1 Data Preprocessing/Machine-Learning-A-Z/Part 2 - Regression/Section 4 - Simple Linear Regression/Simple_Linear_Regression_sample/")
trade_dataset=read.csv("IOC_Data.csv")

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
trade_split = sample.split(trade_dataset$Last.Price, SplitRatio = 2/3)
trade_training_set = subset(trade_dataset, trade_split == TRUE)
trade_test_set = subset(trade_dataset, trade_split == FALSE)


# Fitting Simple Linear Regression to the Training Set
trade_regressor=lm(formula = Last.Price ~ Day,data = trade_training_set)
summary(trade_regressor)

# Predicting the test results
trade_y_pred=predict(trade_regressor,data=trade_test_set)

#Visualizing training test results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x=trade_training_set$Day,y = trade_training_set$Last.Price),
             colour="red"
  )+
  geom_line(aes(x=trade_training_set$Day,predict(trade_regressor,newdata = trade_training_set)),
            colour ="blue"
  )+
  ggtitle("Price vs Day (Training set)") +
  xlab("Day") +
  ylab("Price")


#Visualizing training test results
#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x=trade_test_set$Day,y = trade_test_set$Last.Price),
             colour="red"
  )+
  geom_line(aes(x=trade_training_set$Day,predict(trade_regressor,newdata = trade_training_set)),
            colour ="blue"
  )+
  ggtitle("Price vs Day (Training set)") +
  xlab("Day") +
  ylab("Price")

