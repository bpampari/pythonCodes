import csv

# Function to read afile and convert its content into a dictionary
def read_file_to_dict(file_path):
    dict = {}
    with open(file_path, 'r') as file:  # Open the file in read mode
        reader = csv.reader(file)
        for row in reader:
            key = row[0]  # The first column is used as the key
            dict[key] = row[1:]  # The rest of the columns are stored as the value (list)
    return dict  # Return the dictionary

# Function to replace values from file2 with values from file1 based on matching keys
def replace_values(file1, file2, output_file):
    file1_dict = read_file_to_dict(file1)
    with open(file2, 'r') as f2, open(output_file, 'w', newline='') as out_file:  # Open file2 for reading and output file for writing
        reader = csv.reader(f2)  # Create a CSV reader for file2
        writer = csv.writer(out_file)
        for row in reader:  # Loop through each row in file2
            key = row[0]  # Get the first column (key) from file2's row
            if key in file1_dict:  # If the key exists in file1's dictionary
                new_row = [key] + file1_dict[key]  # Replace the row with the values from file1
            else:
                new_row = row  # Otherwise, keep the original row
            writer.writerow(new_row)

# File paths for input and output
file1 = 'Path of file1'  # CSV file with data to replace values from
file2 = 'path of file2'  # CSV file where values will be replaced
output_file = 'output.txt'  # Output file for the result

replace_values(file1, file2, output_file)
