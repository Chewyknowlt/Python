target = r'B:\Python Course\Ch19_Working_with_CSV_files\04_CSV_DictWriter\04_CSV_DictWriter.csv'

from csv import DictWriter

with open(target, 'w', newline = '') as f:
    burnData = DictWriter(f, fieldnames = ['name', 'country', 'age'])
    burnData.writeheader()

    #Method 1 -> do it multiple times
    burnData.writerow(
        {
            'name' : 'hamza',
            'country' : 'Pakistan',
            'age' : 22
        }
    )
    
    #method 2 -> Do everything 1 time
    burnData.writerows(
        [
            {'name': 'Hamza', 'country': 'Pakistan', 'age': 22},
            {'name': 'Wajiha', 'country': 'Pakistan', 'age': 20},
            {'name': 'Mahnoor', 'country': 'Pakistan', 'age': 26},
        ]
    )