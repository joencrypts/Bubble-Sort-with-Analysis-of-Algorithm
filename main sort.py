import sqlite3
import time
from memory_profiler import memory_usage

# Database setup and creation of the students table
def setup_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS students (name TEXT)')
    conn.commit()
    conn.close()

# Bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# Retrieve students from the database
def get_students(sorted=False):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT name FROM students')
    students = [row[0] for row in c.fetchall()]
    conn.close()

    if sorted:
        bubble_sort(students)
    
    return students

# Main function to sort students and log performance
def sort_and_log():
    while True:
        print("\nMenu:")
        print("1 - Print Sorted List")
        print("2 - Print Unsorted List")
        print("0 - Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            start_time = time.time()
            mem_usage_before = memory_usage()[0]
            students = get_students(sorted=True)
            mem_usage_after = memory_usage()[0]
            end_time = time.time()
            print("\nSorted Students:")
            print("\n".join(students))
            print(f"Time taken: {end_time - start_time:.6f} seconds")
            print(f"Memory used: {mem_usage_after - mem_usage_before:.6f} MB\n")
        elif choice == '2':
            students = get_students(sorted=False)
            print("\nUnsorted Students:")
            print("\n".join(students))
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

# Running the full program
def main():
    setup_database()
    sort_and_log()

if __name__ == "__main__":
    main()
