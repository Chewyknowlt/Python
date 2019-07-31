target =  r'B:\Python Course\Ch19_Working_with_CSV_files\02_read_CSV_dictReader\02_read_csv_dictReader.csv'

from csv import DictReader

with open(target) as f:
    data = DictReader(f)
    #extracting data in organized way
    for each in data:
        print(f"{each['name'].title()} {each['email']} {each['phone']} ")