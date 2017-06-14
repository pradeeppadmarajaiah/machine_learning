#**Import the libraries**

import numpy as np # **mathematics api**

import matplotlib.pyplot as plt #**To draw a plot**

import pandas as pd #**To import and manage data sets**


#**As a first step, set the working directory**

#**Import the OS lib**

import os

#**Change the directory**

os.chdir("C:\Pradeep\Project\Learning\ML A-Z\P1 Data Preprocessing\Machine-Learning-A-Z\Part 1 - Data Preprocessing")
 
#**Print the current working directory**

print (os.getcwd())


#**Read the data set**

data_set=pd.read_csv("data.csv")

#**Print the data set**

print(data_set)

#**Create a matrix of independent varibles :** Country   Age   Salary

X = data_set.iloc[:, :-1].values #**First colon means all the row. :-1 select all the columns - last**

print(X)


#**Create a matrix of dependent varibles**

y = data_set.iloc[:, 3].values

print(y)


## **Handling mising data** 

#**Import Imputer class from sklearn.preprocessing lib**

from sklearn.preprocessing import Imputer

#****

#**Create an imputer object. Replace NAN with mean value for specific column**

imputer = Imputer(missing_values = 'NaN',strategy = "mean",axis = 0)

## **Fit the value to X** 

#**First colon means all the row. 1 : 3 means Second and Third column*

imputer = imputer.fit(X[:, 1:3])

X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X[:,1])

print(X[:,2])


 