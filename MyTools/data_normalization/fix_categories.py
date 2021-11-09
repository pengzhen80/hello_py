from sklearn.preprocessing import LabelEncoder

def fix_categories(data,features):
    class_le = LabelEncoder()
    for feature in features:
        data['Cabin'] = class_le.fit_transform(data['Cabin'].astype(str).values)
    return data  