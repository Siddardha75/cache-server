

import requests

def fetch_from_server(url):
    response = requests.get(url)
    return {
      
        "body" : response.content,
        "status_code" : response.status_code,
        "headers" : dict(response.headers)

    }
