import sqlite3
from faker import Faker

# Database setup and creation of the students table
def setup_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS students (name TEXT)')
    conn.commit()
    conn.close()

# Generating dummy data using Faker
def generate_dummy_data():
    fake = Faker()
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('DELETE FROM students')  # Clear existing data to avoid duplicates
    for _ in range(1000):  # Generate and insert 1000 dummy names
        c.execute('INSERT INTO students (name) VALUES (?)', (fake.name(),))
    conn.commit()
    conn.close()

def main():
    setup_database()
    generate_dummy_data()
    print("1000 dummy student names have been inserted into the database.")

if __name__ == "__main__":
    main()
