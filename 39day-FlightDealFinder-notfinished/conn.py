import requests
import urllib.parse

class Conn:
    
    def __init__(self) -> None:
        pass
    
    def post_req(self, query_json: str, endpoint: str, header: str):
        """ Open a connection with the endpoint"""
        r = requests.post(url=endpoint, json=query_json, headers=header)
        r_json = r.json()
        r.raise_for_status()
        return r_json
    
    def get_req(self, endpoint: str, header: str, param: str):
        param = urllib.parse.urlencode(param, safe='/')
        r = requests.get(url=endpoint, headers=header, params=param)
        r_json = r.json()
        r.raise_for_status()
        return r_json