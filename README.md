# Diabetes_prediction
This GitHub repository contains code for detecting diabetes using machine learning. This GitHub repository contains code for detecting diabetes using machine learning. The code is written in Python and utilizes various libraries such as scikit-learn and pandas for preprocessing and modeling. The dataset used for training and testing the model is also included in the repository. The model is trained after evaluating various algorithms such as decision tree, random forest, and logistic regression. The performance of the model is evaluated using metrics such as accuracy, precision, and recall. The repository also includes a detailed documentation on how to use the code and interpret the results. This can be a valuable resource for researchers and developers who are working on diabetes detection projects.
# About the dataset
diabetes _ binary _ health _ indicators _ BRFSS2015.csv is a clean dataset of 253,680 survey responses to the CDC's BRFSS2015. The target variable Diabetes_binary has 2 classes. 0 is for no diabetes, and 1 is for prediabetes or diabetes. This dataset has 21 feature variables and is not balanced.
# Docker
In order to build the Docker Image please use 
`docker build -t <filename> <rootdirectory`

In order to run the Docker Image please use 
`docker run -p 5000:5000 -p 8000:8000 <filename>`
