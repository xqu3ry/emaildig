import requests
import api_keys

api_key = api_keys.hunter

def hunter(email):
    
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"

    response = requests.get(url)

    if response.ok:
        
        data = response.json()
        
        
    
        print(f"    Email: {email}")
        print(f"    Result: {data.get('data', {}).get('result')}")
        print(f"    Score: {data.get('data', {}).get('score')}")
        print(f"    Did you mean: {data.get('data', {}).get('did_you_mean')}")
        print(f"    MX Records: {data.get('data', {}).get('mx_records')}")
        print(f"    SMTP Provider: {data.get('data', {}).get('smtp_provider')}")
    
    else:
        
        print(f"    Error: {response.status_code}")
