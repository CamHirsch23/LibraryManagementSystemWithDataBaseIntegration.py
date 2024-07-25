"""
This module provides functions to add books, genres, users, and authors to an SQLite database.
"""

import sqlite3


def add_book(conn, title, author, isbn, publication_date):
    """
    Adds a book to the books table in the SQLite database.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO books (title, author, isbn, publication_date) VALUES (?, ?, ?, ?)",
            (title, author, isbn, publication_date)
        )
        conn.commit()
        print(f"Book '{title}' by {author} added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error adding book: {e}")


def add_genre(conn, name):
    """
    Adds a genre to the genres table in the SQLite database.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Genre '{name}' added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error adding genre: {e}")


def add_user(conn, user_id, name, email):
    """
    Adds a user to the users table in the SQLite database.
    """
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (user_id, name, email) VALUES (?, ?, ?)",
            (user_id, name, email)
        )
        conn.commit()
        print(f"User '{name}' added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error adding user: {e}")


def add_author(conn, name):
    """
    Adds an author to the authors table in the SQLite database.
    """
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()
        print(f"Author '{name}' added successfully!")
    except sqlite3.IntegrityError as e:
        print(f"Error adding author: {e}")
