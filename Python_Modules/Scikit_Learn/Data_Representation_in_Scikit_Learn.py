# Data Representation in Sckit-Learn
'''
Consider the Iris dataset, famously analyzed by Ronald Fisher in 1936. 
We can download this dataset in the form of a Pandas DataFrame using the Seaborn library:
'''
import seaborn as sns  
iris = sns.load_dataset('iris')
iris.head()

'''
Here each row of the data refers to a single observed flower, and the number of rows is the total number of flowers in the dataset. 
In general, we will refer to the rows of the matrix as samples, and the number of rows as n_samples.

Likewise, each column of the data refers to a particular quantitative piece of information that describes each sample. 
In general, we will refer to the columns of the matrix as features, and the number of columns as n_features.
'''

# Features Matrix
'''
This table layout makes clear that the information can be thought of as a two-dimensional numerical array or matrix, which we will call the features matrix. 
By convention, this features matrix is often stored in a variable named X. 
The features matrix is assumed to be two-dimensional, with shape [n_samples, n_features], and is
most often contained in a NumPy array or a Pandas DataFrame, though some Scikit-Learn models also accept SciPy sparse matrices.

The samples (i.e., rows) always refer to the individual objects described by the dataset.
For example, the sample might be a flower, a person, a document, an image, a sound
file, a video, an astronomical object, or anything else you can describe with a set of quantitative measurements.

The features (i.e., columns) always refer to the distinct observations that describe
each sample in a quantitative manner. Features
'''

# Target Array
'''
In addition to the feature matrix X, we also generally work with a label or target array, which by convention we will usually call y. 
The target array is usually one dimensional, with length n_samples, and is generally contained in a NumPy array or Pandas Series. 
The target array may have continuous numerical values, or discrete classes/labels. 

Often one point of confusion is how the target array differs from the other features columns. 
The distinguishing feature of the target array is that it is usually the quantity we want to predict from the data: in statistical terms, it is the dependent variable. 
For example, in the preceding data we may wish to construct a model that can predict the species of flower based on the other measurements; in this case, the species column
would be considered the feature.
'''
## With this target array in mind, we can use Seaborn to conveniently visualize the data
%matplotlib inline 
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()
sns.pairplot(iris, hue='species', size=1.5)
plt.title('A visualization of the Iris dataset')

'''
For use in Scikit-Learn, we will extract the features matrix and target array from the DataFrame, which we can do using some of the Pandas DataFrame operations
'''
X_iris = iris.drop('species', axis = 1)
X_iris.shape # (150, 4)

y_iris = iris['species']
y_iris.shape # (150, )