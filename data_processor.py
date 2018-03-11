import read_write as rw
import pandas as pd

def enrich_categories(uncategorised_data):
    unduped_descriptions = [set(str.split()[0] for str in uncategorised_data['Description'])]
    df1 = pd.Series(unduped_descriptions)

    rw.save_to_csv(uncategorised_data, 'uncategorised')
    df = rw.read_csv('categorised')

    df['Description'] = [record.strip() for record in df['Description']]
    df_enriched = df.set_index('Description')['Category'].to_dict()
    rw.save_to_json(df_enriched, 'categorised')

    return df_enriched