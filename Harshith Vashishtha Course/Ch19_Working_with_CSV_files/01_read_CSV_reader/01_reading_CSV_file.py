#read  csv file
target =r'B:\Python Course\Ch19_Working_with_CSV_files\01_read_CSV_reader\01_reading_CSV.csv'
from csv import reader

with open(target) as f:
    data = reader(f)  
    #titerator
    next(data)  #['name', 'email', 'phone'] to hide heading
    for row in data:
        print(row)