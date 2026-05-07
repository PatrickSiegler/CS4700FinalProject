import pandas as pd
import sys



def string_to_numerical_value(val):
    # columns/rows
    if val == "b":
        return 0
    if val == "x":
        return 1
    if val == "o":
        return -1
    
    # win state (between 0 and 1 for sigmoid)
    if val == "win":
        return 1
    if val == "loss":
        return 0
    if val == "draw":
        return 0.5
    
    raise ValueError(f"Unknown value: {val}")

# process raw data into processed data
if __name__ == '__main__':
    file = sys.argv[1]

    df = pd.read_csv(file)
    processed = df.copy()

    # convert to numerical values
    for col in processed.columns:
        processed[col] = processed[col].apply(string_to_numerical_value)

    # write to processed
    split = file.split('/') if '/' in file else file.split('\\')
    out_file = '/'.join(split[:-1]) + "/../processed/data.csv"
    print(f"output saved to {out_file}")
    processed.to_csv(out_file, index=False)