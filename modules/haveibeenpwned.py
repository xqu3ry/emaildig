import requests
import api_keys
import limits


api_key = api_keys.haveibeenpwned

limit = limits.haveibeenpwned


def haveibeenpwned(email):
    
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    
    headers = {
        'User-Agent': 'Python-HIBP-Script',
        'Authorization': f'Bearer {api_key}',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        
        breaches = response.json()
        
        if breaches:
            
            limited_breaches = breaches[:limit]  
            
            print(f'    Email "{email}" not found in {len(breaches)} leaks (showed first {limit}):\n')
            
            for i, breach in enumerate(limited_breaches, 1):
                
                print(f"[{i}] {breach.get('Title', 'No title')} ({breach.get('BreachDate', 'No date')})")
                
                print(f"    Description: {breach.get('Description', '').strip()[:300]}...\n")
        else:
            
            print(f'    Email "{email}" not found in leaks.\n')
    
    elif response.status_code == 404:
        
        print(f'    Email "{email}" not found in leaks.\n')
    
    elif response.status_code == 401:
        
        print(f'    Error 401: Wrong API key.\n')
    
    else:
        
        print(f'    Error {response.status_code}: failed to get info for {email}\n')
