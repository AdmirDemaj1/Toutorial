import pandas as pd

import matplotlib.pyplot as plt

housing_data = pd.read_csv('datasets/housing.csv')
housing_data.sample(5)

housing_data = housing_data.dropna()

housing_data.loc[housing_data['median_house_value'] == 500001].count()

housing_data = housing_data.drop(housing_data.loc[housing_data['median_house_value'] == 500001].index)

housing_data.loc[housing_data['median_house_value'] == 500001].count()

housing_data.head()

housing_data = pd.get_dummies(housing_data, columns=['ocean_proximity'])

housing_data.shape

housing_data.sample(5)

median = housing_data['median_house_value'].median()

median

housing_data['above_median'] = (housing_data['median_house_value'] - median) > 0

housing_data.sample(5)


columns_to_convert = ['ocean_proximity_<1H OCEAN', 'ocean_proximity_INLAND',
                      'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY',
                      'ocean_proximity_NEAR OCEAN']

housing_data[columns_to_convert] = housing_data[columns_to_convert].astype(int)


housing_data.sample(5)

X = housing_data.drop(['median_house_value', 'above_median'], axis=1)
Y = housing_data['above_median']

X.columns

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

x_train.shape, x_test.shape

y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression(solver='liblinear').fit(x_train, y_train)

print("Training_score: ", logistic_model.score(x_train, y_train))

y_pred = logistic_model.predict(x_test)

df_pred_actual = pd.DataFrame({'predicted': y_pred, 'actual': y_test})
df_pred_actual.head(10)

from sklearn.metrics import accuracy_score
print("Testing_score:", accuracy_score(y_test, y_pred))

