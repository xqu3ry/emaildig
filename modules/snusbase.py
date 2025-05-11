import requests
import json
import api_keys
import limits

api_key = api_keys.snusbase

limit = limits.snusbase

def snusbase(email):
    
    url = 'https://api.snusbase.com/data/search'
    
    headers = {
        'Content-Type': 'application/json',
        'Auth': api_key
    }
    
    data = {
        'terms': [email],
        'types': ['email']
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        
        results = response.json()
        
        if results:
            
            
            
            for i, result in enumerate(results[:limit]):
                
                print(f"   Result {i + 1}:")
                print(f"      Source: {result.get('source', 'Not given')}")
                print(f"      Breach date: {result.get('date', 'Not given')}")
                print(f"      Description: {result.get('description', 'No description')}")
                
                for key, value in result.items():
                    
                    if key not in ['source', 'date', 'description']:  
                        
                        print(f"  {key.capitalize()}: {value}")
                
                print('-' * 60)
        else:
            
            print(f'    Email {email} not found in databases.\n')
    
    else:
        
        print(f'    Error {response.status_code}: failed to get info for {email}\n')

