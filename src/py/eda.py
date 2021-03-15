import json
import pandas as pd

datapath = '../../data/02-acl-arc/'

def show_data(jsonl_file):
    df = pd.read_json(jsonl_file, lines=True)
    print(df.head())
    print(df.shape)
    print(df.columns)
    print(df.info())

    print("---------------------------------")
    print(df['label'].value_counts())

def main():
    train_f = datapath + 'train.jsonl'
    test_f  = datapath + 'test.jsonl'
    dev_f   = "../data/imdb/dev.jsonl"
    
    show_data(train_f)
    show_data(test_f)
    show_data(dev_f)

main()
