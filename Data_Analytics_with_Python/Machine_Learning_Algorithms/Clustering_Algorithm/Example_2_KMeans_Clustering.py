# Implementing K-Means Clustering in Python
# Customer Segmentation
## Objective: Customer segmentation based on their Income and Amount of Debt

# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv('clustering.csv')
#print(df.head())
#print(df.info())
#print(df.describe())

# we will be taking only two variables from the data – “LoanAmount” and “ApplicantIncome”.
X = df[["LoanAmount","ApplicantIncome"]]

#Visualise data points
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()

# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster

#number of clusters
K=3

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()

'''
From the visualization, the red dots represent the 3 centroids for each cluster. 
Note that we have chosen these points randomly and hence every time you run this code, you might get different centroids.
'''

# Next, we will define some conditions to implement the K-Means Clustering algorithm. Let’s first look at the code:
# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["ApplicantIncome"]-row_d["ApplicantIncome"])**2
            d2=(row_c["LoanAmount"]-row_d["LoanAmount"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]

'''
These values might vary every time we run this. 
Here, we are stopping the training when the centroids are not changing after two iterations. 
We have initially defined the diff as 1 and inside the while loop, we are calculating this diff as the difference between the centroids in the previous iteration and the current iteration.
'''

# When this difference is 0, we are stopping the training. Let’s now visualize the clusters we have got:
color=['blue','green','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["ApplicantIncome"],data["LoanAmount"],c=color[k])
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('Income')
plt.ylabel('Loan Amount (In Thousands)')
plt.show() 


# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=7, init='k-means++')
# fitting the k means algorithm on scaled data
kmeans.fit(X)

## Let’s evaluate how well the formed clusters are. To do that, we will calculate the inertia of the clusters:
# inertia on the fitted data
print('Inertia: ', kmeans.inertia_) # Output: 36457874.707483634

# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(X)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

'''
Looking at the elbow curve, we can choose any number of clusters between 4 to 7. 
Let’s set the number of clusters as 5 and fit the model:
'''

# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_jobs = -1, n_clusters = 7, init='k-means++')
kmeans.fit(X)
pred = kmeans.predict(X)
#print(pred)

# Finally, let’s look at the value count of points in each of the above-formed clusters:
frame = pd.DataFrame(X)
frame['cluster'] = pred
print(frame['cluster'].value_counts())
#print(frame)
# So, there are 234 data points belonging to cluster 4 (index 3), then 125 points in cluster 2 (index 1), and so on. 
frame.to_excel('Example_2_KMeans_Clustering_Predictions.xlsx')