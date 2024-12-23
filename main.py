import retrieval
import to_genbank
import process_genbank
import stat_analysis
import json
import Clean_Directory

folder_path = r"C:/Users/Nishant Thalwal/Desktop/Biostreamline-main/GenBankFiles"

# Main function to orchestrate the pipeline
def main():
    print("Starting the automated pipeline...")
    retrieval.ncbi_genbank()
    to_genbank.save_genbank()
    process_genbank.gc_features()
    with open('extracted_data.json', 'r') as f:
        data=json.load(f)
    # Analyze the feature lengths and counts
    stat_analysis.analyze_feature_lengths(data=data)
    print("Pipeline execution completed successfully.")



if __name__ == "__main__":
    Clean_Directory.clear_folder(folder_path)
    main()

