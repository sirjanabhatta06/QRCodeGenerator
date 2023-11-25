import requests
import csv
import qrcode
from CSVReader import CSVReader
from UrlValidator import Validator

source_file_path = "Web_Scrapped_websites.csv"

def main():
    # Read the csv file and store in the websites_list 
    csv_reader = CSVReader(source_file_path)
    websites_list = csv_reader.read_csv_file()
    print(f"------- Done reading {source_file_path} file.-------")

    #Pass the websites list and Validate the websites 
    webValidator = Validator()
    valid_websites_list = webValidator.Validate(websites_list)
    print(f"-------- Done Validating Websites.---------")
    for elem in valid_websites_list:
        print(elem + " ")

if __name__=="__main__":
    main()