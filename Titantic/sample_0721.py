import pandas as pd
from IPython.display import display
from scipy.sparse import data
from matplotlib import pyplot as plt

data = pd.read_csv('./input/train.csv')

features = ["Pclass", "Sex", "SibSp", "Parch",'Survived']
X_permut = data[features]

##for categories
# from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
X_permut['Sex'] = class_le.fit_transform(X_permut['Sex'].values)
# print(X_permut.head(10))
####

##for null
from sklearn.impute import SimpleImputer
import numpy as np
cols_with_missing_X_permut = [col for col in X_permut.columns
                     if X_permut[col].isnull().any()]
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
for col in cols_with_missing_X_permut:
    imputer = imputer.fit(X_permut[[col]])
    X_permut[[col]] = imputer.transform(X_permut[[col]])
# print(X_permut.head(10))
###

# Create training and validation splits
df_train = X_permut.sample(frac=0.7, random_state=0)
df_valid = X_permut.drop(df_train.index)
display(df_train.head(4))

# Scale to [0, 1]
max_ = df_train.max(axis=0)
min_ = df_train.min(axis=0)
df_train = (df_train - min_) / (max_ - min_)
df_valid = (df_valid - min_) / (max_ - min_)

# Split features and target
X_train = df_train.drop('Survived', axis=1)
X_valid = df_valid.drop('Survived', axis=1)
y_train = df_train['Survived']
y_valid = df_valid['Survived']

print(X_train.shape)

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[features.count]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])

model.compile(
    optimizer='adam',
    loss='mae',
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=10,
)

import pandas as pd

# convert the training history to a dataframe
history_df = pd.DataFrame(history.history)
# use Pandas native plot method
history_df['loss'].plot();
# plt.show()

from tensorflow import keras
from tensorflow.keras import layers
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])