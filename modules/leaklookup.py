import requests
import json
import api_keys
import limits

limit = limits.leaklookup
api_key = api_keys.leaklookup

def leaklookup(email):
    url = "https://leak-lookup.com/api/search"

    payload = {
        "key": api_key,
        "type": "email_address",
        "query": email
    }

    response = requests.post(url, data=payload)

    
    result = response.json()

    if "message" in result:
        message_data = result["message"]

        
        if isinstance(message_data, dict):
            
            truncated_data = list(message_data.items())[:limit]

            for key, value in truncated_data:
                print(f"    {key}: {value}")
        elif isinstance(message_data, str):
            
            print(f"    Message: {message_data}")
        else:
            print("    Error: unexpected data type for message_data")
    else:
        print("    Failed to get data.")
