#!/bin/python3

import math
import os
import random
import re
import sys

import pandas as pd
from sklearn import linear_model
import sys

def getPred(timeCharged):
    trainCsvData = pd.read_csv("https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt", sep=",",
                               names=['time_charged', 'battery_lasted'])
    trainCsvData['time_charged'] = trainCsvData['time_charged']
    trainCsvData['battery_lasted'] = trainCsvData['battery_lasted']

    trainCsvData['battery_lasted'] = trainCsvData['battery_lasted'].astype(int)

    trainX = trainCsvData.as_matrix(['time_charged'])
    trainY = trainCsvData['battery_lasted']

    algo = linear_model.LinearRegression()
    # algo = linear_model.LogisticRegression()

    model = algo.fit(trainX,trainY)


    trainX_Pred = algo.predict(trainX)

    list = []
    list.append(timeCharged)
    df = pd.DataFrame(list)
    return '{0:.2f}'.format(algo.predict(df)[0]);


if __name__ == '__main__':
    timeCharged = float(input())
    print(getPred(timeCharged))
