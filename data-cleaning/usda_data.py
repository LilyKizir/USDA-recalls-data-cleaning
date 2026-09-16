import pandas as pd

file_path = 'data-cleaning/usda_recalls.json'

df = pd.read_json(file_path)

print(df)