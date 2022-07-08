import os
import json
import gzip
import pandas as pd
from pathlib import Path
import numpy as np

def json_to_list(file):
    data = []
    with gzip.open(file) as f:
        for l in f:
            data.append(json.loads(l.strip()))
    return data

def list_to_csv(data):
    df = pd.DataFrame.from_dict(data)
    return df


def files_in_directory(dir):
    files = []
    productnames =[]
    for file in os.listdir(dir):
        f = os.path.join(dir, file)
        product = file.split('.')[0]
        if os.path.isfile(f):
            files.append(f)
            productnames.append(product)
    return files, productnames


if __name__ == '__main__':
    list, names = files_in_directory('gz files')
    i = 0
    root = 'csv files raw'
    for line in list:
        data = json_to_list(line)
        df = list_to_csv(data)
        df['sentimentMulti'] = round((df['overall'] - 3.0) / 2.0, 0)
        df['sentimentBinary'] = np.where(df['sentimentMulti']!=-1, 1, -1)
        df_new = df[['reviewText', 'sentimentMulti', 'sentimentBinary']]
        filename = names[i]+'.csv'
        df_new.to_csv(root+'/'+filename)
        i=+1


