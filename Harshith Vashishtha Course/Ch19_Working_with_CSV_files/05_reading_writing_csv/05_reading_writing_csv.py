readFile = r'B:\Python Course\Ch19_Working_with_CSV_files\05_reading_writing_csv\05_reading_csv.csv'
writeFile = r'B:\Python Course\Ch19_Working_with_CSV_files\05_reading_writing_csv\05_writing_csv.csv'

from csv import DictReader, DictWriter

with open(readFile) as rf:
    with open(writeFile, 'w', newline = '') as wf:
        csvRead = DictReader(rf)  #Read

        csvWrite = DictWriter(wf, fieldnames = ['name', 'designation', 'salary']) #write
        csvWrite.writeheader()
        for row in csvRead:
            name, designation, salary = row['name'], row['designation'], row['salary']
            csvWrite.writerow(
                {
                    'name' :  name.title(),
                    'designation' : designation.upper(),
                    'salary' : salary
                }
            )