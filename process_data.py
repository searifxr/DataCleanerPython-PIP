import pandas as pd
from pathlib import Path
import time

from outputs.visualizations import Visualizer

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

class Log:
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'

    log_file_path = Path("outputs/process_log.txt")

    @staticmethod
    def write(msg_type, msg):
        with open(Log.log_file_path, 'a', encoding='utf-8') as f:
            f.write(f"[{msg_type.strip()}] {msg}\n")
    @staticmethod
    def info(msg):
        print(f"{Log.INFO}[INFO]{Log.END} {msg}")
        with open(Log.log_file_path, 'a', encoding='utf-8') as f:
            f.write(f"[INFO] {msg}\n")

    @staticmethod
    def success(msg):
        print(f"{Log.SUCCESS}[✔ SUCCESS]{Log.END} {msg}")
        with open(Log.log_file_path, 'a', encoding='utf-8') as f:
            f.write(f"[SUCCESS] {msg}\n")

    @staticmethod
    def warning(msg):
        print(f"{Log.WARNING}[⚠ WARNING]{Log.END} {msg}")
        with open(Log.log_file_path, 'a', encoding='utf-8') as f:
            f.write(f"[WARNING] {msg}\n")

    @staticmethod
    def error(msg):
        print(f"{Log.ERROR}[✖ ERROR]{Log.END} {msg}")
        with open(Log.log_file_path, 'a', encoding='utf-8') as f:
            f.write(f"[ERROR] {msg}\n")

# Create out put folder
Path('outputs').mkdir(exist_ok=True)

