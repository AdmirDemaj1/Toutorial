import pandas as pd

import matplotlib.pyplot as plt

housing_data = pd.read_csv('datasets/housing.csv')
housing_data.sample(5)

housing_data = housing_data.dropna()

housing_data.shape

housing_data.loc[housing_data['median_house_value'] == 500001].count()

housing_data = housing_data.drop(housing_data.loc[housing_data['median_house_value'] == 500001].index)

housing_data.loc[housing_data['median_house_value'] == 500001].count()
    

housing_data.shape

housing_data['ocean_proximity'].unique()

housing_data = pd.get_dummies(housing_data, columns=['ocean_proximity'])

housing_data.shape

housing_data.sample(5)


X = housing_data.drop('median_house_value', axis=1)
Y = housing_data['median_house_value']

X.columns

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

x_train.shape

y_train.shape

from sklearn.linear_model import LinearRegression
linear_model = LinearRegression().fit(x_train, y_train)

print("Training_score:" , linear_model.score(x_train, y_train))

predictors = x_train.columns
predictors

coef = pd.Series(linear_model.coef_, predictors).sort_values()
print(coef)

y_pred = linear_model.predict(x_test)

df_pred_actual = pd.DataFrame({'predicted': y_pred, 'actual': y_test})
df_pred_actual.head(20)

from sklearn.metrics import r2_score
print("Testing score.... :", r2_score(y_test, y_pred))

