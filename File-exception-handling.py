# Get the input filename from the user
filename = input("Enter the filename to read: ")

# Attempt to open and read the file with proper error handling
try:
    # Use context manager to automatically handle file closing
    with open(filename, 'r') as file:
        # Read all lines from the file into a list
        content = file.readlines()