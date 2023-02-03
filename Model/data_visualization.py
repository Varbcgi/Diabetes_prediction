# -*- coding: utf-8 -*-

import warnings
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd

warnings.filterwarnings('ignore')


def ratio_diabetics(data_cp):
    # pie plot of diabetes ratio
    plt.figure(figsize=(12, 5))
    labels = ['No Diabetes', 'Diabetes']
    sizes = [data_cp['Diabetes_binary'].value_counts()[0],
             data_cp['Diabetes_binary'].value_counts()[1]]
    colors = ['green', 'red']
    plt.title(
        'Percentages of diabetic and non diabetics',
        fontdict={
            'fontsize': 20})
    plt.pie(
        sizes,
        labels=labels,
        autopct='%.1f%%',
        colors=colors,
        data=data_cp)


def gender_diabetic(data_cp):

    plt.figure(figsize=(12, 4))
    x = sns.countplot(x='Diabetes_binary', data=data_cp, hue='Sex')
    plt.xticks(rotation=90)
    plt.title(
        'Diabetes statistics among men and women',
        fontdict={
            'fontsize': 20})
    for i in x.patches:
        x.annotate(
            '{:.2f}'.format(
                (i.get_height() / data_cp.shape[0]) * 100) + '%',
            (i.get_x() + 0.25,
             i.get_height() + 0.01))
    plt.show()


def age_counts(data_cp):

    ageplt = px.treemap(data_cp, path=['Age'], title="Age counts")
    ageplt.show()


def age_diabetes(data_cp):

    plt.figure(figsize=(12, 5))
    sns.histplot(data_cp.Age[data_cp.Diabetes_binary == 0],
                 color="y", label="Non Diabetic", kde=True)
    sns.histplot(data_cp.Age[data_cp.Diabetes_binary == 1],
                 color="b", label="Diabetic", kde=True)
    plt.title("Relation between Age and Diabetes")
    plt.xticks(data_cp["Age"].unique())
    plt.legend()


def age(data_cp):
    plt.figure(figsize=(15, 10))
    sns.histplot(data_cp.Age[data_cp.Diabetes_binary == 0],
                 color="y", label="No Diabetic", kde=True)
    sns.histplot(data_cp.Age[data_cp.Diabetes_binary == 1],
                 color="b", label="Diabetic", kde=True)
    plt.title("Relation b/w Age and Diabetes")
    plt.xticks(data_cp["Age"].unique())
    plt.legend()


def smoker(data_cp):

    plt.figure(figsize=(12, 4))
    x = sns.countplot(x='Diabetes_binary', data=data_cp, hue='PhysActivity')
    plt.xticks(rotation=90)
    plt.title(
        'Diabetes statistics among those who do physical activity and who dont',
        fontdict={
            'fontsize': 20})
    for i in x.patches:
        x.annotate(
            '{:.2f}'.format(
                (i.get_height() / data_cp.shape[0]) * 100) + '%',
            (i.get_x() + 0.25,
             i.get_height() + 0.01))
    plt.show()


def phyexc(data_cp):

    plt.figure(figsize=(12, 4))
    x = sns.countplot(x='Diabetes_binary', data=data_cp, hue='PhysActivity')
    plt.xticks(rotation=90)
    plt.title(
        'Diabetes statistics among those who do physical activity and who dont',
        fontdict={
            'fontsize': 20})
    for i in x.patches:
        x.annotate(
            '{:.2f}'.format(
                (i.get_height() / data_cp.shape[0]) * 100) + '%',
            (i.get_x() + 0.25,
             i.get_height() + 0.01))
    plt.show()


def alch(data_cp):

    data_cp['HvyAlcoholConsump'].value_counts()
    plt.figure(figsize=(12, 4))
    x = sns.countplot(
        x='HvyAlcoholConsump',
        hue='Diabetes_binary',
        data=data_cp)
    plt.title(
        'Diabetes statistics among heavy drinkers',
        fontdict={
            'fontsize': 20})
    for i in x.patches:
        x.annotate(
            '{:.2f}'.format(
                (i.get_height() / data_cp.shape[0]) * 100) + '%',
            (i.get_x() + 0.25,
             i.get_height() + 0.01))
    plt.show()


def genhlt(data_cp):
    sns.countplot(data_cp["GenHlth"], data=data_cp, hue="Diabetes_binary")
    plt.title("Relation b/w GenHlth and Diabetes")


def highchol(data_cp):
    pd.crosstab(
        data_cp.HighChol,
        data_cp.Diabetes_binary).plot(
        kind="bar",
        figsize=(
            8,
             6))
    plt.title('Diabetes Disease Frequency for HighChol')
    plt.xlabel("HighChol")
    plt.ylabel('Frequency')
    plt.show()


def highcholbp(data_cp):
    sns.catplot(
        x="HighBP",
        y="HighChol",
        data=data_cp,
        hue="Diabetes_binary",
        kind="bar")
    plt.title("Relation b/w HighBP ,HighChol and Diabetes")


def highbp(data_cp):

    pd.crosstab(
        data_cp.HighBP,
        data_cp.Diabetes_binary).plot(
        kind="bar",
        figsize=(
            5,
             4))
    plt.title('Diabetes Disease Frequency for HighBP')
    plt.xlabel("HighBP")
    plt.ylabel('Frequency')
    plt.show()


def bmi_counts(data_cp):

    ax = px.treemap(data_cp, path=['BMI'], title="BMI counts")
    ax.show()


def bmi_age(data_cp):

    plt.figure(figsize=(25, 20))
    sns.histplot(data_cp.BMI[data_cp.Diabetes_binary == 0],
                 color="y", label="Non Diabetic", kde=True)
    sns.histplot(data_cp.BMI[data_cp.Diabetes_binary == 1],
                 color="b", label="Diabetic", kde=True)
    plt.title("Relation between BMI and Diabetes")

    plt.xticks(data_cp["BMI"].unique())
    plt.legend()


def all_rep(data_cp):

    ratio_diabetics(data_cp)
    gender_diabetic(data_cp)
    alch(data_cp)
    age(data_cp)
    age_diabetes(data_cp)
    age_counts(data_cp)
    bmi_age(data_cp)
    bmi_counts(data_cp)
    genhlt(data_cp)
    highchol(data_cp)
    highbp(data_cp)
    highcholbp(data_cp)
    smoker(data_cp)
    phyexc(data_cp)
