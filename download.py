import opendatasets as od

# Download dataset into the 'dataset' folder
od.download("https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud", data_dir="dataset")
