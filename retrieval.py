import Bio
import Bio.Entrez
import os

# Define a global list for IDs
ID = []

Bio.Entrez.email = 'nishantthalwal@gmail.com'  # Set your email
search_term = input("Enter The Search Term: ")  # Get the search term from the user
  


def ncbi_genbank():
    global ID  # Declare ID as a global variable to modify it inside the function

    # Perform the search
    with Bio.Entrez.esearch(db='nucleotide', retmax=int(input("Enter The Number of Sequences: ")), term=search_term) as handle:
        search_results = Bio.Entrez.read(handle)  # Parse the HTTP response to a dictionary

    # Clear the global ID list to avoid appending to old results
    ID.clear()
    
    # Populate the ID list
    for i in search_results['IdList']:  # Iterate over the 'IdList' in the parsed dictionary
        ID.append(i)  # Append each ID to the list

    print(f"Search Results: {search_results}")
    print(f"IDs: {ID}")




