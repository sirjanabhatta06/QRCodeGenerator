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
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
        qr.add_data(elem)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img.save("Test.png")
        
    print(f"-------- Done creating QR codes.---------")

if __name__=="__main__":
    main()