import matplotlib.pyplot as plt
import time
from pathlib import Path

class Visualizer:
    def __init__(self, filename, output_dir='outputs/Graphs'):
        self.filename = filename
        self.output_dir = Path(output_dir) / filename
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def create_histograms(self, df, log_func):
        """Create histograms for all numeric columns"""
        numeric_cols = df.select_dtypes(include=['number']).columns

        for col in numeric_cols:
            log_func.info(f"Creating histogram for {col}...")
            time.sleep(0.5)

            plt.figure(figsize=(10, 5))
            plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.grid(axis='y', alpha=0.3)
            plt.savefig(f'{self.output_dir}/histogram_{col}.png')
            plt.close()
            log_func.success(f"✓ Saved histogram_{col}.png")
            time.sleep(0.5)

    def create_scatter(self, df, log_func):
        """Create scatter plot for first 2 numeric columns"""
        numeric_cols = df.select_dtypes(include=['number']).columns
        
        if len(numeric_cols) >= 2:
            log_func.info(f"Creating scatter plot...")
            time.sleep(0.5)
            
            plt.figure(figsize=(10, 5))
            plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]], 
                       color='green', alpha=0.6, s=50, edgecolor='black')
            plt.xlabel(numeric_cols[0])
            plt.ylabel(numeric_cols[1])
            plt.title(f'{numeric_cols[0]} vs {numeric_cols[1]}')
            plt.grid(alpha=0.3)
            plt.savefig(f'{self.output_dir}/scatter_{numeric_cols[0]}_vs_{numeric_cols[1]}.png', 
                       dpi=150, bbox_inches='tight')
            plt.close()
            
            log_func.success(f"✓ Saved scatter plot")
            time.sleep(0.5)

    def create_barcharts(self, df, log_func):
        """Create bar charts for categorical columns"""
        cat_cols = df.select_dtypes(include=['object']).columns
        
        for col in cat_cols:
            log_func.info(f"Creating bar chart for {col}...")
            time.sleep(0.5)
            
            plt.figure(figsize=(10, 5))
            df[col].value_counts().head(10).plot(kind='bar', color='coral', edgecolor='black')
            plt.title(f'Top values in {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(f'{self.output_dir}/bar_{col}.png', dpi=150, bbox_inches='tight')
            plt.close()
            
            log_func.success(f"✓ Saved bar_{col}.png")
            time.sleep(0.5)
    
    def create_all(self, df, log_func):
        """Create all visualizations"""
        self.create_histograms(df, log_func)
        self.create_scatter(df, log_func)
        self.create_barcharts(df, log_func)