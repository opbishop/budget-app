import integration.transactions as th
from service import data_processor

print(th.empty_db())
print(data_processor.enrich_categories())