import csv

# Create a list of query ids
query_ids = ["Q1821", "Q1822", "Q1823", "Q1824", "Q1825", "Q1826"]

# Create a list of rows for the utility matrix
rows = [
    ["U_11", 3, "", 88, 3, 95, 2],
    ["U_12", 12, 50, 90, 2, 77, 10],
    ["U_13", "", "", "", 95, 1, 24],
]

# Write the query ids and rows to a CSV file
with open("utility_matrix.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(query_ids)
    writer.writerows(rows)
