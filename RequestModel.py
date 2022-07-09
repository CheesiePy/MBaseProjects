import requests
import WebTools

class RequestHandler:
    def __init__(self, url):
        self.url = url
        self.ws = WebTools.WebScraper(url)

    def get_request(self):
        response = requests.get(self.url)
        return response.text

    def post_request(self, data):
        response = requests.post(self.url, data=data)
        return response.text

    def put_request(self, data):
        response = requests.put(self.url, data=data)
        return response.text

    def delete_request(self):
        response = requests.delete(self.url)
        return response.text

    def post_login_request(self, username, password):
        response = requests.post(self.url, data={'username': username, 'password': password}, allow_redirects=True)
        return response.text

    def download_source(self):
        response = requests.get(self.url)
        playFile = open(self.ws.get_title()+'.txt', 'wb')
        for chunk in response.iter_content(100000):
            playFile.write(chunk)


url = 'https://is.telhai.ac.il/nidp/idff/sso?id=TelHai&sid=0&option=credential&sid=0&target=https%3A%2F%2Fportal.telhai.ac.il%2F'
res = requests.get(url)

rh = RequestHandler(url)


# print(res.status_code)

# file_dest = 'requests_docs.txt'
# playFile = open(file_dest, 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()