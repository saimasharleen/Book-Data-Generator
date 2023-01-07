def generate_query_set(data):
    query_set = []
    for query_id, attributes in data.items():
        query_string = f"{query_id},"
        for attribute, value in attributes.items():
            query_string += f"{attribute}={value},"
        query_set.append(query_string[:-1])
    return "\n".join(query_set)

data = {
    "Q1821": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    "Q1822": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    "Q1823": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    "Q1824": {
        "title": "Maybe Now",
        "author": "Colleen Hoover"
    },
    "Q1825": {
        "title": "Losing Hope",
        "author": "Colleen Hoover"
    },
    "Q1826": {
        "title": "Ugly Love",
        "author": "Colleen Hoover"
    },
    "Q1827": {
        "title": "Harry Potter and the Order of the Phoenix",
        "author": "J.K. Rowling"
    },
    "Q1828": {
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling"
    }

}
# This code will generate a query set
query_set = generate_query_set(data)
print(query_set)
# write the query_set string to a file called "query_set.csv" in the current working directory.
with open("query_set.csv", "w") as f:
    f.write(query_set)