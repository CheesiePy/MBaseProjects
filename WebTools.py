import webbrowser


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.html = self.get_html()
        self.title = self.get_title()
        self.text = self.get_text()

    def get_html(self):
        import requests
        response = requests.get(self.url)
        return response.text

    def get_url(self):
        return self.url

    def get_html_forms(self):
        import re
        forms = re.findall('<form.*</form>', self.html)
        return forms

    def get_title(self):
        import re
        title = re.search('<title>(.*)</title>', self.html)
        return title.group(1)

    def get_section(self, section_name):
        import re
        section = re.findall('<section id="' + section_name + '">(.*)</section>', self.html)
        return section

    def get_section_text(self, section_name):
        import re
        text = re.findall('<section id="' + section_name + '">(.*)</section>', self.html)
        return text

    def get_all_sections(self):
        import re
        sections = re.findall('<section>(.*)</section>', self.html)
        return sections

    def get_text(self):
        import re
        text = re.findall('<p>(.*)</p>', self.html)
        return text

    def find_downloadable_links(self):
        import re
        links = re.findall('<a href="(.*)"', self.html)
        return links


    def login(self, login_url, username, password):
        import requests
        response = requests.post(login_url, data={'username': username, 'password': password}, allow_redirects=True)
        return response.text


class Webrowser:
    import webbrowser
    import FileManagerUtils
    def __init__(self):
        chrome_path = self.FileManagerUtils.find_file_and_return_dir('chromedriver.exe')
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        self.webbrowser = webbrowser.get('chrome')

    def open_url(self, url):
        self.url = url
        self.webbrowser.open(self.url)

