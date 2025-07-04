#!usr/bin/env python3
import hashlib
import os

def calculate_md5(filename):
    """Calculates the MD5 hash of a file."""
    try:
        with open(filename, 'rb') as f:
            file_content = f.read()
            md5_hash = hashlib.md5(file_content).hexdigest()
            return md5_hash
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_directory(directory):
    """Checks files in a directory against the hash database."""
    mismatched_files = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath): #Ensure it's a file and not a directory
            hash_value = calculate_md5(filepath)
            if hash_value:
                if filename not in hash_database:
                    print(f"Warning: File '{filename}' found in directory but not in database.")
                elif hash_value != hash_database[filename]:
                    mismatched_files.append(filename)
                    print(f"Warning: Hash mismatch detected for '{filename}'.")
    return mismatched_files

# Example hash database: replace with your actual hashes
hash_database = {
    'FileYouWant.zip': '640f416675ce157ac0b6645b5a0a03dc',
}

directory_to_check = r'E:\\GithubRepos\\' # use double backslashes for Windows paths this is an example path & for linux use the /media...
mismatched = check_directory(directory_to_check)

if mismatched:
    print("\nFiles with hash mismatches:")
    for filename in mismatched:
        print(filename)
else:
    print("\nAll files in the directory match the hash database.")
