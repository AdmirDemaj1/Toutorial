import sklearn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('datasets/titanic_train.csv')
titanic_df.head(10)

titanic_df.shape


titanic_df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
titanic_df.head()


titanic_df = titanic_df.dropna()


titanic_df['Sex'] = titanic_df['Sex'].map({'male': 1, 'female': 0})

from sklearn import preprocessing

# label_encoding = preprocessing.LabelEncoder()
# titanic_df['Sex'] = label_encoding.fit_transform(titanic_df['Sex'].astype(str))

titanic_df = pd.get_dummies(titanic_df , columns=['Embarked'])

titanic_df.head()

titanic_df = titanic_df.sample(frac=1).reset_index(drop=True)
titanic_df.head()

# Calculate the correlation matrix
titanic_data_corr = titanic_df.corr()
                                                  

titanic_df.to_csv('datasets/titanic_processed.csv', index=False)

print(titanic_data_corr)

# Plot the scatter plot
fig, ax = plt.subplots(figsize=(12, 8))
plt.scatter(titanic_df['Fare'], titanic_df['Survived'])
plt.xlabel('Fare')
plt.ylabel('Survived')
plt.title('Scatter plot of Fare vs Survived')
plt.show()

