#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Load Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


#Load Data
drugdata = pd.read_csv('./drugdataset.csv')
drugdata.head()


# In[43]:


drugdata.describe()


# In[39]:


#Identify number of Classes (i.e. Species)
drugdata.Drug.unique()


# In[44]:


#Create x and y variables
X = drugdata.drop('Drug',axis=1).to_numpy()
y = drugdata['Drug'].to_numpy()

#Create Train and Test datasets
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,test_size = 0.2,random_state=100)

#Scale the data
from sklearn.preprocessing import StandardScaler  
sc = StandardScaler()  
x_train2 = sc.fit_transform(X_train)
x_test2 = sc.transform(X_test)


# In[45]:


#Script for Neural Network
from sklearn.neural_network import MLPClassifier  
mlp = MLPClassifier(hidden_layer_sizes=(5,4,5),
                    activation='relu',solver='adam',
                    max_iter=10000,random_state=100)  
mlp.fit(x_train2, y_train) 
predictions = mlp.predict(x_test2) 

#Evaluation Report and Matrix
from sklearn.metrics import classification_report, confusion_matrix  
target_names=['drugY', 'drugC', 'drugX', 'drugA', 'drugB']
print(confusion_matrix(y_test,predictions))  
print(classification_report(y_test,predictions,target_names=target_names)) 


# In[ ]:




