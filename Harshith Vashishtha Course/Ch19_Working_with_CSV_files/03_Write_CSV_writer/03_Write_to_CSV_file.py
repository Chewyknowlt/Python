#writer, DictWriter
target = r'B:\Python Course\Ch19_Working_with_CSV_files\03_Write_to_CSV_file\03_Write_to_CSV_file.csv'

from csv import writer

with open(target, 'w', newline = '') as f:  #newline = '' -> delete blanks lines
    burn_data = writer(f)
    #Methods -> writerow, writerows
    # burn_data.writerow(['name', 'country'])
    # burn_data.writerow(['hamza', 'pakistan'])
    # burn_data.writerow(['wajiha', 'pakistan'])

    burn_data.writerows( [ ['name', 'country'], ['hamza', 'pakistan'], ['wajiha', 'pakistan'] ] )