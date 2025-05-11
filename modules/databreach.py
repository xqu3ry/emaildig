import requests
import limits
import api_keys

api_key = api_keys.databreach  

limit = limits.databreach


def databreach(email):
    
    url = "https://databreach.com/api/v2/scan"
    
    
    body = {
        "query": [
            {"field": "email", "value": email}
        ]
    }
    
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    
    
    response = requests.post(url, json=body, headers=headers)
    
    
    print(f"    Server response: {response.status_code}")
    
    print(f"    Server response (JSON): {response.json()}")
    
    if response.status_code == 200:
        
        data = response.json()
        
        if data.get("found", 0) > 0:
            
            breach = data.get("breaches", [])[:limit]  
            print(f"\n    Found breach for {email}:")
            print(f"    Breach: {breach['name']}")
            print(f"    Breach date: {breach['breach_date']}")
            print(f"    Description: {breach['summary']}")
            print(f"    Number of records: {breach['rows']}")
            print(f"    Icon: {breach['icon']}")
        
        else:
            
            print(f"\n    For {email} leaks not found.")
    
    elif response.status_code == 401:
        
        print("\n    Error: API key not provided or wrong.")
    
    else:
        print(f"\n    Error {response.status_code}: Faled to get info for {email}")


