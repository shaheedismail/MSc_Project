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

    asin_brand = []
    for file in tqdm(file_list):
        dataset_meta = []
        if file[-2:] == 'gz' and 'meta_' in file:
            with gzip.open(file) as f:
                print(file)
                for i, l in enumerate(f):
                    dataset_meta.append(json.loads(l.strip()))
                    #if i < 10:
                        #continue
                    #else:
                        #break

        for item in dataset_meta:
            try:
                brand = item['brand']
                asin = item['asin']
                category = item['category']
            except KeyError:
                brand='nobrand'
            asin_brand.append((brand, asin, category))

    df_meta = pd.DataFrame(asin_brand, columns = ['brand', 'asin', 'category'])
    df_meta.to_csv('meta.csv', index=False)

