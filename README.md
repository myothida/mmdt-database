# mmdt-database
Instructions for setting up a home library database in Google Cloud and accessing it using SQL and Python.

# Home Library Database Setup in Google Cloud

## Overview
This repository provides step-by-step instructions for setting up a home library database in Google Cloud SQL using PostgreSQL. Students will learn how to create a database, populate it with data, and access it using SQL queries from Python.

## Prerequisites
- A Google Cloud account. Sign up at [Google Cloud Console](https://console.cloud.google.com/).
- Basic knowledge of SQL and Python.

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
3. **Create Users**:
   - Go to the **Users** tab.
   - Click on **Add User Account** to create new database users as needed.

### Step 5: Configure Access
1. **Allow Connections**:
   - Go to the **Connections** tab of your Cloud SQL instance.
   - Under **Authorized networks**, add your client IP address or the IP range that needs access.
   - Enable **Public IP** if necessary.
2. **Configure SSL (Optional)**: For secure connections, consider setting up SSL in the **SSL** tab.

### Step 6: Create a Table and Insert Data
Use the following SQL commands to create a `books` table and insert sample data:

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    published_year INT,
    genre VARCHAR(100)
);

INSERT INTO books (title, author, published_year, genre) VALUES
('1984', 'George Orwell', 1949, 'Dystopian'),
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

