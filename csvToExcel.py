import pandas as pd

data = pd.read_csv('./output/naver_copy_sample.csv', encoding='ISO-8859-1')
writer = pd.ExcelWriter('./output/output_ulta.xlsx')
data.to_excel(writer, index=False,encoding='utf-8')
writer.save()
