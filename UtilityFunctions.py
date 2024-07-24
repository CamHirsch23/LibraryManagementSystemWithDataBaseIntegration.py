import sqlite3
import re

def connect_to_db(db_filename):
    return sqlite3.connect(db_filename)

def validate_isbn(isbn):
    pattern = r'^(?:ISBN(?:-1[03])?:? )?(?=\d{10}$|(?=(?:\d+-){4})\d{13}$|97[89]\d{10}$|(?=(?:\d+-){4})\d{17}$)97[89]?\d{1,5}[- ]?\d+[- ]?\d+[- ]?\d+[- ]?\d$'
    return re.match(pattern, isbn) is not None
