## Simple linear regression

## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
dataset_trade = pd.read_csv('file:///C:/Pradeep/Project/Learning/ML A-Z/P1 Data Preprocessing/Machine-Learning-A-Z/Part 2 - Regression/Section 4 - Simple Linear Regression/Simple_Linear_Regression_sample/IOC_Data.csv')
Xt = dataset_trade.iloc[:, :-1].values
yt = dataset_trade.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
Xt_train, Xt_test, yt_train, yt_test = train_test_split(Xt, yt, test_size = 1/3, random_state = 0)

## Fitting the Simple linear regression to the training set . Using LinearRegression Class
from sklearn.linear_model import LinearRegression
regresss_t=LinearRegression() #no compulsory arguements
regresss_t.fit(Xt_train,yt_train)


## Predecting the test results (trade price of test set)
yt_pred=regresss_t.predict(Xt_test)

##Visualize the data #Train set observation plot
plt.scatter(Xt_train,yt_train,color='red')
plt.plot(Xt_train,regresss_t.predict(Xt_train),color="blue")
plt.title("IOC Stock Price vs Day (Train set)")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()



##Visualize the data #Test set observation plot
plt.scatter(Xt_test,yt_test,color='red')
plt.plot(Xt_train,regresss_t.predict(Xt_train),color="blue")
plt.title("IOC Stock Price vs Day (Test Set)")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()


