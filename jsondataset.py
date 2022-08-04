import os
import json
import gzip
import pandas as pd
from pathlib import Path
import numpy as np
from tqdm import tqdm

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
    file_list, _ = files_in_directory('AmazonData')
    dataset=[]
    for file in tqdm(file_list):
        if file[-2:] == 'gz' and 'meta_' not in file:
            with gzip.open(file) as f:
                for i, l in enumerate(f):
                    dataset.append(json.loads(l.strip()))
                    if i < 1: continue
                    else: break
    df = pd.DataFrame.from_dict(dataset)
    df.to_csv('Datasetjson.csv', index=False)

