import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd

def transform_data():

    s3 = S3FileSystem()
    # S3 bucket directory (data lake)
    DIR = 's3://ece5984-s3-mcagle/Final_Project/Lake'                                    # Insert here
    # Get data from S3 bucket as a pickle file
    raw_data = np.load(s3.open('{}/{}'.format(DIR, 'data.pkl')), allow_pickle=True)
    raw_data["Date & Time Stamp"] = pd.to_datetime(df["Date & Time Stamp"])
    raw_data["Mast - 96.0m Turbulence Intensity"] = raw_data["Mast - 96.0m Turbulence Intensity"].str.rstrip('%').astype(float)
    raw_data.replace(-99.99, np.nan, inplace=True)
    raw_data.dropna(inplace=True)
    raw_data.drop_duplicates(inplace=True)
    # Push cleaned data to S3 bucket warehouse
    DIR_wh = 's3://ece5984-s3-mcagle/Final_Project/Warehouse'  # Insert here
    with s3.open('{}/{}'.format(DIR_wh, 'clean_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(raw_data))