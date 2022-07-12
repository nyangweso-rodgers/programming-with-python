# Artificial Intelligence
Field of Computer Science that aims to make computers achieve human-style intelligence. There are many approaches to reaching this goal, including __Machine Learning__ & __Deep Learning__.

# Foundations of Machine Learning

## What is Machine Learning?
__Machine Learning__ is the scientific study of _algorithms and statistical models that computer systems use to perform a specific task  without using explicit instructions_, relying on patterns and inference instead. i.e., ML is the study of building generic (generalized) algorithms and statistical models that perform certain tasks e.g., predicting the prices of things. (_Fundamentally, __machine learning__ involves building mathematical models to help understand data._)

## Machine Learning Algorithm/Model
Mathematical expression that reppresents data in the context of a problem, often a business problem. The aim is to go from data to insight.

## Purpose of Machine Learning
ML is required for tasks that are unit too complicated for humans to code directly.

### *Machine Learning = Representation + Evaluation + Optimization*

1. __Representation__: involves the transformation of inputs from one space to another more useful space which can be more easily interpreted.
2. __Evaluation__: is essentially the __loss function__. (how effectively did your algorithm transform your data to a more useful space?)
3. __Optimization__: (this is the last piece of the puzzle) once you have the *evaluation component*, you can optimize the representation function in order to improve your evaluation metric.

# Kinds of Machine Learning Algorithms
__Machine Learning__ can be broken down into three kinds:
## 1. Supervised Learning
_Supervised learning_ involves somehow modeling the relationship between measured features of data and some label associated with the data; once this model is determined, it can be used to apply labels to new, unknown data.

_We apply Supervised ML techniques when we have a piece of data that we want to predict or explain. We do so by using the previous data of inputs and outputs to predict an output based on a new input._

__Supervised Learning__ can then be classified into two algorithms:
### 1.1 Classification
Used to predict which _class_ a data point belongs to, which is usually a _discrete_ value.
#### Examples
1. predicting whether an email is spam or not.
2. predicting whether it's going to rain or not.
3. customer segmentation - classifying your customers into different groups.
4. predicting whether a review is either positive, negative or neutral.

*__NOTE__: classification problem requires the examples to classified into one of two or more classes and can be divided further into __binary-classification__ problem and __multi-label classification__ problem*.

### 1.2 Regression
In _regression_, the labels are _continuous_ quantities.
#### Examples
1. predicting the price of a house
2. predicting the sales of a particular product.
3. salary estimation.


## 2. Unsupervised Learning
Are ML methods that don't make explicit outcome predictions, but instead find hidden relationships in the data. _Unsupervised learning_ involves modeling the features of a dataset without reference to any label, and is often described as “letting the dataset speak for itself.”

*Unsupervised ML looks at ways to relate and group data points without the use of a target variable to predict.i.e, it evaluates data in terms of traits and uses the traits to form clusters of items that are similar to one another.*

#### Examples:
1. can be used in customer segmentation.
2. Fraud detection.
3. used in building recommendation systems

### 2.1 Clustering
_Clustering algorithms_ identify distinct groups of data.
### 2.2 Dimensionality Reduction
_dimensionality reduction algorithms_ search for more succinct representations of the data.


## 3. Reinforcement Learning
Here, we start with no training/input data and our agent learns what to do based on the environment and how to map certain situations into actions in order to maximize reward.

# Model Selection and Hyperparameter Tuning
##  Selecting the Best Model
Of core importance regarding _model selection_ and selection of _hyperparameters_ is the following question: if our _estimator is underperforming_, how should we move forward? There are several possible answers:

1. Use a more complicated/more flexible model
2. Use a less complicated/less flexible model
3. Gather more training samples
4. Gather more data to add features to each sample

The answer to this question is often counterintuitive. In particular, sometimes using a more complicated model will give worse results, and adding more training samples may not improve your results! The ability to determine what steps will improve your model is what separates the successful machine learning practitioners from the unsuccessful.

## The bias–variance trade-off
Fundamentally, the question of “_the best model_” is about finding a sweet spot in the trade-off between __bias__ and __variance__.

A model is said to __underfit__ the data if it does not have enough model _flexibility_ to suitably account for all the features in the data. Another way of saying this is that the model has __high bias__.

A model is said to __overfit__ the data if it has so much model flexibility that the model ends up accounting for random errors as well as the underlying data distribution. Another way of saying this is that the model has __high variance__.

__R^2 score__, or __coefficient of determination__, measures how well a model performs relative to a simple mean of the target values. __R^2 = 1__ indicates a perfect match, __R^2 = 0__ indicates the model does no better than simply taking the mean of the data, and negative values mean even worse models.

_Remarks:_
* For __high-bias models__, the performance of the model on the validation set is similar to the performance on the training set.
* For __high-variance models__, the performance of the model on the validation set is far worse than the performance on the training set.

### Essential features of a Validation Curve:
* The training score is everywhere higher than the validation score. This is generally
the case: the model will be a better fit to data it has seen than to data it has not seen.
* For very low model complexity (a high-bias model), the training data is underfit,
which means that the model is a poor predictor both for the training data and for
any previously unseen data.
* For very high model complexity (a high-variance model), the training data is
overfit, which means that the model predicts the training data very well, but fails
for any previously unseen data.
* For some intermediate value, the validation curve has a maximum. This level of
complexity indicates a suitable trade-off between bias and variance.

