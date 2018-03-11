import read_write as rw
import data_processor

df = rw.read_statements()
categories = data_processor.enrich_categories(df)

df['Category'] = [categories[x] for x in [e.split()[0] for e in df['Description']]]

print(df.tail())