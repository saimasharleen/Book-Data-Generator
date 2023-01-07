import os
import user
import query
import utility_matrix
def generate_book_table(books):
    # Create a list of field names
    fields = ["book_id", "title", "author","language_code", "year_published", "num_pages", "publisher", "genre"]
    # Create a list to store the rows of the table
    rows = []
    # Add the field names as the first row
    rows.append(",".join(fields))
    # Add a row for each book
    for book in books:
        row = []
        for field in fields:
            row.append(str(book[field]))
        rows.append(",".join(row))
    # Return the table as a string
    return "\n".join(rows)

books = [
    {   "book_id": 9780743273565,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "language_code": "eng",
        "year_published": 1925,
        "num_pages": 180,
        "publisher": "Scribner's Sons",
        "genre": "Tragedy"
    },
    {   "book_id": 9780061120084,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "language_code": "eng",
        "year_published": 1960,
        "num_pages": 324,
        "publisher": "J. B. Lippincott & Co.",
        "genre": "Fiction"
    },
    {"book_id": 9780590353427,
     "title": "Harry Potter and the Philosopher's Stone",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 1997,
     "num_pages": 223,
     "publisher": "Bloomsbury",
     "genre": "Fantasy"
     },
    {"book_id": 9780439064866,
     "title": "Harry Potter and the Chamber of Secrets",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 1998,
     "num_pages": 251,
     "publisher": "Bloomsbury",
     "genre": "Fantasy"
     },
    {"book_id": 9780439136365,
     "title": "Harry Potter and the Prisoner of Azkaban",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 1999,
     "num_pages": 317,
     "publisher": "Bloomsbury",
     "genre": "Fantasy"
     },
    {"book_id": 9780439139601,
     "title": "Harry Potter and the Goblet of Fire",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2000,
     "num_pages": 636,
     "publisher": "Bloomsbury",
     "genre": "Fantasy"
     },
    {"book_id": 9780439358071,
     "title": "Harry Potter and the Order of the Phoenix",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2003,
     "num_pages": 766,
     "publisher": "Bloomsbury",
     "genre": "Fantasy"
     },
    {"book_id": 9780316228532,
     "title": "The Casual Vacancy",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2012,
     "num_pages": 503,
     "publisher": "Little, Brown and Company",
     "genre": "Fiction"
     },
    {"book_id": 9780316206830,
     "title": "The Cuckoo's Calling",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2013,
     "num_pages": 455,
     "publisher": "Mulholland Books",
     "genre": "Crime"
     },
    {"book_id": 9780316206847,
     "title": "The Silkworm",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2014,
     "num_pages": 455,
     "publisher": "Mulholland Books",
     "genre": "Crime"
     },
    {"book_id": 9780316206854,
     "title": "Career of Evil",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2015,
     "num_pages": 453,
     "publisher": "Mulholland Books",
     "genre": "Crime"
     },
    {"book_id": 9780316206861,
     "title": "Lethal White",
     "author": "J.K. Rowling",
     "language_code": "eng",
     "year_published": 2018,
     "num_pages": 624,
     "publisher": "Mulholland Books",
     "genre": "Crime"
     },
    {"book_id": 9781501110362,
     "title": "It Ends with Us",
     "author": "Colleen Hoover",
     "language_code": "eng",
     "year_published": 2016,
     "num_pages": 384,
     "publisher": "Atria Books",
     "genre": "Romance"
     },
    {"book_id": 9781476712079,
     "title": "Hopeless",
     "author": "Colleen Hoover",
     "language_code": "eng",
     "year_published": 2012,
     "num_pages": 368,
     "publisher": "Atria Books",
     "genre": "New Adult"
     },
    {"book_id": 9781476712048,
     "title": "Maybe Now",
     "author": "Colleen Hoover",
     "language_code": "eng",
     "year_published": 2013,
     "num_pages": 343,
     "publisher": "Atria Books",
     "genre": "New Adult"
     },
    {"book_id": 9781476712062,
     "title": "Losing Hope",
     "author": "Colleen Hoover",
     "language_code": "eng",
     "year_published": 2014,
     "num_pages": 358,
     "publisher": "Atria Books",
     "genre": "New Adult"
     },
    {"book_id": 9781476712079,
     "title": "Ugly Love",
     "author": "Colleen Hoover",
     "language_code": "eng",
     "year_published": 2014,
     "num_pages": 368,
     "publisher": "Atria Books",
     "genre": "New Adult"
     }
]
# This code will generate a table
book_table = generate_book_table(books)
print(book_table)
# write this string to a file by using the write method of a file object.
# This will write the book_table string to a file called "book_table.csv" in the current working directory.
with open("book_table.csv", "w") as f:
    f.write(book_table)
exec(open('user.py').read())
os.system('python user.py')
exec(open('query.py').read())
os.system('python query.py')
exec(open('utility_matrix.py').read())
os.system('python utility_matrix.py')