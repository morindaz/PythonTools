# coding=utf-8
'''
*批量提取文件夹的名字 dir answer_C /b>E:\out\feature\answer_C.txt  #将该目录下video中的所有目录存到E盘的1.txt文件中
*转换好的视频目录：E:\video\answer_C
*声道数2  样本速率16000  PCM signed 512kbps stereo
'''
import os
import pandas as pd
from vadAnalysis import *
flag = "answer_C"
#输入视频的目录，需要加上相应的文件夹名称
inDir = "E:\\video\\"+flag
#输出音频的目录，需要加上相应的文件夹名称
outDir ="E:\out\\feature\\"+flag
cmd = "E:\out\\feature\\"+flag+".txt"
file = open(cmd)
lines = file.readlines()
reactTime = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    path = inDir+"\\"+lines[i]
    print path
    time = main([2, path])
    #如果存在两个以上的时间，则数组中第二个位置认为是开始的时间，第一个为客服的时间
    if len(time)>1:
        reactTime.append(time[1])
    #如果只有一个事件，则认为第一个就是开始的时间
    else:
        reactTime.append(time[0])
print reactTime
outPut = {'video': lines, 'reaction': reactTime}
print outPut
output_Archive = pd.DataFrame(outPut)
output_Archive.to_csv(flag+'.csv')
# print lines
