import read_write as rw

def enrich_categories(uncategorised_data):
    rw.save_to_csv(uncategorised_data, 'uncategorised')
    df = rw.read_csv('categorised')
    df['Description'] = [record.replace('\'', '').strip() for record in df['Description']]
    df_enriched = df.set_index('Description')['Category'].to_dict()
    rw.save_to_json(df_enriched, 'categorised')
    return df_enriched