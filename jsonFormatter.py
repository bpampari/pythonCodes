# this program is to read the txt file which have unformatted JSON and format/beautify them in the same file.
import json
import os

# Specify the folder where the .txt files are located
directory = "Directory Path where files are located"

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Process only .txt files
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)

        # Open the file for reading its content
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                content = json.loads(file.read())  # Attempt to read and parse the content as JSON
            except json.JSONDecodeError as e:  # Handle any JSON parsing errors
                print(f"Error decoding JSON in file {filename}: {e}")  # Print an error message and continue
                continue  # Skip to the next file if there's an error

        # Open the file again for writing, to format and save the JSON
        with open(filepath, 'w', encoding='utf-8') as file:
            # Write the content back to the file, formatted as pretty-printed JSON
            json.dump(content, file, indent=4, ensure_ascii=False)  # Format with 4-space indentation and ensure ASCII characters are preserved
