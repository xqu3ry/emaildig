import requests
import limits

limit = limits.breachdirectory

def breachdirectory(email):

    url = "https://api.breachdirectory.org/rapidapi-IscustemTaingtowItrionne"
    
    params = {
        "func": "auto",
        "term": email
    }
    
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        
        data = response.json()

        if "result" in data and isinstance(data["result"], list):
            
            breaches = data["result"][:limit]
            
            print(f"\n    Found entries: {data.get('found', len(breaches))} (showing first 10):\n")
            
            for i, entry in enumerate(breaches, 1):
                
                print(f"        {i}.Email: {entry.get('email')}")
                print(f"            Password: {entry.get('password')}")
                print(f"            SHA1: {entry.get('sha1')}")
                print(f"            Hash: {entry.get('hash')}")
                print(f"            Hash Password: {entry.get('hash_password')}")
                print(f"            Source: {entry.get('sources')}\n")
        
        else:
            
            print("    Entries Not Found.")
    
    else:
        
        print(f"    Error when requesting: {response.status_code}")
