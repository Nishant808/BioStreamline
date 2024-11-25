import Bio.Entrez
import pandas as pd
from retrieval import ID

# Set email for NCBI Entrez
Bio.Entrez.email = "nishantthalwal@gmail.com"

# Lists to store CSV data
ID_CSV = []
Length_CSV = []
Accession_CSV = []
Title_CSV = []

# Function to fetch details and save to CSV
def to_csv():
    if not ID:
        print("ID list is empty. Please check the retrieval step.")
        return

    # Process each ID
    for i in ID:
        try:
            # Fetch summary data for the ID
            with Bio.Entrez.esummary(db='nucleotide', id=i) as handle:
                summary = Bio.Entrez.read(handle)

            # Debug: Print summary content
            print(f"Summary for ID {i}: {summary}")

            # Ensure summary has data
            if summary:
                dict1 = summary[0]  # Access the first result
                ID_CSV.append(dict1.get('Id', 'N/A'))
                Length_CSV.append(dict1.get('Length', 'N/A'))
                Accession_CSV.append(dict1.get('AccessionVersion', 'N/A'))
                Title_CSV.append(dict1.get('Title', 'N/A'))
            else:
                print(f"No summary data found for ID {i}. Skipping.")
        
        except Exception as e:
            print(f"Error processing ID {i}: {e}")

    # Check if data was retrieved
    if ID_CSV:
        # Create DataFrame
        data = {
            'ID': ID_CSV,
            'Length': Length_CSV,
            'Accession': Accession_CSV,
            'Title': Title_CSV
        }
        df = pd.DataFrame(data)

        # Write to CSV
        df.to_csv("Export.csv", index=False)
        print("Data successfully exported to Export.csv!")
    else:
        print("No data to write to CSV. Please check your inputs.")

