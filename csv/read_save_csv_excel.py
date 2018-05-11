# -*- coding: utf-8 -*-
import pandas as pd
path = "./a.csv"
read_csv = pd.read_csv(path, sep=',', header=0)
df = {"json_name": img_name, "company_name":company_name, "establish": establish,
      "reg_num":reg_num,"address":address,"person":person,"count":count_number}
output = pd.DataFrame(df)
output.to_csv(output_name)

read_excel = pd.read_excek(path,header =0)
all_img_labels.sort_values(by='filename').to_excel(os.path.join(img_input_dir, 'aug_label.xlsx'), index=False)

print("labels generated to file {} finished".format(output_name))