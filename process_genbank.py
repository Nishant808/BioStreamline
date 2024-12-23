import os
import json
from Bio import SeqIO

# Define the path to the GenBank files
path = "C:/Users/Nishant Thalwal/Desktop/BioStreamline-main/GenBankFiles"

# List to store extracted data
extracted_data = []

def gc_features():
    # Iterate over the files in the folder
    for file_name in os.listdir(path):
        # Only process GenBank files (.gb extension)
        if file_name.endswith(".gb"):
            # Build the full file path
            file_path = os.path.join(path, file_name)
            
            # Open and parse the GenBank file
            with open(file_path, "r") as handle:
                records = SeqIO.parse(handle, "genbank")
                
                # Iterate over each record in the GenBank file
                for record in records:
                    print(f"Processing {file_name}: {record.id}")
                    
                    # Extract sequence length and GC content
                    sequence_length = len(record.seq)
                    gc_content = (record.seq.count('G') + record.seq.count('C')) / sequence_length
                    
                    # Dictionary to hold record data
                    record_data = {
                        "file_name": file_name,
                        "record_id": record.id,
                        "sequence_length": sequence_length,
                        "gc_content": gc_content,
                        "features": []
                    }
                    
                    # Iterate over the features in the record
                    for feature in record.features:
                        feature_type = feature.type
                        if feature_type in ['gene', 'CDS', 'exon', 'intron']:  # Check for specific features
                            feature_data = {"type": feature_type}
                            
                            # Extract specific qualifiers
                            if 'gene' in feature.qualifiers:
                                feature_data["gene_name"] = feature.qualifiers['gene']
                            if 'product' in feature.qualifiers:
                                feature_data["product"] = feature.qualifiers['product']
                            if 'translation' in feature.qualifiers:
                                feature_data["translation"] = feature.qualifiers['translation']
                            if feature_type in ['CDS', 'exon']:
                                feature_data["location"] = str(feature.location)
                                feature_data["sequence"] = str(feature.extract(record.seq))
                            
                            # Append feature data to the record
                            record_data["features"].append(feature_data)
                    
                    # Append record data to the extracted data list
                    extracted_data.append(record_data)
                    
    # Save the extracted data to a JSON file
    with open("extracted_data.json", "w") as json_file:
        json.dump(extracted_data, json_file, indent=4)  # Pretty-print the JSON for readability

    print("Data extraction and saving to JSON complete.")


