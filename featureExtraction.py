import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def feature_extract():

    s3 = S3FileSystem()
    # S3 bucket directory (data warehouse)
    DIR_wh = 's3://ece5984-s3-mcagle/Final_Project/Warehouse'                                 # Insert here
    data = np.load(s3.open('{}/{}'.format(DIR_wh, 'clean_data.pkl')), allow_pickle=True)
    target_data = data["Turbine Power"]
    features = data.drop(columns=["Turbine Power","Date & Time Stamp"])
    scaler = MinMaxScaler()
    feature_transform = scaler.fit_transform(features)
    feature_transform = pd.DataFrame(columns=features.columns, data=feature_transform, index=features.index)
    X_train, X_test, y_train, y_test = train_test_split(feature_transform, target_data, test_size=0.2)
    # Push extracted features to data warehouse
    with s3.open('{}/{}'.format(DIR_wh, 'X_train.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_wh, 'X_test.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_wh, 'y_train.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
    with s3.open('{}/{}'.format(DIR_wh, 'y_test.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))