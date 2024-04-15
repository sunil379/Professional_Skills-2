import requests
import pandas as pd

# Reading from Web (.txt)
web_url_txt = "https://example-files.online-convert.com/document/txt/example.txt"
response_txt = requests.get(web_url_txt)
web_data_txt = response_txt.text

# Displaying contents from Web (.txt)
print("Contents of Web (.txt):")
print(web_data_txt)
print("\n" + "-"*50 + "\n")  # Separating sections

# Reading from Web (.csv)
web_url_csv = "https://calmcode-datasette.fly.dev/calmcode/sleep.csv"
response_csv = requests.get(web_url_csv)
web_data_csv = response_csv.text

# Displaying contents from Web (.csv)
print("Contents of Web (.csv):")
print(web_data_csv)
print("\n" + "-"*50 + "\n")  # Separating sections

# Reading from Disk (.txt)
local_txt_file_path = "python.txt"
with open(local_txt_file_path, "r") as local_txt_file:
    local_txt_data = local_txt_file.read()

# Displaying contents from Disk (.txt)
print("Contents of Disk (.txt):")
print(local_txt_data)
print("\n" + "-"*50 + "\n")  # Separating sections

# Reading from Disk (.csv)
local_csv_file_path = "english_1grams.csv"
df = pd.read_csv(local_csv_file_path)

# Displaying contents from Disk (.csv)
print("Contents of Disk (.csv):")
print(df)
