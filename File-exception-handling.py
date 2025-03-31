# Get the input filename from the user
filename = input("Enter the filename to read: ")

# Attempt to open and read the file with proper error handling
try:
    # Use context manager to automatically handle file closing
    with open(filename, 'r') as file:
        # Read all lines from the file into a list
        content = file.readlines()

# Handle specific exceptions that might occur during file reading
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except IsADirectoryError:
    print(f"Error: '{filename}' is a directory, not a file.")
except Exception as e:  # Catch-all for unexpected errors
    print(f"An unexpected error occurred while reading the file: {e}")

# If file reading is successful, process the content
else:
    # Convert all lines to uppercase using list comprehension
    modified_content = [line.upper() for line in content]
    
    # Define the output directory path
    modified_dir = "assets/modified"


# Create the new filename structure:
# Extract base filename from potential path (e.g., "data/example.txt" -> "example.txt")
base_name = os.path.basename(filename)