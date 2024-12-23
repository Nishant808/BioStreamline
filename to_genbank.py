from retrieval import ID
import os
import Bio

# Ensure Bio.Entrez.email is set
Bio.Entrez.email = 'nishantthalwal@gmail.com'

# Default folder name
folder_path = "GenBankFiles"

# Check if the folder exists; if not, create it
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the save function
def save_genbank():
    # Read IDs from the ID.txt file
    with open('ID.txt', 'r') as id_file:
        ids = [line.strip() for line in id_file.readlines()]

    # Fetch and save GenBank files
    for i in ids:  # Loop through the list of IDs
        # Fetch GenBank data
        with Bio.Entrez.efetch(db='nucleotide', id=i, rettype="gb", retmode="text") as handle:
            genbank_data = handle.read()

        # Define the file name and path
        file_name = f"{i}.gb"
        file_path = os.path.join(folder_path, file_name)

        # Save the GenBank data to the specified folder
        with open(file_path, "w") as file:
            file.write(genbank_data)

        print(f"Saved GenBank file for ID {i} to {file_path}")
