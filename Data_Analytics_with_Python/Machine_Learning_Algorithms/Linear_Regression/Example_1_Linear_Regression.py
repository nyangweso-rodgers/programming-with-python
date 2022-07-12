# Linear Regression with only Python and Numpy
## Implementing Linear Regression in Python without using any Machine Learning Libraries
import numpy as np    
import matplotlib.pyplot as plt
import pandas as pd
import time

df = pd.read_csv('https://raw.githubusercontent.com/Baakchsu/LinearRegression/master/weight-height.csv') # data set from GitHub
df
## Creating a Linear Regression Class
class LinearRegression:
    def fit(self, X, Y):
        X = np.array(X).reshape(-1, 1)
        Y = np.array(Y).reshape(-1, 1)
        x_shape = X.shape 
        self.parameter_cache = []
        num_var = x_shape[1] # the shape corresponds to number of input variable dimensions. There is only one for this dataset i.e., weight of person
        self.weight_matrix - np.random.normal(-1, 1, (num_var, 1))
        self.intercept = np.random.rand(1)
        for i in range(50):
            self.dcostdm = np.sum(np.multiply(((np.matmul(X,self.weight_matrix)+self.intercept)-Y),X))*2/x_shape[0] #w.r.t to the weight
            self.dcostdc = np.sum(((np.matmul(X,self.weight_matrix)+self.intercept)-Y))*2/x_shape[0]          #partial derivative of cost w.r.t the intercept
            self.weight_matrix -= 0.1*self.dcostdm                                                                  #updating the weights with the calculated gradients
            self.intercept -= 0.1*self.dcostdc                                                                      #updating the weights with the calculated gradients
            self.parameter_cache.append(np.array((self.weight_matrix,self.intercept)))                             #the parameters are cached just to track the progress
            return self.weight_matrix,self.intercept,self.parameter_cache
        def predict(self,X):
            product = np.matmul(np.array(X).reshape(-1,1),self.weight_matrix)+self.intercept
            return product
## Training the Linear Regression Model
for i in range(50):
    self.dcostdm =  np.sum(np.multiply(((np.matmul(X,self.weight_matrix)+self.intercept)-Y),X))*2/x_shape[0] #partial derivative of cost w.r.t the weights
    self.dcostdc = np.sum(((np.matmul(X,self.weight_matrix)+self.intercept)-Y))*2/x_shape[0]                #partial derivative of cost w.r.t the intercept
    self.weight_matrix -= 0.1*self.dcostdm                                                                  #updating the weights with the calculated gradients
    self.intercept -= 0.1*self.dcostdc                                                                      #updating the weights with the calculated gradients
    self.parameter_cache.append(np.array((self.weight_matrix,self.intercept)))
return self.weight_matrix,self.intercept,self.parameter_cache

## The Predict Method
def predict(self,X):
    product =  np.matmul(np.array(X).reshape(-1,1),self.weight_matrix)+self.intercept
    return product

## How do We Use the Model Class?
reg = LinearRegression()

'''
Till now, we just created the model class and the training code. 
Now, we’ll create an instance of the Linear Regression class with the above line of code.
'''
x = (df['Weight']-df['Weight'].mean())/df['Weight'].std() #standardization of the dataset
y = (df["Height"]-df["Height"].mean())/df["Height"].std() #standardization of the dataset
'''
These two lines will standardize the dataset using the mathematical formula X-u/std. 
In that, X is the variable we want to standardize, ‘u’ is the mean of that variable and ‘std’ is the standard deviation. 
This helps the model learn faster as all the variables will be in the range ( -1 to 1). It centers the mean to 0 and unit standard deviation (std=1).
'''
params = reg.fit(x[:-180],y[:-180])
'''
By calling the fit method of the class instance ‘reg’ and passing the X and Y values, we initiate the training. 
Here, we pass the dataset leaving the last 180 data points for testing.
'''

## Model Visualization
pred = reg.predict(np.array(x[-180:]))
plt.scatter(x[-180:],y[-180:])
plt.plot(x[-180:],pred)