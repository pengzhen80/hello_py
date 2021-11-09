from sklearn.impute import SimpleImputer
import numpy as np
def ClearNullData(data):
  cols_with_missing_data = [col for col in data.columns
                     if data[col].isnull().any()]
  imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
  for col in cols_with_missing_data:
    imputer = imputer.fit(data[[col]])
    data[[col]] = imputer.transform(data[[col]])
  return data