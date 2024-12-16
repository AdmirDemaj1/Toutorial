import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the processed Titanic dataset
titanic_df = pd.read_csv('datasets/titanic_processed.csv')

# Split the data into features (X) and target (Y)
X = titanic_df.drop('Survived', axis=1)
Y = titanic_df['Survived']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Train the Logistic Regression model
logistic_model = LogisticRegression(penalty='l2', C=1.0, solver='liblinear').fit(x_train, y_train)

# Make predictions on the test set
y_pred = logistic_model.predict(x_test)

# Create a DataFrame to compare actual and predicted values
pred_results = pd.DataFrame({'Y_TEST': y_test, 'Y_PRED': y_pred})

# Calculate metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("accuracy_score:", acc)
print("precision_score:", prec)
print("recall_score:", recall)

# Count the occurrences of actual vs predicted
counts = pd.DataFrame({
    'Actual': pred_results['Y_TEST'].value_counts(),
    'Predicted': pred_results['Y_PRED'].value_counts()
}).fillna(0)

# Plotting the counts of actual vs predicted
counts.plot(kind='bar', figsize=(10, 6))
plt.title('Predicted vs Actual Survival Counts')
plt.xlabel('Survived (0: No, 1: Yes)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(['Actual', 'Predicted'], loc='upper right')
plt.grid(axis='y')
plt.show()
