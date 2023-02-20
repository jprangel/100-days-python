import requests

class Conn:
    
    def __init__(self) -> None:
        pass
    
    def post_req(self, query_json: str, endpoint: str, header: str):
        """ Open a connection with the endpoint"""
        r = requests.post(url=endpoint, json=query_json, headers=header)
        r_json = r.json()
        r.raise_for_status()
        return r_json