## Simple linear regression

## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
dataset = pd.read_csv('file:///C:/Pradeep/Project/Learning/ML A-Z/P1 Data Preprocessing/Machine-Learning-A-Z/Part 2 - Regression/Section 4 - Simple Linear Regression/Simple_Linear_Regression_sample/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print(X)
print(y)



# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


## Fitting the Simple linear regression to the training set . Using LinearRegression Class
from sklearn.linear_model import LinearRegression
regresss=LinearRegression() #no compulsory arguements
regresss.fit(X_train,y_train)

## Predecting the test results (salary of test set)
y_pred=regresss.predict(X_test)

##Visualize the data #Train set observation plot
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regresss.predict(X_train),color="blue")
plt.title("Salary vs Experience (Train set)")
plt.xlabel("Year of Salary")
plt.ylabel("Salary")
plt.show()



##Visualize the data #Test set observation plot
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regresss.predict(X_train),color="blue")
plt.title("Salary vs Experience (Test Set)")
plt.xlabel("Year of Salary  (Test set)")
plt.ylabel("Salary")
plt.show()

