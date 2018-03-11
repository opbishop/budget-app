import os
import json
import pandas as pd
from config import config
from pprint import pprint


def save_to_json(obj, fp):
    with open('{}/{}.json'.format(config['data'], fp), 'w') as fp:
        json.dump(obj, fp)
    fp.close()


def read_json(fp):
    try:
        with open('{}/{}.json'.format(config['data'], fp), 'r') as fp:
            return json.load(fp)
    except FileNotFoundError as e:
        print(e)


def read_statements():
    files = os.listdir(config['statement_data'])
    df = pd.read_csv('{}/{}'.format(config['statement_data'], files[0]))
    for file in files[1:]:
        df = df.append(pd.read_csv('{}/{}'.format(config['statement_data'], file)), ignore_index=True)
    return df


def save_to_csv(obj, fp):
    obj.to_csv('data/{}.csv'.format(fp))


def read_csv(fp):
    try:
        with open('{}/{}.csv'.format(config['data'], fp), 'r') as fp:
            return pd.read_csv(fp)
    except FileNotFoundError as e:
        print(e)
