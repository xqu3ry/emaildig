import requests
import api_keys

api_key = api_keys.ipqualityscore

def ipqualityscore(email):

    url = f"https://www.ipqualityscore.com/api/json/email/{api_key}/{email}"

    response = requests.get(url)

    if response.ok:
        
        data = response.json()

        print(f"    Email: {email}")
        print(f"    Valid: {data.get('valid')}")
        print(f"    Deliverability: {data.get('deliverability')}")
        print(f"    Disposable: {data.get('disposable')}")
        print(f"    Catch-All: {data.get('catch_all')}")
        print(f"    Spam Trap Score: {data.get('spam_trap_score')}")
        print(f"    Fraud Score: {data.get('fraud_score')}")
        print(f"    DNS Valid: {data.get('dns_valid')}")
        print(f"    Domain Age: {data.get('domain_age', {}).get('human')}")
        print(f"    First Seen: {data.get('first_seen', {}).get('human')}")
        print(f"    Sanitized Email: {data.get('sanitized_email')}")
        print(f"    MX Records:")
        
        for mx in data.get("mx_records", []):
            
            print(f"  - {mx}")
        
        print(f"A Records:")
        
        for a in data.get("a_records", []):
            
            print(f"  - {a}")
    
    else:
        
        print(f"    Error: {response.status_code}")
