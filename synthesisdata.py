import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate authors data
def generate_authors(num):
    authors = []
    for _ in range(num):
        authors.append({
            'authorid': _ + 1,
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'biography': fake.text(max_nb_chars=200),
            'birthdate': fake.date_of_birth(minimum_age=20, maximum_age=90)
        })
    return authors

# Function to generate genres data
def generate_genres(num):
    genres = set()
    while len(genres) < num:
        genres.add(fake.word())
    return [{'genreid': i + 1, 'genrename': genre} for i, genre in enumerate(genres)]

# Function to generate books data
def generate_books(num, author_ids, genre_ids):
    books = []
    for _ in range(num):
        books.append({
            'bookid': _ + 1,
            'title': fake.catch_phrase(),
            'authorid': random.choice(author_ids),
            'genreid': random.choice(genre_ids),
            'publisheddate': fake.date_this_century(),
            'isbn': fake.isbn13(),
            'pages': random.randint(100, 1000)
        })
    return books

# Function to generate members data
def generate_members(num):
    members = []
    for _ in range(num):
        members.append({
            'memberid': _ + 1,
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'email': fake.email(),
            'joindate': fake.date_this_decade(),
            'membershipstatus': random.choice(['Active', 'Inactive'])
        })
    return members

# Function to generate loans data
def generate_loans(num, book_ids, member_ids):
    loans = []
    for _ in range(num):
        loans.append({
            'loanid': _ + 1,
            'bookid': random.choice(book_ids),
            'memberid': random.choice(member_ids),
            'loandate': fake.date_this_year(),
            'returndate': fake.date_this_year()
        })
    return loans

# Number of rows to generate
num_rows = 100

# Generate data
authors_data = generate_authors(num_rows)
genres_data = generate_genres(num_rows)
author_ids = [author['authorid'] for author in authors_data]
genre_ids = [genre['genreid'] for genre in genres_data]
books_data = generate_books(num_rows, author_ids, genre_ids)
members_data = generate_members(num_rows)
member_ids = [member['memberid'] for member in members_data]
loans_data = generate_loans(num_rows, [book['bookid'] for book in books_data], member_ids)

# Create DataFrames
authors_df = pd.DataFrame(authors_data)
genres_df = pd.DataFrame(genres_data)
books_df = pd.DataFrame(books_data)
members_df = pd.DataFrame(members_data)
loans_df = pd.DataFrame(loans_data)

# Save DataFrames to CSV files
authors_df.to_csv('authors.csv', index=False)
genres_df.to_csv('genres.csv', index=False)
books_df.to_csv('books.csv', index=False)
members_df.to_csv('members.csv', index=False)
loans_df.to_csv('loans.csv', index=False)

print("CSV files generated successfully!")
