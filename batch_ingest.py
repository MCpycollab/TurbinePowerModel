import s3fs
from s3fs.core import S3FileSystem
import pickle
import pandas as pd
from io import StringIO

def ingest_data():
    csv_file_path = "s3://ece5984-s3-mcagle/Final_Project/Origin/Dataset_1.csv"
    df=pd.read_csv(csv_file_path)
    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-s3-mcagle/Final_Project/Lake'                        # Insert here
    # Push data to S3 bucket as a pickle file
    with s3.open('{}/{}'.format(DIR, 'data.pkl'), 'wb') as f:
        f.write(pickle.dumps(df))