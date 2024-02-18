import pandas as pd

try:
    data = pd.read_csv('./output/naver_copy_sample.csv', encoding='utf-8',encoding_errors='ignore')
except UnicodeDecodeError as e:
    print(f"Error reading CSV file: {e}")
    # Handle the exception as needed, e.g., log the error, skip problematic rows, etc.
    # You might want to add more specific handling based on your use case

# Continue with the rest of your processing, assuming data is loaded successfully
writer = pd.ExcelWriter('output.xlsx')
data.to_excel(writer, index=False)
writer.close()


