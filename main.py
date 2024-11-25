import retrieval
import process_genbank
import stat_analysis
import to_csv
import to_genbank

# Step 1: Retrieve Sequence IDs
def retrieve_sequences():
    print("Step 1: Retrieving sequence IDs from GenBank...")
    retrieval.ncbi_genbank()  # Assumes search term and count are prompted within the function
    print("Sequence IDs retrieved successfully.")

# Step 2: Save GenBank Files
def save_genbank_files():
    print("Step 2: Saving GenBank files...")
    to_genbank.save_genbank()  # Assumes IDs are handled globally in the retrieval module
    print("GenBank files saved successfully.")

# Step 3: Process GenBank Files
def process_files():
    print("Step 3: Processing GenBank files to extract features...")
    extracted_data = process_genbank.gc_features()
    print("Feature extraction complete.")
    return extracted_data

# Step 4: Perform Statistical Analysis
def analyze_features(extracted_data):
    print("Step 4: Performing statistical analysis on extracted features...")
    stat_analysis.analyze_feature_lengths(extracted_data)  # Assumes analysis and visualization are handled
    print("Statistical analysis complete.")

# Step 5: Export to CSV
def export_to_csv(extracted_data):
    print("Step 5: Exporting extracted data to CSV...")
    to_csv.export(extracted_data)  # Assumes the function handles exporting
    print("Data exported to CSV successfully.")

# Main function to orchestrate the pipeline
def main():
    print("Starting the automated pipeline...")
    retrieve_sequences()
    save_genbank_files()
    extracted_data = process_files()
    analyze_features(extracted_data)
    export_to_csv(extracted_data)
    print("Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()
