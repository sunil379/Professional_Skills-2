# Writing to a Text File (.txt)
text_data = '''Writing to a file in Python
There are two ways to write in a file:
a)Using write()
b)Using writelines()

# Writing to a Python Text File Using write()
write() : Inserts the string str1 in a single line in the text file.
File_object.write(str1)
'''

txt_file_path = "sample.txt"
with open(txt_file_path, "w") as txt_file:
    txt_file.write(text_data)

# Writing to a CSV File (.csv)
import csv

csv_data = [
    ["Name", "Age", "City"],
    ["Sam", 25, "New York"],
    ["Adam", 30, "San Francisco"],
    ["Shane", 22, "Chicago"]
]

csv_file_path = "sample.csv"
with open(csv_file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(csv_data)
