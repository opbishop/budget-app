import integration.transactions as th
import pandas as pd
from data_models.transaction import Transaction
from pprint import pprint

def enrich_categories():
    data_unenriched = th.read_statements()
    unduped_descriptions = [set(str.split()[0] for str in data_unenriched['Description'])]
    df1 = pd.Series(unduped_descriptions)

    # th.save_to_csv(uncategorised_data, 'uncategorised')
    catdf = th.read_csv('categorised')
    catdf['Description'] = [record.strip() for record in catdf['Description']]

    data_unenriched['Description'] = [record.strip() for record in data_unenriched['Description']]

    categories = catdf.set_index('Description')['Category'].to_dict()

    data_unenriched['Category'] = [categories[x.strip()] for x in [e.split()[0].strip() for e in data_unenriched['Description']]]

    transactions=[]
    for transaction in data_unenriched.to_records():
        try:
            tt = Transaction(date=transaction[1], mcc=transaction[2], description=transaction[3],
                             amount=transaction[4], category=transaction[5])
            transactions.append(tt)
        except KeyError as e:
            print(e)

    data_enriched = data_unenriched

    th.save_to_db(transactions)


    return data_enriched