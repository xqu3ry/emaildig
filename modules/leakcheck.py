import requests
import json
import api_keys
import limits

api_key = api_keys.leakcheck
limit = limits.leakcheck

def leakcheck(email):
    url = f'https://leakcheck.io/api/public?key={api_key}&check={email}'
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        print("HTTP status:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            if data.get('success') and data.get('sources'):
                for i, leak in enumerate(data['sources'][:limit]):
                    print(f"    Result {i + 1}:")
                    print(f"        Source: {leak.get('name', 'Not given')}")
                    print(f"        Breach date: {leak.get('date', 'Not given')}")
            else:
                print(f'    No leaks found for {email}.')
        else:
            print(f'    Error {response.status_code}: request failed.')

    except Exception as e:
        print(f'    Exception occurred: {e}')
