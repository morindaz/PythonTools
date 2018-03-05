import json

h = json.load(open("20171229_data.json"))

done_dict = {}
for d in h["rasa_nlu_data"]["common_examples"]:
    if d["intent"]:
        done_dict[d["text"]] = d

print "Done = ", len(done_dict)

auto_fill = 0
skip = 0

output_list = []
text_set = set()
for d in h["rasa_nlu_data"]["common_examples"]:
    if d["intent"]:
        output_list.append(d)
    else:
        if d["text"] in done_dict:
            output_list.append(done_dict[d["text"]])
            auto_fill += 1
        else:
            if d["text"] not in text_set:
                output_list.append(d)
            else:
                d["intent"] = "X"
                output_list.append(d)
                skip += 1
    text_set.add(d["text"])

h["rasa_nlu_data"]["common_examples"] = output_list


json.dump(h, open("remove_dup.json", "w"))
print "autofill = ", auto_fill
print "skip = ", skip
