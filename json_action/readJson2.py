import json

with open('D:\\combine\\t0_719_1280_1319.json', 'r', encoding='utf-8-sig') as h:
    data_h = json.load(h)
copy_h = data_h
with open('D:\\combine\\t720_1239.json', 'r', encoding='utf-8-sig') as m:
    data_m = json.load(m)
copy_m = data_m
data = data['rasa_nlu_data']
# for example in data['common_examples']:
#     print(example['text'])
#     print(example['intent'])
#     for entity in example['entities']:
#         print(entity['start'])
#         print(entity['end'])
#         print(entity['value'])
#         print(entity['entity'])

for i in range(10):
    print(data2['common_examples'][3])
print(11)