import csv
import os
import sys

def main(argv):
    folder = argv[0]
    for file in os.listdir(folder):
        open_csv(f'{folder}/{file}')
    

def open_csv(file):
    with open(file, 'r', encoding='utf-8') as f:
        filereader = csv.DictReader(f)

        with open('data/compiled_daily_sales_data.csv', 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['product', 'sales', 'date', 'region']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
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