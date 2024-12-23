# BioStreamline-Pipeline
![image](https://github.com/user-attachments/assets/2b2fd583-9293-4e8d-9ac9-8f5adc4b7836)

**BioStreamline** is an automated bioinformatics pipeline designed to streamline the process of retrieving, processing, and analyzing GenBank data. It integrates tools for data extraction, feature analysis, and visualization to provide an end-to-end solution for genomic data analysis.

---

## Features
- **Automated Sequence Retrieval**: Fetch sequence IDs from GenBank using customizable search terms.
- **GenBank File Processing**: Extract sequence features, calculate GC content, and annotate key genomic regions.
- **Statistical Analysis**: Perform detailed analysis on features such as CDS lengths and distribution.
- **Interactive Visualizations**: Generate plots including histograms, boxplots, and heatmaps for data insights.
- **Scalable Workflow**: Modular scripts allow for easy scaling and integration into larger projects.

---

## Workflow
1. **Retrieve Sequence IDs**: Query GenBank for nucleotide sequences based on user-defined search terms.
2. **Save GenBank Files**: Download and store sequence data locally for further processing.
3. **Process GenBank Files**: Extract relevant features, such as genes, CDS, and exons, while computing GC content.
4. **Analyze Features**: Perform statistical analysis and generate visualizations for comprehensive insights.

---

## Installation
### Prerequisites
- Python 3.8+
- Libraries:
  - `biopython`
  - `plotly`
  - `numpy`
  - `scipy`

Install dependencies using pip:
```bash
pip install biopython plotly numpy scipy
```

---

## Usage
1. Clone the repository:
```bash
git clone https://github.com/username/BioStreamline-Pipeline.git
cd BioStreamline-Pipeline
```

2. Run the main pipeline:
```bash
python main.py
```

3. Follow the prompts to input your search term and the number of sequences to retrieve.

---

## File Structure
- `main.py`: Orchestrates the entire pipeline.
- `retrieval.py`: Fetches sequence IDs from GenBank.
- `to_genbank.py`: Downloads and saves GenBank files.
- `process_genbank.py`: Processes GenBank files and extracts features.
- `stat_analysis.py`: Performs statistical analysis and visualization.

---

## Visualizations
- **Histogram**: CDS length distribution.
- **Bar Chart**: Feature type counts.
- **Boxplot and Violin Plot**: CDS length spread and density.
- **Heatmap**: Feature type proportions.
- **Scatter Plot**: Random feature lengths.

---

## Example Output
- Sequence IDs retrieved from GenBank.
- GenBank files saved in the `GenBankFiles` folder.
- Extracted data stored in `extracted_data.json`.
- Statistical analysis displayed in the terminal.
- Visualizations rendered interactively.

---

## Future Enhancements
- Add support for parallel processing to handle larger datasets.
- Include additional feature annotations like promoters and regulatory elements.
- Enable cloud deployment for remote accessibility.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the pipeline.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
- [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/)
- [Biopython](https://biopython.org/)
- [Plotly](https://plotly.com/)
