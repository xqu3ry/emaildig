import requests
import limits
import api_keys

api_key = api_keys.dehashed  

limit = limits.dehashed

def dehashed(email):
    
    url = "https://api.dehashed.com/v2/search"
    
    headers = {
        "Dehashed-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "query": email,
        "page": 1,
        "size": limit,  
        "wildcard": False,
        "regex": False,
        "de_dupe": True
    }

    try:
        
        response = requests.post(url, json=payload, headers=headers)
        
        data = response.json()

        

        if "error" in data:
            
            print(f"    Error: {data['error']}")
            
            return

        entries = data.get("entries", [])
        
        if not entries:
            
            print(f"    Nothing found for {email}.")
            
            return

        print(f"\nFound {len(entries)} entries for {email}:\n")
        
        for i, entry in enumerate(entries[:10], 1):
            
            print(f"    --- Entry #{i} ---")
            
            if "email" in entry: print("        Email:", ", ".join(entry["email"]))
            
            if "username" in entry: print("        Username:", ", ".join(entry["username"]))
            
            if "password" in entry: print("        Password:", ", ".join(entry["password"]))
            
            if "ip_address" in entry: print("        IP:", ", ".join(entry["ip_address"]))
            
            if "database_name" in entry: print("        Database:", entry["database_name"])
            
            print()

    except requests.exceptions.RequestException as e:
        
        print(f"    Request error: {e}")
    
    except Exception as e:
        
        print(f"    Unexpected error: {e}")

