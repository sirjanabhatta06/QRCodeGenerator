import csv
from CSVReader import CSVReader

source_file_path = "QRCodeGenerator/Web_Scrapped_websites.csv"

def main():
    csv_reader = CSVReader(source_file_path)
    websites_list = csv_reader.read_csv_file()

    print(websites_list)

if __name__=="__main__":
    main()