import pandas as pd
import numpy as np
import argparse
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

###function calcualtes distance matrix for mxn matrix where m is the number of observations, and the space is n-dimesions
def calculate_distance(matrix, metric):
    distance_matrix =pdist(matrix, metric=metric)
    distance_matrix = squareform(distance_matrix)
    return(distance_matrix)

def main():
    parser = argparse.ArgumentParser(description='Do some stuff and hope it works.')
    parser.add_argument('input_sheet', help='name of bucket table in csv format') 
    parser.add_argument('output_sheet', help='name of output file')
    parser.add_argument('metric',choices={"euclidean", "jaccard", "braycurtis", "canberra"},help='type of distance metric')
    args = parser.parse_args()

    metric = args.metric
    input_file = args.input_sheet
    output_file = args.output_sheet

    df = pd.read_csv(input_file)

    sample_name = df["sample_name"].tolist()
    features = df.columns.tolist()

    df.drop(["sample_name"], axis=1, inplace=True)
    matrix = df.to_numpy()
    
    distance_matrix = calculate_distance(matrix, metric)

    new_df = pd.DataFrame(distance_matrix)
    new_df.set_index(pd.Series(sample_name), inplace=True)
    new_df.columns = sample_name
    
    new_df.to_csv(output_file)


if __name__ == "__main__":
    main()
