# Task - Predict the Class of the Iris Plant based on the attributes
'''
# Codiing a Decision Tree
-we use the scikit-learn library to code the decision tree model.
- we use the iris data dataset to build a decision tree classifier
- the data set contains information of 3 classes of the iris plant with the following attributes: 
1. sepal length, 
2. sepal width, 
3. petal length, 
4. petal width
5. Iris Setosa
6. Iris Versicolour
7. Iris Virginica
'''
# Improting required libraries
import pandas as pd 
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = load_iris()
print('Data Features: ',data.feature_names) # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print('Classes to predict: ',data.target_names) # ['setosa' 'versicolor' 'virginica']
# print(data.target) 
# print(data.filename) 
# print(data.DESCR) 

# Extracting data attributes
X = data.data
### Extracting target/class labels
y = data.target
print('Number of examples in the data: ', X.shape[0])
# First four rows in the variable 'X'
print(X[:4])
# using the train_test_split to create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 47, test_size = 0.25)

# Since, this is a classification problem, we use the DecisionTreeClassifier function
clf = DecisionTreeClassifier(criterion= 'entropy') # sets the measure for splitting the attribute to information gain
# Training the decision tree classifier
clf.fit(X_train, y_train)

# Predicting Labels onn the test set
y_pred = clf.predict(X_test)

# Evalutaion
'''
we evaluate the predicted classes using some metrics
-- for this case, we woll use the accuracy_score to calculate the accuracy of the predicted labels
'''
## Importing the accuracy metric from sklearn.metrics library
from sklearn.metrics import accuracy_score
print('Accuracy Score on Train data: ', 
      accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('Accuracy Score on Test Data: ', 
      accuracy_score(y_true=y_test, y_pred=y_pred))

# Parameter Tuning
'''
We tune the parameters of the decision  tree to increase  its accuracy. 
-- one of those parameters is 'min_samples_split', which is the minimum number of samples required to split an internal node. its default value = 2 because we cannot split on a node containing only one example/sample
'''
clf_2 = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf_2.fit(X_train, y_train)
print('Accuracy Score on Train Data: ',
     accuracy_score(y_true = y_train, y_pred = clf_2.predict(X_train)))
print('Accuracy Score on Test Data: ',
      accuracy_score(y_true=y_test, y_pred=clf_2.predict(X_test)))
### Remark
'''
-- Accuracy on the Train Set decreased while remained the same for the Test set
'''