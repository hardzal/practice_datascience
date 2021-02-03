import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import surprise
from surprise import SVD
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise import Reader, Dataset
from surprise import KNNBasic

# read dataset 
jobs = pd.read_csv('dataset/export_dataframe.csv')
# EDA (Exploritary Data Analysis)
# a head list of dataset
jobs.head()
# a summary / description of dataset
jobs.describe()
# an info about dataset
jobs.info()

