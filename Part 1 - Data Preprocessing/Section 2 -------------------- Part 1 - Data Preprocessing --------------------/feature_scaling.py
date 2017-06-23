# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:55:30 2017

@author: pradeep
"""

## Data Preprocessing

## Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
dataset = pd.read_csv('C:\Pradeep\Project\Learning\ML A-Z\P1 Data Preprocessing\Machine-Learning-A-Z\Part 1 - Data Preprocessing\Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

## Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Coverting categorical data to numerical value 

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder_X=LabelEncoder()

X[:,0]=labelencoder_X.fit_transform(X[:,0]) 

##array([0, 2, 1, 2, 1, 0, 2, 0, 1, 0]
##0=France, 2=Spain, 1=Germany

oneHotEncoder=OneHotEncoder(categorical_features=[0]) #categorical_features encode First column

X=oneHotEncoder.fit_transform(X).toarray()

labelencoder_y=LabelEncoder()

y=labelencoder_X.fit_transform(y)   #Since it is a dependent variable. Label encoder is enough


#Splitting the data in to training and test set
from sklearn.cross_validation import train_test_split

#20% of the data will be test set (good choice will be, 20 or 25%)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


#feature scaling
from sklearn.preprocessing import StandardScaler
scaling_X=StandardScaler()
X_train=scaling_X.fit_transform(X_train)
X_test=scaling_X.transform(X_test)


