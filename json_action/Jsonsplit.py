'''
可以拼接两个json文件，template_json为原始的文件
add为需要新增上去的文件
result为结果，checkpoint为检查点，当在检查点时候需要符合条件
两个range为拼接的范围
'''
import json
a =[2,3,4,5,6,7]
b = a[0:3]
print(b)
# template_json = "20180102hyc.json"
add_json = "20180102_dataP180.json"
result_json = "20180102_sssdata.json"
checkpoint = 5600
range_one = 5200
# range_two = range_one + 800
range_two = 6999
with open('D:\\combine\\' + add_json, 'r', encoding='utf-8-sig') as h:
    template = json.load(h)
copy_h = template['rasa_nlu_data']['common_examples']
arr1 = template
print(arr1['rasa_nlu_data']['common_examples'][checkpoint])  # 无数据
print(template['rasa_nlu_data']['common_examples'][checkpoint])  # 无数据

# with open('D:\\combine\\' + add_json, 'r', encoding='utf-8-sig') as m:
#     add_file = json.load(m)
# print(add_file['rasa_nlu_data']['common_examples'][checkpoint])
# 有数据
for i in range(7300):
    arr1['rasa_nlu_data']['common_examples'][i] = template['rasa_nlu_data']['common_examples'][i]
with open(result_json, "w") as mm:
    json.dump(arr1, mm, indent=1)
    print("finish")
print("hello")
