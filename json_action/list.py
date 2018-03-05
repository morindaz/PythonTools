'''
找到符合某一列名字的数据，并且把所有符合的数据保存下来
'''
import os
import pandas as pd
all_file = os.listdir('D:\idcard_gt_online\idcard_gt_online')
csvPath = 'D:\\1226id_utf8.csv'
df = pd.read_csv(csvPath, sep=',', header=0)
data = df.values
print(type(data))
# dataFrame = pd.DataFrame(data)
# pic =
result = []
for obj in all_file:
    for i in data:
        if obj==i[0]:
            print(i)
            print(obj)
            result.append(i)

result_toCSV = pd.DataFrame(result)
result_toCSV.to_csv("result_hyc.csv")
