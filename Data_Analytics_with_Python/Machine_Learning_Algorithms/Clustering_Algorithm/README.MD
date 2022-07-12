# Clustering
## K-Means Clustering
__k-means__ clustering is a method of __vector quantization__ that aims to _partition n observations into k clusters_ in which each observation belongs to the cluster with the nearest mean (__cluster centers__ or __cluster centroid__), serving as a prototype of the cluster. This results in a partitioning of the data space into __Voronoi cells__. k-means clustering minimizes within-cluster variances (__squared Euclidean distances__), but not regular Euclidean distances.

In __clustering__, we do not have a target to predict. We look at the data and then try to club similar observations and form different groups. Hence it is an __unsupervised learning__ problem.

### Properties of Clusters
* All the data points in a cluster should be similar to each other
* The data points from different clusters should be as different as possible

### Applications of Clustering in Real-World Scenarios
* Customer Segmentation
* Document Clustering
* Image Segmentation
* Recommendation Engines

### Understanding the Different Evaluation Metrics for Clustering
1. __Inertia__: calculates the sum of distances of all the points within a cluster from the centroid of that cluster. _NOTE_: the lesser the inertia value, the better our clusters are.
2. __Dunn Index__: Along with the distance between the centroid and points, the _Dunn index_ also takes into account the distance between two clusters. This distance between the centroids of two different clusters is known as __inter-cluster__ distance. 

__Dunn Index__ = min(Inter Cluster distance) / max(Intra Cluster distance)

_REMARK:_Dunn index is the ratio of the minimum of inter-cluster distances and maximum of intracluster distances. We want to maximize the Dunn index. The more the value of the Dunn index, the better will be the clusters.

### Introduction to K-Means Clustering
__K-means__ is a _centroid-based algorithm_, or a _distance-based algorithm_, where we calculate the distances to assign a point to a cluster. In __K-Means__, each cluster is associated with a centroid. The main objective of the __K-Means__ algorithm is to _minimize the sum of distances between the points and their respective cluster centroid_.

### Steps to Creating Clusters with K-means
1. __Step 1:__ Choose the number of clusters k
2. __Step 2:__ _Select k random points from the data as centroids_. Next, we randomly select the centroid for each cluster. Let’s say we want to have 2 clusters, so k is equal to 2 here. We then randomly select the centroid.
3. __Step 3:__ Assign all the points to the closest cluster centroid
4. __Step 4:__ _Recompute the centroids of newly formed clusters_. Now, once we have assigned all of the points to either cluster, the next step is to compute the centroids of newly formed clusters:
5. __Step 5:__ Repeat steps 3 and 4

## Challenges with the K-Means Clustering Algorithm
1. different cluster sizes
2. densities of the original points are different

__Remark:__ 
* _One of the solutions is to use a higher number of clusters._
* _Remember how we randomly initialize the centroids in __k-means__ clustering? Well, this is also potentially problematic because we might get different clusters every time. So, to solve this problem of __random initialization__, there is an algorithm called __K-Means++__ that can be used to choose the initial values, or the initial cluster centroids, for K-Means._

## K-Means++ to Choose Initial Cluster Centroids for K-Means Clustering
In some cases, if the initialization of clusters is not appropriate, __K-Means__ can result in arbitrarily bad clusters. This is where __K-Means++__ helps. It _specifies a procedure to initialize the cluster centers before moving forward with the standard k-means clustering algorithm_.

Using the __K-Means++__ algorithm, we optimize the step where we randomly pick the cluster centroid. We are more likely to find a solution that is competitive to the optimal K-Means solution while using the K-Means++ initialization.

### The steps to initialize the centroids using K-Means++ are:
1. The first cluster is chosen uniformly at random from the data points that we want to cluster. This is similar to what we do in K-Means, but instead of randomly picking all the centroids, we just pick one centroid here
2. Next, we compute the distance (D(x)) of each data point (x) from the cluster center that has already been chosen
3. Then, choose the new cluster center from the data points with the probability of x being proportional to (D(x))2
4. We then repeat steps 2 and 3 until k clusters have been chosen

_REMARK:_ 
* _Using K-Means++ to initialize the centroids tends to improve the clusters. Although it is computationally costly relative to random initialization, subsequent K-Means often converge more rapidly._

## How to Choose the Right Number of Clusters in K-Means Clustering?
_NOTE:_ _The maximum possible number of clusters will be equal to the number of observations in the dataset._

But then how can we decide the optimum number of clusters? One thing we can do is plot a graph, also known as an __elbow curve__, where the _x-axis will represent the number of clusters_ and the _y-axis will be an evaluation metric_. 

_REMARK:_ 
* __the cluster value where the decrease in inertia value becomes constant can be chosen as the right cluster value for our data.__
* You must also look at the __computation cost__ while deciding the number of clusters. If we increase the number of clusters, the computation cost will also increase. So, if you do not have high computational resources, my advice is to choose a lesser number of clusters.
## _References_
1. https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/