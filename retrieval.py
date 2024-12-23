import Bio
import Bio.Entrez
import os

# Set your email for NCBI requests
Bio.Entrez.email = 'nishantthalwal@gmail.com'

# Define a global list for IDs
ID = []

# Get the search term from the user
search_term = input("Enter The Search Term: ")

def ncbi_genbank():
    global ID  # Declare ID as a global variable to modify it inside the function

    # Perform the search
    with Bio.Entrez.esearch(db='nucleotide', retmax=int(input("Enter The Number of Sequences: ")), term=search_term) as handle:
        search_results = Bio.Entrez.read(handle)  # Parse the HTTP response to a dictionary

    # Clear the global ID list to avoid appending to old results
    ID.clear()
    
    # Populate the ID list and write to ID.txt
    with open('ID.txt', 'w') as id_file:
        for i in search_results['IdList']:  # Iterate over the 'IdList' in the parsed dictionary
            ID.append(i)  # Append each ID to the list
            id_file.write(f"{i}\n")  # Write each ID to the file

    print(f"Search Results: {search_results}")
    print(f"IDs: {ID}")


