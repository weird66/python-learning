# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format. Then, compute the maximum, minimum, average, and absolute values for each column in the dataset. (see attached file)

import pandas as pd

class DatasetProcessor:
    def __init__(self):
        self.df = None

    def read_csv(self, csv_path):
        try:
            self.df = pd.read_csv(csv_path, sep=';')
            print(f"Successfully loaded {csv_path}")
        except FileNotFoundError:
            print(f"Error: The file at {csv_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            raise

    def to_parquet(self, parquet_path):

        if self.df is not None:
            try:
                self.df.to_parquet(parquet_path, engine='auto')
                print(f"Successfully converted to {parquet_path}")
            except Exception as e:
                print(f"An error occurred during Parquet conversion: {e}")
                raise
        else:
            print("DataFrame not loaded. Cannot convert to Parquet.")

    def calculate_statistics_from_parquet(self, parquet_path):

        try:
            df_from_parquet = pd.read_parquet(parquet_path)
            print(f"Successfully loaded {parquet_path} for statistics.")
            numeric_cols = df_from_parquet.select_dtypes(include=['number']).columns
            stats = {}
            for col in numeric_cols:
                stats[col] = {
                    'max': df_from_parquet[col].max(),
                    'min': df_from_parquet[col].min(),
                    'average': df_from_parquet[col].mean(),
                    'absolute': df_from_parquet[col].abs().tolist()
                }
            return stats
        except FileNotFoundError:
            print(f"Error: The file at {parquet_path} was not found.")
            raise
        except Exception as e:
            print(f"An error occurred while reading the Parquet file or calculating statistics: {e}")
            raise

def main():

    csv_file = 'week3/student-mat.csv'
    parquet_file = 'week3/student-mat.parquet'

    try:
        processor = DatasetProcessor()

        processor.read_csv(csv_path=csv_file)

        processor.to_parquet(parquet_path=parquet_file)

        statistics = processor.calculate_statistics_from_parquet(parquet_path=parquet_file)
        if statistics:
            print("\nStatistics for numeric columns from Parquet file:")
            for col, stats in statistics.items():
                print(f"\nColumn: {col}")
                print(f"  Max: {stats['max']}")
                print(f"  Min: {stats['min']}")
                print(f"  Average: {stats['average']:.2f}")
                # Printing all absolute values can be long, so we'll just show the first 5
                print(f"  Absolute Values (first 5): {stats['absolute'][:5]}")

    except Exception as e:
        print(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
