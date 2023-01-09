import pandas as pd

# Read in the existing data CSV file
df = pd.read_csv('Book_final.csv')

# Create an empty DataFrame to store the query set data
query_set = pd.DataFrame(columns=['query_id', 'conditions'])

# Iterate over the rows in the original DataFrame
for index, row in df.iterrows():
    # Extract the query id and conditions for each row
    query_id = row['query_id']
    conditions = row.drop(['query_id']).to_dict()

    # Append the query id and conditions to the new DataFrame as a new row
    query_set = query_set.append({'query_id': query_id, 'conditions': conditions}, ignore_index=True)

# Write the new DataFrame to a CSV file
query_set.to_csv('query_sets.csv', index=False)
