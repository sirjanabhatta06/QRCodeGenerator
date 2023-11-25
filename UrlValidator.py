import requests

class Validator:
    https = ""
    valid_websites_list = []
    def __init__(self):
        self.https = "https://"
        self.valid_websites_list = []
    def Validate (self, websites_list):
        for url in websites_list:
            try: 
                # response = requests.get(self.https + url)
                # if(response.status_code == 200):
                #     self.valid_websites_list.append(self.https+url)
                
                response = requests.head((self.https + url), allow_redirects=True)
                if (response.status_code >= 200 and response.status_code < 400):
                    self.valid_websites_list.append(self.https+url)
                    
            except requests.exceptions.RequestException:
                pass
        return self.valid_websites_list