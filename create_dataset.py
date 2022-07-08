from Data_preparation import files_in_directory
import pandas as pd

def create_dataset_binary(files, records):
    sentiment = 'sentimentBinary'
    for file in files:
        df = pd.read_csv(file)
        df_pos = df[df[sentiment]==1]
        df_pos = df_pos.head(records/2)
        df_neg = df[df[sentiment]==-1]
        df_neg = df_neg.head(records/2)
        df_new = pd.concat([df_pos, df_neg])
    return df_new

if __name__ == '__main__':
    create_dataset_binary(files_in_directory('csv files raw'), 100000).to_csv('dataset.csv')

