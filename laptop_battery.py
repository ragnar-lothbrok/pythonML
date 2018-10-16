#!/bin/python3
# https://www.hackerrank.com/challenges/battery/editorial
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def getPred(timeCharged):
    trainCsvData = pd.read_csv("https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt", sep=",",
                               names=['time_charged', 'battery_lasted'])

    trainCsvData['time_charged'] = trainCsvData['time_charged']
    trainCsvData['battery_lasted'] = trainCsvData['battery_lasted']

    trainCsvData = trainCsvData.sample(frac=1)

    trainCsvData['battery_lasted'] = trainCsvData['battery_lasted'].astype(int)

    trainX = trainCsvData.as_matrix(['time_charged'])
    trainY = trainCsvData['battery_lasted']

    trainX, testX, trainY, y_test = train_test_split(trainX, trainY, test_size=0.2)

    algo = linear_model.LinearRegression()
    # algo = linear_model.LogisticRegression()

    model = algo.fit(trainX,trainY)


    trainX_Pred = algo.predict(trainX)

    list = []
    list.append(timeCharged)
    df = pd.DataFrame(list)
    # '{0:.2f}'.format(algo.predict(df)[0]);
    return "{0:.2f}".format(min(charge_time*2,8))


if __name__ == '__main__':
    timeCharged = float(input())
    print(getPred(timeCharged))
