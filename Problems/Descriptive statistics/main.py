import pandas as pd

iris_sample = {'sepal_length': {0: 5.8, 1: 5.2, 2: 5.9, 3: 4.8, 4: 4.9}, 'sepal_width': {0: 2.7, 1: 2.7, 2: 3.0, 3: 3.0, 4: 3.0}, 'petal_length': {0: 5.1, 1: 3.9, 2: 4.2, 3: 1.4, 4: 1.4}, 'petal_width': {0: 1.9, 1: 1.4, 2: 1.5, 3: 0.1, 4: 0.2}, 'species': {0: 'virginica', 1: 'versicolor', 2: 'versicolor', 3: 'setosa', 4: 'setosa'}}
df = pd.DataFrame(iris_sample)

# your code here
print(df.describe())