# **Data Processing & Visualization Tool: CLI-Based Data Cleaning & Exploration Tool for Noisy Real World CSV Data**

## Real World Problem
Real world datasets often contain missing values, inconsistent schema, and unstandardized columns, which slows down exploratory data analysis and research workflows.

## Short description
A Python tool that automatically cleans CSV datasets, removes null values, and creates beautiful visualizations. This project was designed to mirror real-world data preprocessing pipelines used in academic and industry research. 

## Quick Start
### Install from Source (For Development And Use)
```bash
git clone https://github.com/searifxr/DataCleanerPython-PIP
cd DataCleaner
pip install -e .
```


The tool will:
1. Find all CSV files in your project
2. Let you select which one to process
3. Clean the data
4. Optionally create visualizations

## What it does

1. **Loads CSV files** - Import your data from anywhere in the project
2. **Detects null values** - Shows what needs cleaning
3. **Cleans data** - Removes nulls, normalizes column names
4. **Creates visualizations** - Histograms, scatter plots, bar charts
5. **Saves everything organized** - Cleaned data + graphs by filename

## Folder Structure

```
DataCleaner/
├── process_data.py          # Main script
├── setup.py                 # Installation config
├── requirements.txt         # Dependencies
├── README.md                # This file
├── outputs/
│   └── visualizations.py    # Visualization class
├── sample_data/             # Example CSV files
└── outputs/
    ├── Data/                # Generated cleaned CSV files
    └── Graphs/              # Generated visualizations (by filename)
```

## Requirements

- Python 3.7+
- pandas
- matplotlib


### Local Development

```bash
pip install -e .
python process_data.py
```

## Features

✓ Automatic null value detection  
✓ Interactive cleaning prompts  
✓ Smart column name normalization  
✓ Multiple visualization types  
✓ Organized output folders  
✓ Loop-based processing (process multiple files)  

## License

Free to use and modify!
