import os

def find_and_replace_in_file(file_path, find_replace_pairs):
    """
    Find and replace strings in a text file.

    Parameters:
        file_path (str): Path to the .txt file to be modified.
        find_replace_pairs (list of tuples): List of (find, replace) pairs.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform replacements
    for find_str, replace_str in find_replace_pairs:
        content = content.replace(find_str, replace_str)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Replacements completed in {file_path}.")

# Example usage
if __name__ == "__main__":
    file_path = "C:/2024/sam.txt"  # Replace with your Notepad++-opened file path
    # List of (find, replace) pairs
    find_replace_pairs = [
        ("123", "bbb"),
        ("456", "ddd"),
        ("789", "fff"),
       # ("123", "456"),
        # Add more pairs as needed
    ]

    find_and_replace_in_file(file_path, find_replace_pairs)
