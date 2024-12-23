import Bio
import Bio.Entrez
import os

# Set your email for NCBI requests
Bio.Entrez.email = str(input("Enter Your E-mail: "))

# Define a global list for IDs
ID = []

# Get the search term from the user
search_term = input("Enter the search term: ")

# Function to search NCBI and save IDs
def ncbi_genbank():
    global ID  # Declare ID as a global variable to modify it inside the function

    try:
        # Get the number of sequences to fetch
        retmax = int(input("Enter the number of sequences: "))
        
        # Perform the search
        with Bio.Entrez.esearch(db='nucleotide', retmax=retmax, term=search_term) as handle:
            search_results = Bio.Entrez.read(handle)  # Parse the HTTP response to a dictionary

        # Clear the global ID list to avoid appending to old results
        ID.clear()
        
        # Filter out IDs with no nucleotide sequences
        print("Filtering records with nucleotide sequences...")
        for seq_id in search_results['IdList']:
            with Bio.Entrez.efetch(db='nucleotide', id=seq_id, rettype='gb', retmode='text') as fetch_handle:
                record = Bio.SeqIO.read(fetch_handle, "genbank")
                if len(record.seq) > 0:  # Check if the sequence exists
                    ID.append(seq_id)

        # Write the filtered IDs to ID.txt
        with open('ID.txt', 'w') as id_file:
            for i in ID:
                id_file.write(f"{i}\n")  # Write each ID to the file

        print(f"Filtered IDs: {ID}")

    except Exception as e:
        print(f"An error occurred: {e}")
