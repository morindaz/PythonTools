# coding=utf-8
'''
批量将mov或者mp4的文件转换成wav，方便后续vad语音判断开始的帧
并将开始和结束的时间记录下来
*批量提取文件夹的名字 dir answer_C /b>E:\out\feature\answer_C.txt  #将该目录下video中的所有目录存到E盘的1.txt文件中
*批量生成对应文件夹下面的所有文件名称，保存成txt格式。
*利用ffmpeg将mov转换成wav格式
# ffmpeg.exe -i __34.15to38.4_Admiration.mov __34.15to38.4_Admiration.wav
# ffmpegDir = "E:\pingan\压缩包\\ffmpeg-20170821-d826951-win64-static\\ffmpeg-20170821-d826951-win64-static\\bin"
*转换好的视频目录：E:\video\answer_C
'''


import os
ffmpegDir = "E:\pingan\\Zip\\ffmpeg-20170821-d826951-win64-static\\ffmpeg-20170821-d826951-win64-static\\bin"
flag = "answer_I"
#输入视频的目录，需要加上相应的文件夹名称
inFix = "E:\\pingan\\CQT_PingAn\\CQTVideo\\"
#输出音频的目录，需要加上相应的文件夹名称
inDir = inFix+flag
outDir = "E:\\video\\"+flag
cmd = "E:\out\\feature\\video\\"+flag+".txt"
file = open(cmd)
lines = file.readlines()
os.chdir(ffmpegDir)


for i in range(len(lines)):
    lines[i] = lines[i].strip()
    _, audioname = os.path.split(lines[i])
    # print audioname
    filestr, postfix = os.path.splitext(audioname)
    itemCMD = "ffmpeg.exe -i "  + inDir+"\\"+lines[i] + " " + outDir + "\\" + filestr + ".wav"
    os.system(itemCMD)
    print itemCMD
