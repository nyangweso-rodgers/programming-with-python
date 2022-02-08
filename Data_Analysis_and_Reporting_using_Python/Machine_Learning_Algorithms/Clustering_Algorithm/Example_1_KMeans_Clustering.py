# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

wholesale_customer_data = pd.read_csv('Wholesale customers data.csv')
# print(wholesale_customer_data.head())
# print(wholesale_customer_data.info())
# print(wholesale_customer_data.describe())

X = wholesale_customer_data.copy()

# Visualization of the data using Pairplot
'''
sns.pairplot(X,
             x_vars=['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen'],
             #y_vars=['Channel', 'Region']
             y_vars=['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen'],
             )
'''

## Observations from the pandas describe method
'''
Here, we notice that there is a lot of variation in the magnitude of the data. 
Variables like Channel and Region have low magnitude whereas variables like Fresh, Milk, Grocery, etc. have a higher magnitude.

Since K-Means is a distance-based algorithm, this difference of magnitude can create a problem. 
So let’s first bring all the variables to the same magnitude:
'''
# standardizing the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(X)

# statistics of scaled data
pd.DataFrame(data_scaled).describe()

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

## Let’s evaluate how well the formed clusters are. To do that, we will calculate the inertia of the clusters:
print(# inertia on the fitted data
kmeans.inertia_) # Output: 2599.38555935614

'''
We got an inertia value of almost 2600. 
Now, let’s see how we can use the elbow curve to determine the optimum number of clusters in Python.

We will first fit multiple k-means models and in each successive model, we will increase the number of clusters. 
We will store the inertia value of each model and then plot it to visualize the result:
'''
# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

'''
Looking at the elbow curve, we can choose any number of clusters between 5 to 8. 
Let’s set the number of clusters as 6 and fit the model:
'''
# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)
#print(pred)

# Finally, let’s look at the value count of points in each of the above-formed clusters:
frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
print(frame['cluster'].value_counts())
#print(frame)
# So, there are 234 data points belonging to cluster 4 (index 3), then 125 points in cluster 2 (index 1), and so on. 
frame.to_excel('Example_1_KMeans_Clustering_Predictions.xlsx')