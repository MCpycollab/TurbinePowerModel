import s3fs
from s3fs.core import S3FileSystem
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

def build_train():

    s3 = S3FileSystem()
    DIR_wh = 's3://ece5984-s3-mcagle/Final_Project/Warehouse'
    X_train = np.load(s3.open('{}/{}'.format(DIR_wh, 'X_train.pkl')), allow_pickle=True)
    X_test = np.load(s3.open('{}/{}'.format(DIR_wh, 'X_test.pkl')), allow_pickle=True)
    y_train = np.load(s3.open('{}/{}'.format(DIR_wh, 'y_train.pkl')), allow_pickle=True)
    y_test = np.load(s3.open('{}/{}'.format(DIR_wh, 'y_test.pkl')), allow_pickle=True)

    # Building the Random Forrest Regression Model
    rf_regressor = RandomForestRegressor(
        n_estimators=100,  # Number of trees
        max_depth=None,  # Maximum depth of the tree
        min_samples_split=2,  # Minimum samples needed to split a node
        random_state=42  # Seed for reproducibility
    )

    # Training the model
    rf_regressor.fit(X_train, y_train)

    # Making predictions
    y_pred = rf_regressor.predict(X_test)

    DIR_outputs = "s3://ece5984-s3-mcagle/Final_Project/Warehouse/Model_Outputs"
    # Save model temporarily
    with s3.open('{}/{}'.format(DIR_outputs, 'model.pkl'), 'wb') as f:
        f.write(pickle.dumps(rf_regressor))
    with s3.open('{}/{}'.format(DIR_outputs, 'y_pred.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_pred))
    with s3.open('{}/{}'.format(DIR_outputs, 'X_tested.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_test))
    with s3.open('{}/{}'.format(DIR_outputs, 'y_tested.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_test))
    with s3.open('{}/{}'.format(DIR_outputs, 'X_trained.pkl'), 'wb') as f:
        f.write(pickle.dumps(X_train))
    with s3.open('{}/{}'.format(DIR_outputs, 'y_trained.pkl'), 'wb') as f:
        f.write(pickle.dumps(y_train))
