import pandas as pd

# Reading Excel data sheet
excel_file_path = "Formula_Excel_Template.xlsx"
df = pd.read_excel(excel_file_path)

# Displaying contents of the DataFrame
print("Contents of Excel data sheet:")
print(df)
