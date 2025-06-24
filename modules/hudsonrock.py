import requests

def check_email(email):
    url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={email}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        

        
        stealers = data.get("stealers", [])
        if not stealers:
            print("    No infostealer data found.")
            return

        for entry in stealers:
            print("\nInfected Device Info:")
            print(f"    Computer:       {entry.get('computer_name')}")
            print(f"    OS:             {entry.get('operating_system')}")
            print(f"    Malware Path:   {entry.get('malware_path')}")
            print(f"    Compromised:    {entry.get('date_compromised')}")
            print(f"    IP:             {entry.get('ip')}")
            print(f"    Antiviruses:    {', '.join(entry.get('antiviruses', []))}")
            print(f"    Corp Services:  {entry.get('total_corporate_services')}")
            print(f"    User Services:  {entry.get('total_user_services')}")

            print("\n    Top Passwords:")
            for pw in entry.get("top_passwords", []):
                print(f"    - {pw}")

            print("\n    Top Logins:")
            for login in entry.get("top_logins", []):
                print(f"    - {login}")

    except Exception as e:
        print(f"    Error: {e}")
