import pandas as pd
import read_write
import data_processor

df = read_write.read_statements()
print(df.tail())

x = set(df['Description'])
y = [set(str.split()[0] for str in df['Description'])]
df1 = pd.Series(y)

data_processor.enrich_categories(df1)

cats = read_write.read_json('categorised')

print(cats)