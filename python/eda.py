import json
import pandas as pd


def show_data(jsonl_file):
    df = pd.read_json(jsonl_file, lines=True)
    print(df.head())
    print(df.shape)
    print(df.columns)
    print(df.info())

    print("---------------------------------")
    print(df['label'].value_counts())

def main():
    train_f = "../data/imdb/train.jsonl"
    test_f  = "../data/imdb/test.jsonl"
    dev_f   = "../data/imdb/dev.jsonl"
    
    show_data(train_f)
    show_data(test_f)
    show_data(dev_f)

main()
