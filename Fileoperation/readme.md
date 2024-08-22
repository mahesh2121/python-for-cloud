1.1 Understanding File Paths

Files can be stored in various locations on your computer, and Python allows you to specify the location using file paths:

    Absolute Path: Complete path from the root directory. Example: C:/Users/Mahesh/Documents/file.txt
    Relative Path: Path relative to the current working directory. Example: Documents/file.txt


     Opening a File

To work with a file, you first need to open it using the open() function.

file = open('example.txt', 'r')


Closing a File

It's crucial to close the file after you're done working with it to free up resources.

file.close()
