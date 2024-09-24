# mmdt-database
Instructions for setting up a home library database in Google Cloud and accessing it using SQL and Python.

# Home Library Database Setup in Google Cloud

## Overview
This repository provides step-by-step instructions for setting up a home library database in Google Cloud SQL using PostgreSQL. Students will learn how to create a database, populate it with data, and access it using SQL queries from Python.

## Prerequisites
- A Google Cloud account. Sign up at [Google Cloud Console](https://console.cloud.google.com/).
- Basic knowledge of SQL and Python.
- Google Cloud SDK installed (optional, for command-line usage).
- CSV files for books, genres, authors, members, and loan_records.

## Steps to Set Up the Home Library Database

### Step 1: Create a Google Cloud Project
1. **Access the Console**: Go to [Google Cloud Console](https://console.cloud.google.com/).
2. **Create Project**: Click on the project dropdown in the top left corner and select **New Project**.
3. **Enter Details**: Provide a name for your project (e.g., `Home Library Database`) and click **Create**.

### Step 2: Enable the Cloud SQL API
1. Navigate to **APIs & Services** > **Library** in the Cloud Console.
2. Search for **Cloud SQL Admin API** and click **Enable**.

### Step 3: Create a Cloud SQL Instance
1. In the Cloud Console, navigate to **Databases** > **SQL**.
2. Click on **Create Instance**.
3. Choose **PostgreSQL** as the database engine.
4. **Configure Instance**:
   - **Instance ID**: Choose a unique ID (e.g., `home-library-instance`).
   - **Root Password**: Set a strong password for the default user.
   - **Region and Zone**: Select your preferred region and zone.
   - **Database Version**: Choose the desired PostgreSQL version.
5. Click **Create**.

### Step 4: Set Up the Database and Users
1. **Access the Instance**: Click on the created instance name in the SQL Instances dashboard.
2. **Create a Database**:
   - Go to the **Databases** tab.
   - Click on **Create Database** and name it (e.g., `library_db`).
3. **Create Users**: (optional)
   - Go to the **Users** tab.
   - Click on **Add User Account** to create new database users as needed.

### Step 5: Create the database schema
1. **Connect to Your Cloud SQL Instance**: Use the Cloud SQL Query Editor in the Google Cloud Console.
2. Connect using your instance’s public IP and database credentials.
3. Create the necessary tables in your database by executing the following SQL schema in the SQL instance:

-- Drop tables if they exist
DROP TABLE IF EXISTS loan_records;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS authors;

-- Create the authors table
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_year INT,
    nationality VARCHAR(100)
);

-- Create the genres table
CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create the books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT REFERENCES authors(author_id) ON DELETE CASCADE,
    published_year INT,
    genre_id INT REFERENCES genres(genre_id) ON DELETE SET NULL,
    isbn VARCHAR(20) UNIQUE,
    available_copies INT DEFAULT 1
);

-- Create the members table
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(20),
    join_date DATE DEFAULT CURRENT_DATE
);

-- Create the loan records table
CREATE TABLE loan_records (
    loan_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id) ON DELETE CASCADE,
    book_id INT REFERENCES books(book_id) ON DELETE CASCADE,
    loan_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    due_date DATE
);

### Step 6: Upload Data from CSV Files to Google Cloud SQL Using Google Cloud Console
1. **Access the Instance**: Click on the created instance name in the SQL Instances dashboard.
2. **Import CSV Data**:
   - Click on Import and provide the path to your CSV file stored in Google Cloud Storage (GCS).
   - If your files are not yet in GCS, upload them to a bucket.
3. **Import CSV Files**:
   - Specify the CSV file path (e.g., gs://your-bucket-name/authors.csv) and select the target database.
   - Click Import.
   - Follow the same process for each CSV file (authors, genres, books, members, loan_records).
