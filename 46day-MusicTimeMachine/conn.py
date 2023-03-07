import requests

class Conn:
    
    def __init__(self) -> None:
        pass
    
    def get_request(self, url: str):
        """ Get request to a URL"""
        response = requests.get(url)
        website_content = response.text 
        response.raise_for_status()
        return website_content
    