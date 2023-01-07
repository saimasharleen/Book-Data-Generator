import csv

# Define the user ids
user_ids = ["U_1", "U_2", "U_3", "U_4", "U_5", "U_6", "U_7", "U_8", "U_9", "U_10", "U_11", "U_12", "U_13", "U_14", "U_15", "U_16", "U_17", "U_18", "U_19", "U_20"]

# Create a list of dictionaries representing the rows of the CSV file
rows = []
for user_id in user_ids:
    rows.append({"user_id": user_id})

# Write the rows to a CSV file
with open("user_ids.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["user_id"])
    writer.writeheader()
    writer.writerows(rows)