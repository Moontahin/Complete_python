# Python File I/O and JSON Handling: Comprehensive Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides a comprehensive guide to file input/output operations and JSON handling.
We will explore:
1. Reading and writing to plain text files.
2. Working with CSV files using the csv module.
3. Handling JSON data with the json module.
4. Practical examples and real-world applications.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Example 1: Writing to a Text File
with open('data/example.txt', 'w') as text_file:
    text_file.write("Hello, Python developers!\n")
    text_file.write("Welcome to file I/O operations.")

# Example 2: Reading from a Text File
with open('data/example.txt', 'r') as file:
    content = file.read() # readlines(), readlines()
    print(content)

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

import csv

# Example 3: Writing to a CSV File
with open('data/example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 28, "New York"])
    writer.writerow(["Bob", 22, "Los Angeles"])
    writer.writerow(["Carol", 24, "Chicago"])

# Example 4: Reading from a CSV File
with open('data/example.csv', 'r') as file:
    reader = csv.reader(file)
    # for row in reader:
    #     print(row)


# Section 3: JSON Data
# --------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.

import json

# Example 5: Writing JSON to a File
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('data/data.json', 'w') as file:
    json.dump(data, file)


# Example 6: Reading JSON from a File
with open('data/data.json', 'r') as file:
    data = json.load(file)
    print(data)

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Example 7: Processing JSON Data from a File
# Suppose we have a JSON file containing multiple user records.
users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bob@example.com"}
]
with open('data/newPractice.json', 'w') as file:
    json.dump(users , file)
    
with open('data/users.json', 'w') as file:
    json.dump(users, file)

with open('data/users.json', 'r') as file:
    users = json.load(file)

# for user in users:
#         print(f"{user['name']} ({user['age']}): {user['email']}")

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)   
            data = [row for row in csv_reader]

        with open(json_file_path, mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"CSV data successfully converted to JSON and saved at: {json_file_path}")
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file_path = "data/products.csv"  
json_file_path = "data/products.json"  
csv_to_json(csv_file_path, json_file_path)

# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.
import datetime
def write_log(log_file_path, message):
    try:
        with open(log_file_path, mode='a') as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] {message}\n")
        print(f"Log message appended to {log_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")

log_file_path = "data/application.log"  # Replace with your log file path
write_log(log_file_path, "Application started.")
write_log(log_file_path, "Performed some operations.")
write_log(log_file_path, "Application closed.")
# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
