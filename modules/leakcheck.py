import requests
import json
import api_keys
import limits

api_key = api_keys.leakcheck

limit = limits.leakcheck

def leakcheck(email):
    
    url = f'https://leakcheck.io/api/public?key={api_key}&check={email}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        data = response.json()
        
        
        if data.get('success') == True and data.get('sources'):
            
            leaks = data['sources']
            
            
            
            for i, leak in enumerate(leaks[:limit]):
                print(f"    Result {i + 1}:")
                print(f"        Source: {leak.get('name', 'Not given')}")
                print(f"        Breach date: {leak.get('date', 'Not given')}")
                
        
        else:
            
            print(f'    For {email} found no leaks, or there is error on server.\n')
    
    else:
        
        print(f'    Error {response.status_code}: failed to get info for {email}\n')


