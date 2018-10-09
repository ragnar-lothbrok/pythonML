import pandas as pd
import matplotlib.pyplot as plt

trainCsvData =  pd.read_csv("../titanic/train.csv")


#once you print this you will see NaN means no value present at that place
print(trainCsvData.head(5))

#OR

print('=================PRINTING FIRST 3 ROWS======')

print(trainCsvData[:3])

# print('Total Rows : '+trainCsvData.shape())



print('============SELECTING A COLUMN=============')
print(trainCsvData['PassengerId'])


print('============SELECTING MULTIPLE COLUMN AND ROWS===========')
print(trainCsvData[['PassengerId','Survived']][:3])

#For ploting data must be numeric
plt.rcParams['figure.figsize'] = (15, 5)
trainCsvData['PassengerId'].plot()


# trainCsvData.plot(figsize=(15, 10))
# plt.show()

print(trainCsvData)

#Gives count of each value
print(trainCsvData['Survived'].value_counts())


#show bar graph (histogram) mentioning value counts
trainCsvData['Survived'].value_counts().plot(kind='bar')
plt.show()