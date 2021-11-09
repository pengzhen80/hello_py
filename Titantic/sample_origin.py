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
print(train_data.head(5))
test_data = pd.read_csv("./input/test.csv")
y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# print(train_data.columns)
print(X.count)
print(X_test.count)
tree_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
tree_model.fit(X, y)
predictions = tree_model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)