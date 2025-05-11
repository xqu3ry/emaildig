import requests
import api_keys

api_key = api_keys.emailrep


def emailrep(email):
    
    url = f'https://emailrep.io/{email}'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'User-Agent': 'Python-EmailRep-Script',
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        
        data = response.json()
        
        
        reputation = data.get('reputation', 'unknown')
        
        risk = data.get('risk', 'unknown')
        
        threats = ', '.join(data.get('threats', [])) or 'no threats'

        print(f'    Reputation for {email}: {reputation}')
        print(f'    Risk: {risk}')
        print(f'    Threats: {threats}\n')
        
    elif response.status_code == 404:
        
        print(f'    Email {email} not found in Emailrep database.\n')
    
    else:
        
        print(f'    Error {response.status_code}: failed to get info for {email}\n')


