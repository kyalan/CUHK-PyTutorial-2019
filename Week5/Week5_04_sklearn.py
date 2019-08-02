import os
os.chdir('C:/Users/user/Documents/CUHKPyTutorial2019-20190711T013955Z-001/CUHKPyTutorial2019/Week5')

import pandas as pd
df = pd.read_csv('train.csv')

print("The dataset contains ", df.shape[0], "rows of data.")
print("And also the columns are the following:/n")
print(df.info())
print()
print("And some samples:")
print(df.sample(5))

df['Age'] = df.Age.fillna(df.Age.mean()) # the mean
df['Cabin'] = df.Cabin.fillna('Unknown')
df['Embarked'] = df.Embarked.fillna(df['Embarked'].value_counts().index[0]) # the most frequent one
df.info()
df.describe()

# Set Regressor and Response Variables
regressors_num = ['Age', 'SibSp', 'Parch', 'Fare']
regressors_cat = ['Pclass', 'Sex', 'Embarked']
response = 'Survived'

# preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), regressors_num),
        ('cat', OneHotEncoder(handle_unknown='ignore'), regressors_cat)]
)
X = preprocessor.fit_transform(df)
y = df[response]

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression
model_logReg = LogisticRegression()
model_logReg.fit(X, y)
print('Logistic Model Accuracy =', model_logReg.score(X, y))

# Decision Tree Model
from sklearn.tree import DecisionTreeClassifier
model_dtree = DecisionTreeClassifier()
model_dtree.fit(X, y)
print('Decision Tree Model Accuracy =', model_dtree.score(X, y))