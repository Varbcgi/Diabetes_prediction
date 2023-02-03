# -*- coding: utf-8 -*-

from metrics import *
from model import modelml 
import warnings
# Import libraries to handle data
import numpy as np
import pandas as pd

from data_preprocessing import *
from data_visualization import *
from metrics import *
import pickle


warnings.filterwarnings('ignore')

# Import required dataset from the path
dataset = pd.read_csv(r"C:\Users\varun.bhoj\Desktop\diabetes_binary.csv")

df = dataset.copy()
all_rep(df)

check_duplicates(df)

df = remove_anamolies(df)

# Split data into training and test sets
X_train, X_test, y_train, y_test = split_data(dataset)

# Oversample the minority class using SMOTE
X_res, y_res = imbdat(X_train, y_train)

# Make predictions on the test set
model = modelml(X_res, y_res)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
y_pred = predict_result(model, X_test)

# Print classification report with recall and precision
print(report(y_test, y_pred))

