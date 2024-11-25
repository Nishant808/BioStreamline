from retrieval import ID
import os
import Bio


# Define the save function
def save_genbank():
    # Ensure Bio.Entrez.email is set
    Bio.Entrez.email = 'nishantthalwal@gmail.com'

    # Default folder name
    folder_path = "GenBankFiles"

    # Check if the folder exists; if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Fetch and save GenBank files
    for i in ID:  # Loop through the list of IDs
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




