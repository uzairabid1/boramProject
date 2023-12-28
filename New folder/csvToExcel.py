import pandas as pd

data = pd.read_csv('naver_copy_sample.csv')
writer = pd.ExcelWriter('output_ulta.xlsx')
data.to_excel(writer, index=False,encoding='utf-8')
writer.save()