def main():
    """Main entry point for the application"""
    Path('outputs').mkdir(exist_ok=True)
    Path('data').mkdir(exist_ok=True)
    # Log.log_file_path.parent.mkdir(exist_ok=True)
    # with open(Log.log_file_path, 'w') as f:
    #     f.write(f"Data Processing Log - Started at {time.ctime()}\n\n")

    while True:
        print("\n" + "=" * 50)
        print("DATA PROCESSING SCRIPT")
        print("=" * 50)

        # List available CSV files from entire project except outputs/Data
        root_path = Path('.')
        csv_files = [
            f for f in root_path.glob('**/*.csv')
            if 'outputs' not in f.parts and 'Data' not in f.parts
        ]

        
        if not csv_files:
            Log.error("No CSV files found in project!")
            print("Please add CSV files anywhere in the project")
            continue
        
        print("\nAvailable files:")
        for i, file in enumerate(csv_files, 1):
            print(f"  {i}. {file.relative_to(root_path)}")
        
        # Load CSV file
        Log.info("\n[1] Loading data...")
        time.sleep(1)
        search_term = input("Enter file name (or number): ")
        time.sleep(0.5)

        # Check if user wants to quit
        if search_term.lower().strip() == 'quit':
            Log.success("Exiting Data Processing Script.")
            break

        # Try to find the file
        found_file = None
        
    
        # Try by number
        try:
            idx = int(search_term) - 1
            if 0 <= idx < len(csv_files):
                found_file = csv_files[idx]
        except ValueError:
            pass
        
        # Try by name search
        if not found_file:
            for file in csv_files:
                if search_term.lower() in file.stem.lower():
                    found_file = file
                    break
        
        if not found_file:
            print("\u203c" * 50)
            Log.error("File not found!")
            print("\u203c" * 50)
            continue
        
        file_name = found_file.stem
        
        try:
            df = pd.read_csv(found_file)
            time.sleep(0.5)
            Log.success(f"\u2714 Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
            time.sleep(1)
        except Exception as e:
            Log.error(f"Error reading file: {e}")
            continue

        Log.info("Original Data Columns:")
        Log.info(", ".join(df.columns))
        time.sleep(0.5)
        Log.info("First 10 rows of data:")
        Log.info("\n"+df.head(10).to_string())
        time.sleep(1)

        # Checks for null values
        Log.info("\n[2] Checking null values...")
        time.sleep(1)
        null_counts = df.isnull().sum()
        print("\nNull values per column:")
        time.sleep(0.5)
        print(null_counts)
        time.sleep(1)

        total_nulls = df.isnull().sum().sum()
        Log.info(f"Total null values: {total_nulls}")
        time.sleep(1)

        CleanFlag = True
        if total_nulls == 0:
            Log.success("No null values found, your data is clean!")
            CleanFlag = False
        else:
            yes_or_no: str = input('\u203c would you like to clean the null values? (y/n) \u203c')
            if yes_or_no and yes_or_no.__contains__('n'):
                Log.warning("null data is not recommended... are you sure? (y/n)")
                confirmation = input()
                if confirmation.__contains__('y'):
                    CleanFlag = False
            else:
                CleanFlag = True

        if CleanFlag:
            #Clean null values
            Log.info("[3] cleaning null values...")
            time.sleep(1)
            Log.info(f"Rows before cleaning: {len(df)}")
            time.sleep(0.5)
            df_clean = df.dropna()
            time.sleep(1)
            Log.info(f"Rows after cleaning: {len(df_clean)}")
            time.sleep(0.5)
            Log.info(f"Rows removed: {len(df) - len(df_clean)}")
            time.sleep(1)

            # Clean column names
            Log.info("[4] Cleaning columns")
            time.sleep(1)

            original_columns = df_clean.columns.tolist()
            cleaned_columns = (
                df_clean.columns
                .str.strip()
                .str.replace(r"[^\w]+", "_", regex=True)
                .str.lower()
            )

            df_clean.columns = cleaned_columns

            # Log only meaningful changes (ignore pure lowercase changes)
            for old, new in zip(original_columns, cleaned_columns):
                if old.replace(" ", "").lower() != new.replace("_", ""):
                    Log.info(f"Cleaned column: '{old}' -> '{new}'")

            time.sleep(0.5)
            Log.success("Column names cleaned")

            

            #Saving cleaned data
            output_path = f'outputs/Data/{file_name}_cleaned.csv'
            Log.info(f"Saving to: {output_path}")
            time.sleep(0.5)
            df = df_clean
            df_clean.to_csv(output_path, index=False, encoding="utf-8-sig")
            time.sleep(1)
            Log.success(f"Saved to: {output_path}")
            time.sleep(1)

            print('\n' + '=' * 50)
            time.sleep(0.5)
            Log.success(" PROCESSING COMPLETE!")
            time.sleep(0.5)
            print('=' * 50)
            
            # Ask for visualizations
            time.sleep(1)
            viz_choice = input('\n✚ Would you like to create visualizations? (y/n) ✚')
            if viz_choice and not viz_choice.__contains__('n'):
                Log.info("\n[5] Creating visualizations...")
                time.sleep(1)
                viz = Visualizer(file_name)
                viz.create_all(df_clean, Log)
                time.sleep(1)
                Log.success("Visualizations created!")
                time.sleep(1)

        else:
            output_path = f'outputs/Data/{file_name}.csv'
            Log.info(f"Saving to: {output_path}")
            time.sleep(0.5)
            Log.info("Saving as it is")
            time.sleep(1)   
            df.to_csv(output_path, index=False,encoding='utf-8-sig')
            time.sleep(1)
            Log.success(f"Saved to: {output_path}")
            time.sleep(1)

            print('\n' + '=' * 50)
            time.sleep(0.5)
            Log.success("PROCESSING COMPLETE!")
            time.sleep(0.5)
            print('=' * 50)
            
            # Ask for visualizations
            time.sleep(1)
            viz_choice = input('\n✚ Would you like to create visualizations? (y/n) ✚')
            if viz_choice and not viz_choice.__contains__('n'):
                Log.info("[5] Creating visualizations...")
                time.sleep(1)
                viz = Visualizer(file_name)
                viz.create_all(df, Log)
                time.sleep(1)
                Log.success("Visualizations created!")
                time.sleep(1)

        # Ask to process another file
        time.sleep(1)
        another = input('\n✚ Process another file? (y/n) ✚')
        if another and another.__contains__('n'):
            Log.success("\nThanks for using Data Processing Script!")
            Log.success(f"Saved cleaned file: {output_path} at {time.ctime()}")
            break
            

if __name__ == "__main__":
    main()



