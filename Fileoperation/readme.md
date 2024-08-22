
# Python File Handling Tutorial

## 1. Understanding File Paths

Files can be stored in various locations on your computer, and Python allows you to specify the location using file paths:

- **Absolute Path**: Complete path from the root directory. Example: `C:/Users/Mahesh/Documents/file.txt`
- **Relative Path**: Path relative to the current working directory. Example: `Documents/file.txt`

### Opening a File

To work with a file, you first need to open it using the `open()` function.

```python
file = open('example.txt', 'r')
```

### Closing a File

It's crucial to close the file after you're done working with it to free up resources.

```python
file.close()
```

Using the `with` statement is the recommended way to open and close files automatically.

```python
with open('example.txt', 'r') as file:
    content = file.read()
```

## 2. Reading Files

### 2.1 Reading the Entire File

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### 2.2 Reading Line by Line

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
```

### 2.3 Reading Specific Number of Characters

```python
with open('example.txt', 'r') as file:
    content = file.read(10)  # reads the first 10 characters
    print(content)
```

## 3. Writing to Files

### 3.1 Writing Text to a File

```python
with open('example.txt', 'w') as file:
    file.write("Hello, world!")
```

### 3.2 Appending Text to a File

```python
with open('example.txt', 'a') as file:
    file.write("\nWelcome to Python!")
```

## 4. Working with Different File Types

### 4.1 Handling CSV Files

CSV files are common for storing tabular data. Python’s `csv` module is useful for working with them.

#### 4.1.1 Reading CSV Files

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

#### 4.1.2 Writing to CSV Files

```python
import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Mahesh", "30", "Mumbai"])
```

### 4.2 Handling JSON Files

JSON is a popular format for data exchange. Python’s `json` module helps in working with JSON files.

#### 4.2.1 Reading JSON Files

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

#### 4.2.2 Writing to JSON Files

```python
import json

data = {
    "name": "Mahesh",
    "age": 30,
    "city": "Mumbai"
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
```

### 4.3 Handling Excel Files

Excel files are commonly used for spreadsheets. The `pandas` library can handle Excel files.

#### 4.3.1 Reading Excel Files

```python
import pandas as pd

data = pd.read_excel('data.xlsx')
print(data)
```

#### 4.3.2 Writing to Excel Files

```python
import pandas as pd

data = {
    'Name': ['Mahesh', 'Suresh'],
    'Age': [30, 28],
    'City': ['Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
```

## 5. Advanced File Handling Techniques

### 5.1 Handling Large Files

Reading large files can consume a lot of memory. Processing them in chunks is more efficient.

#### 5.1.1 Reading in Chunks

```python
with open('largefile.txt', 'r') as file:
    while chunk := file.read(1024):  # Reads 1024 bytes at a time
        print(chunk)
```

### 5.2 File Operations

#### 5.2.1 Renaming and Deleting Files

The `os` module provides utilities for file operations.

```python
import os

# Renaming a file
os.rename('example.txt', 'newname.txt')

# Deleting a file
os.remove('newname.txt')
```

#### 5.2.2 Working with Directories

```python
import os

# Creating a directory
os.mkdir('new_folder')

# Listing files in a directory
files = os.listdir('new_folder')
print(files)

# Deleting a directory
os.rmdir('new_folder')
```

## 6. Handling Binary Files

Binary files include images, videos, and other non-text data.

### 6.1 Reading and Writing Binary Files

#### 6.1.1 Reading Binary Files

```python
with open('image.png', 'rb') as file:
    data = file.read()
```

#### 6.1.2 Writing Binary Files

```python
with open('copy_image.png', 'wb') as file:
    file.write(data)
```

## 7. Exception Handling in File Operations

Handling errors that might occur during file operations is crucial.

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
```
