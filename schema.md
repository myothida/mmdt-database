# Home Library SQL Schema

This SQL schema defines the tables for a home library system using PostgreSQL syntax, compatible with Google Cloud SQL.

```sql
-- Drop tables if they exist
DROP TABLE IF EXISTS loans CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS members CASCADE;

-- Create authors table
CREATE TABLE authors (
    authorid SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    biography TEXT,
    birthdate DATE
);

-- Create genres table
CREATE TABLE genres (
    genreid SERIAL PRIMARY KEY,
    genrename VARCHAR(50) NOT NULL UNIQUE
);

-- Create books table
CREATE TABLE books (
    bookid SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    authorid INT,
    genreid INT,
    publisheddate DATE,
    isbn VARCHAR(20) UNIQUE,
    pages INT,
    FOREIGN KEY (authorid) REFERENCES authors(authorid) ON DELETE SET NULL,
    FOREIGN KEY (genreid) REFERENCES genres(genreid) ON DELETE SET NULL
);

-- Create members table
CREATE TABLE members (
    memberid SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    joindate DATE NOT NULL,
    membershipstatus VARCHAR(10) CHECK (membershipstatus IN ('Active', 'Inactive')) DEFAULT 'Active'
);

-- Create loans table
CREATE TABLE loans (
    loanid SERIAL PRIMARY KEY,
    bookid INT,
    memberid INT,
    loandate DATE NOT NULL,
    returndate DATE,
    FOREIGN KEY (bookid) REFERENCES books(bookid) ON DELETE CASCADE,
    FOREIGN KEY (memberid) REFERENCES members(memberid) ON DELETE CASCADE
);

