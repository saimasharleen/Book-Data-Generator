import csv
import random

# Generate a list of 100 unique query IDs
query_ids = ['Q' + str(i) for i in range(5001)]

# Generate a list of possible attribute names and values
attributes = ['author', 'language', 'genre', 'year', 'title']
values = ['mcgill', 'eng', 'Tragedy', '2020', 'The Tempest']

# Create an empty list to store the queries
queries = []

# Generate 100 queries
for query_id in query_ids:
  # Create an empty list to store the conditions for this query
  conditions = []
  # Choose a random number of attributes for this query
  num_attributes = random.randint(1, len(attributes))
  # Choose a random subset of the attributes
  chosen_attributes = random.sample(attributes, num_attributes)
  # Generate a condition for each chosen attribute
  for attribute in chosen_attributes:
    # Choose a random value for this attribute
    value = random.choice(values)
    # Add the condition to the list of conditions
    conditions.append(attribute + '=' + value + '')
  # Join the conditions into a single string separated by commas
  conditions_str = ','.join(conditions)
  # Add the query to the list of queries
  queries.append([query_id, conditions_str])

# Write the queries to a CSV file
with open('queries.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerows(queries)
