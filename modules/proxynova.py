import requests
import json
import limits
limit = limits.proxynova

def proxynova(email):

    url = "https://api.proxynova.com/comb"
    
    params = {
        "query": email,
        "start": 0,
        "limit": limit
    }

    response = requests.get(url, params=params)

    if response.ok:
        
        try:
            data = response.json()
        
        
            for line in data.get("lines", []):
                
                print("    " + line)
        
        except ValueError:
            
            print("    Failed to parse JSON:")
            
            print(response.text)
    
    else:
        print(f"    Request error: {response.status_code}")
