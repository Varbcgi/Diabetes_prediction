import warnings
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import numpy as np
# Import libraries to handle data

warnings.filterwarnings('ignore')


def data_check(dataset):
    # To get the information on the data
    dataset.info()


def check_duplicates(df):

    # Summing up the count of duplicate data
    df.duplicated().sum()


def remove_duplicates(df):

    # Drop all duplicates
    df_dup = df.drop_duplicates(inplace=True)
    return np.array(df_dup)


def remove_anamolies(df):

    # Using Isolation forest in order to check for anamolies
    model = IsolationForest()
    model.fit(df)
    # df['anomailes_scores']=model.decision_function(df)
    df['anomaly'] = model.predict(df)

    df[df['anomaly'] == -1]
    df.drop(df[df['anomaly'] == -1].index, inplace=True)
    return df


def split_data(dataset):
    # Seprating dependent and independent features
    y_diabetes = dataset['Diabetes_binary'].values
    X = dataset.drop(['Diabetes_binary'], axis=1)
    X = X.values

    # Splitting dataset into test and training sets
    X_train_org, X_test, y_train_org, y_test = train_test_split(
        X, y_diabetes, test_size=0.30, random_state=44, stratify=y_diabetes)
    return X_train_org, X_test, y_train_org, y_test


def imbdat(x_train, y_train):

    # Using SMOTE to oversample minority data
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(x_train, y_train)
    return X_res, y_res
