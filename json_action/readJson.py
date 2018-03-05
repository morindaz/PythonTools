'''
可以拼接两个json文件，template_json为原始的文件
add为需要新增上去的文件
result为结果，checkpoint为检查点，当在检查点时候需要符合条件
两个range为拼接的范围
'''
import json

template_json = "./combine/maoshunyi_greeting.json"
add_json = "./combine/maoshunyi_insure_80.json"
result_json = "combine_data.json"
checkpoint = 5600
range_one = 5200
# range_two = range_one + 800
range_two = 6999
with open(template_json, 'r', encoding='utf-8-sig') as h:
    template = json.load(h)
copy_h = template['rasa_nlu_data']['common_examples']
arr1 = template

with open('D:\\combine\\' + add_json, 'r', encoding='utf-8-sig') as m:
    add_file = json.load(m)
print(add_file['rasa_nlu_data']['common_examples'][checkpoint])
# 有数据
for i in range(range_one, range_two):
    arr1['rasa_nlu_data']['common_examples'][i] = add_file['rasa_nlu_data']['common_examples'][i]

print(arr1['rasa_nlu_data']['common_examples'][checkpoint])  # 有数据
with open(result_json, "w") as mm:
    json.dump(arr1, mm, indent=1)
    print("finish")
print("hello")
# mm.write(json.dumps(arr1))
# for i in range(1280,1319):
#     arr1['rasa_nlu_data']['common_examples'][i]
# json_dic2 = json.dump(arr1)
# print(arr1['rasa_nlu_data']['common_examples'][120])
# print(data_h['rasa_nlu_data']['common_examples'][120])
# print(data_m['rasa_nlu_data']['common_examples'][120])
# for i in range(10):
#     print(data2['common_examples'][3])
