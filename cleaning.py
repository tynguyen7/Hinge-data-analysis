# All packages used for cleaning and analysis
import pandas as pd
import re
import json

#Import user data downlaoded from Hinge
file_path = [YOUR_FILE_PATH_HERE]

with open(file_path,'r') as file:
    match_data = json.load(file)

# Creating overarching dataframe
id = []
data = []

for index, value in enumerate(match_data):
    id.append(index)
    data.append(value)

df = pd.DataFrame({'id': id, 'data': data})

# Separating the nested dictionaries
new_rows = []

for df_index, row in df.iterrows():
    interaction_id = row['id']
    all_data = row['data']
  
# All_data is a dictionary with interaction types (match/like/chats/block) as the key and timestamp/body/comments as the value.
    for key, value in all_data.items():
        new_rows.append({'id': interaction_id, 'interaction_type': key, 'details': value})

df = pd.DataFrame(new_rows)
df.to_csv('all_data.csv', index = False)
