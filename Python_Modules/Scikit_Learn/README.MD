# Introducing Scikit - Learn
There are several Python libraries that provide solid implementations of a range of machine learning algorithms. One of the best known is __Scikit-Learn__, a package that provides efficient versions of a large number of common algorithms. __Scikit-Learn__ is characterized by a _clean_, _uniform_, and _streamlined API_, as well as by very useful and complete online documentation. A benefit of this uniformity is that once you understand the basic use and syntax of Scikit-Learn for one type of model, switching to a new model or algorithm is very straightforward.

## Scikit-Learn’s Estimator API
The __Scikit-Learn__ API is designed with the following guiding principles in mind, as outlined in the _Scikit-Learn_ API paper:

## 1. Consistency
All objects share a common interface drawn from a limited set of methods, with consistent documentation.
## 2. Inspection
All specified parameter values are exposed as public attributes.
## 3. Limited object hierarchy
Only algorithms are represented by Python classes; datasets are represented in standard formats (NumPy arrays,Pandas DataFrames, SciPy sparse matrices) and parameter names use standard Python strings.
## 4. Composition
Many machine learning tasks can be expressed as sequences of more fundamental algorithms, and Scikit-Learn makes use of this wherever possible.
## 5. Sensible defaults
When models require user-specified parameters, the library defines an appropriate default value.

In practice, these principles make Scikit-Learn very easy to use, once the basic principles are understood. Every machine learning algorithm in Scikit-Learn is implemented via the Estimator API, which provides a consistent interface for a wide range of machine learning applications.

## Basics of the API
Most commonly, the steps in using the __Scikit-Learn estimator API__ are as follows:
1. Choose a class of model by importing the appropriate estimator class from __Scikit-Learn__.
2. Choose model __hyperparameters__ by instantiating this class with desired values.
3. Arrange data into a _features matrix_ and _target vector_.
4. __Fit__ the model to your data by calling the__ fit()__ method of the model instance.
5. Apply the model to new data:

• For __supervised learning__, often we _predict labels_ for unknown data using the ___predict()__ method.

• For __unsupervised learning__, we often transform or infer properties of the data using the __transform()__ or __predict()__ method.

## References
1. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

