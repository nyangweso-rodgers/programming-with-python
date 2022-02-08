# Decision Tree
__Decision Tree__ analysis is a general, predictive modelling tool constructed via an algorithmic approach that identifies ways to split a data set based on different conditions. __Decision Trees__ are _non-parametric_ __Supervised__ learning method used for both __classification__ and __regression__ tasks. The goal is to _create a model that predicts the value of a target variable by learning simple decision rules inferrred from the data features_.

## Definitions of Terms
* __Instances__: refer to the vector of feature that define the input space.
* __Attribute__: a quantity describing an instance
* __Concept__: the function that maps input to output
* __Target Concept__: the function that we are trying to find i.e., the actual answer
* __Hypothesis Class__: set of all the possible functions.
* __Sample__: set of inputs paired with a label, which is the correct output (also known as the __Training Set__)
* __Candidate Concept__: a concept which we think is a target concept
* __Testing Concet__: similar to the training set and is used to test the candidate concept and determmine its performance.

## Issues in Decision Trees
1. __Avoiding Overfitting__:
* allow the tree to grow until it overfits and then prune it
* prevent the tree from growing too deep by stopping it before it perfectly classifies the training training data.

2. __Incorporating continuous valued attributes__

## Advantages of Decision Trees
1. Easy to use and understand
2. Can handle both categorical and numerical data
3. Resistant to outliers, hence require little data preprocessing
4. New features can be easily added
5. Can be used to build larger classifiers by using ensemble methods.

## Disadvantages of Decision Trees
1. prone to overfitting
2. require some kind of measurement as to how well they are doing.
3. need to be careful with parameter tuning
4. can create biased learned trees if some classes dominate