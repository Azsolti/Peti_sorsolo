import requests

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    RESET = '\033[0m'
    

class Request:
    def __init__(self, url):
        self.url = url
        

    def return_text(self):
        response = requests.get(self.url)
        print(response.text)


    def serialize_data(self,*args ,**kwargs):
        
        if "get" in args:
          self.url = url + "/get"
          response = requests.get(self.url, **kwargs)
        elif "post" in args:
          self.url = url + "/post"
          response = requests.post(self.url, **kwargs)
        else:
          response = requests.get(self.url, **kwargs)
        
        headers_dict = ''.join(f'\n{Colors.GREEN}{k.upper()}{Colors.RESET}: {Colors.BLUE}{v}{Colors.RESET}' for k, v in response.headers.items())
        json_dict = ''.join(f'\n{Colors.GREEN}{k}{Colors.RESET}: {Colors.BLUE}{v}{Colors.RESET}' for k, v in response.json().items())
        text_str = '\n'.join(response.text.split('\n'))
        print(headers_dict, json_dict, text_str)
        # print(f"""JSON :\n\t{json_dict}\nTEXT :\n\t{text_str}\nHEADERS :\n\t{headers_dict}""")

    def post_all(self, **kwargs):
        response = requests.post(self.url, **kwargs)
        
      
url = "https://httpbin.org"        
payload = {"xxx": "xxx", "gbhsgba": "heahaqaokok"}  

o = Request(url)
o.serialize_data()
