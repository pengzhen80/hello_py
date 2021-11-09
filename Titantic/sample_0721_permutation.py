# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import eli5
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
from sklearn.ensemble import RandomForestClassifier
train_data = pd.read_csv("./input/train.csv")

###permutation importance:
from sklearn.model_selection import train_test_split

y_permut = train_data["Survived"] # Convert from string "Yes"/"No" to binary
basefeatures = ['PassengerId','Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
X_permut = train_data[basefeatures].copy()
# print(X_permut.head(5))
####preprocess

##for categories
# from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
X_permut['Name'] = class_le.fit_transform(X_permut['Name'].values)
X_permut['Sex'] = class_le.fit_transform(X_permut['Sex'].values)
X_permut['Cabin'] = class_le.fit_transform(X_permut['Cabin'].astype(str).values)
X_permut['Embarked'] = class_le.fit_transform(X_permut['Embarked'].values)
X_permut['Ticket'] = class_le.fit_transform(X_permut['Ticket'].values)
# print(X_permut.head(10))
####

##for null
from sklearn.impute import SimpleImputer
cols_with_missing_X_permut = [col for col in X_permut.columns
                     if X_permut[col].isnull().any()]
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
for col in cols_with_missing_X_permut:
    imputer = imputer.fit(X_permut[[col]])
    X_permut[[col]] = imputer.transform(X_permut[[col]])
# print(X_permut.head(10))
###

train_X_permut, val_X_permut, train_y_permut, val_y_permut = train_test_split(X_permut,y_permut, random_state=1)
permut_model = RandomForestClassifier(n_estimators=50, random_state=1).fit(train_X_permut, train_y_permut)

from sklearn.inspection import permutation_importance

perm = permutation_importance(permut_model, val_X_permut, val_y_permut,n_repeats=30,random_state=0)

important_features=[]

for i in perm.importances_mean.argsort()[::-1]:
    if perm.importances_mean[i] - 2 * perm.importances_std[i] > 0:
        important_features.append(train_data.columns[i])
        print(f"{train_data.columns[i]:<8}"
              f"{perm.importances_mean[i]:.3f}"
             f" +/- {perm.importances_std[i]:.3f}")

# import eli5
# from eli5.sklearn import PermutationImportance

# perm = PermutationImportance(permut_model, random_state=1).fit(val_X_permut, val_y_permut)
# eli5.show_weights(perm, feature_names = val_X_permut.columns.tolist())
#############
print(important_features)
important_features.remove('Survived')

test_data = pd.read_csv("./input/test.csv")
y = train_data['Survived']

# features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[important_features])
X_test = pd.get_dummies(test_data[important_features])
# print(train_data.columns)

print(X.count)
print(X_test.count)
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)

##for null
cols_with_missing_X_test = [col for col in X_test.columns if X_test[col].isnull().any()]
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
for col in cols_with_missing_X_test:
    imputer = imputer.fit(X_test[[col]])
    X_test[[col]] = imputer.transform(X_test[[col]])
# print(X_permut.head(10))
###
print(X_test.count)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)