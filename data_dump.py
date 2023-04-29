import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATAPATH_FILE="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME='aps'
COLLECTION_NAME='sensor'
if __name__=='__main__':
    df=pd.read_csv(DATAPATH_FILE)
    print(f"number of rows and columns:{df.shape}")


# drop the index in df and then convert into json format before inserting to mongodb
# inplace=true (dataset make changes in same memory location)
df.reset_index(drop=True, inplace=True)

json_record= list(json.loads(df.T.to_json()).values())
print(json_record[0])
 
 # insert converted json record to MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

