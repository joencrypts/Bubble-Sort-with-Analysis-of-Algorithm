# Bubble-Sort-with-Analysis-of-Algorithm
Students Database Management Application
Description

This Python application is designed to manage and sort student names stored in an SQLite database. It allows users to interact through a simple command-line menu to view both sorted and unsorted lists of student names. The sorting is performed using the classic Bubble Sort algorithm. Additionally, the application includes performance logging, which captures both the time taken and memory usage for sorting operations, providing insights into the efficiency of the process.
Key Features:

    Database Setup: Automatically creates an SQLite database and a table to store student names if they don't already exist.
    Data Retrieval: Fetches student names from the database and can return them either in sorted or unsorted order.
    Performance Metrics: Logs the time and memory usage involved in sorting the students to help evaluate the efficiency.
    User Interaction: Provides a simple text-based menu system for user interaction, making it easy to use.

Installation
Prerequisites

Before running this application, you need to ensure that Python 3.x is installed on your system along with the following Python packages:

    sqlite3: For database operations.
    memory_profiler: To monitor the memory usage during execution.

You can install the necessary Python package using pip:

bash

pip install memory-profiler

Setup

No additional setup is required beyond having the Python environment ready and the necessary packages installed.
Usage

To run the application, execute the following command in the terminal:

bash

python bsort.py

Upon running the application, you will be presented with a menu with the following options:

    Print Sorted List: Displays the list of students sorted alphabetically.
    Print Unsorted List: Displays the list of students as they are stored in the database.
    Exit: Closes the application.

Choose an option by entering the corresponding number when prompted.
Code Description
Functions

    setup_database(): Sets up the SQLite database and creates the necessary table.
    bubble_sort(arr): Implements the Bubble Sort algorithm to sort an array.
    get_students(sorted=False): Fetches student names from the database and optionally sorts them before returning.
    sort_and_log(): Handles user interactions and logs performance data during sorting operations.
    main(): The entry point of the application that sets up the database and starts the user interaction loop.

Modules

    sqlite3: Used for all database-related operations.
    time: Utilized to measure the execution time for performance logging.
    memory_profiler: Used to monitor and log the memory usage during the execution.

Contributing

Contributions to this project are welcome. You can enhance the sorting algorithm, add new features, or improve the user interface. For major changes, please open an issue first to discuss what you would like to change.
