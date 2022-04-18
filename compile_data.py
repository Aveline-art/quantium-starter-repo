import csv
import os
import sys

def main(argv):
    folder = argv[0]
    paths = [f'{folder}/{file}' for file in os.listdir(folder)]
    open_csv(paths)
    

def open_csv(paths):
    with open('data/compiled_daily_sales_data.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['product', 'sales', 'date', 'region']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for file in paths:
            with open(file, 'r', encoding='utf-8') as f:
                filereader = csv.DictReader(f)
                for row in filereader:
                    if row['product'] == 'pink morsel':
                        writer.writerow({
                            'product': row['product'],
                            'sales': int(row['quantity']) * float(row['price'][1:]),
                            'date': row['date'],
                            'region': row['region']
                        })

if __name__ == "__main__":
   main(sys.argv[1:])