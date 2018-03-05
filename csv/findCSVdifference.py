# 比较了两个csv，除去其中重复的部分
import pandas as pd
basic ="E:\\pingan\\dataMiningFrame_GammaLab\\data\\need\\"
testPath = basic+"test.csv"
trainPath = basic+'train2.csv'
test = pd.read_csv(testPath,sep=',',header=0)
train = pd.read_csv(trainPath,sep=',',header=0)
dataTest = test.values
dataTrain = train.values
result = []
# dataTest = [[2,1,23,3]]
print(len(dataTrain))
print(len(dataTest))
count =0
for i in dataTrain:
# print(len(i))
    res =0
    for m in dataTest:
        temp = (i==m).all()
        if temp:
            print("出现相同")
            res =1
            break
    if res ==0:
        result.append(i)
        print("不同的")
print(len(dataTrain))
print(len(dataTest))
print(len(result))
selected = pd.DataFrame(result)
selected.to_csv("selected.csv")