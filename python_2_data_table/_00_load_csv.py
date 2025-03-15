# Allowed functions : pandas or any lib for data set manipulation

#-> Dataset: (You have to adapt the type of return according to your library)

import pandas as pd

def load(path: str) -> list:
    try:
        df = pd.read_csv(path, index_col=None)
        print(f"Loading dataset of dimensions {df.shape}")
        pd.set_option('display.show_dimensions', False) # Optional: Suppress dimensions in display
        return (df)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
    except UnicodeDecodeError:
        print("Error: There was an encoding issue with the file.")
    except ValueError as e:
        print(f"ValueError: {e}") 
    return []

def main():
    print(load("life_expectancy_years.csv"))

if __name__ == "__main__":
    main()
    
"""Expected output
$> python tester.py
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
$>
"""