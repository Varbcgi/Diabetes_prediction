# -*- coding: utf-8 -*-

from sklearn.metrics import classification_report

def report(y_test, y_pred):

    print(classification_report(y_test, y_pred))