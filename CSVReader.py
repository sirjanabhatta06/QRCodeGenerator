import csv

class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv_file(self):
        websites_list = []
        count = 0
        try:  
            with open(self.file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                header = next(reader)
                for row in reader:
                    websites_list.append(row[1])
                    count = count + 1
                    if count > 1000:
                        break
            return websites_list
        except FileNotFoundError as file_not_found:
            print(f"The file {self.file_path} does not exist {file_not_found}")
        except Exception as e:
            print(f"Error while running file {e}")
    