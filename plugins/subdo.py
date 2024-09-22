import requests
import pandas as pd
import sys

def get_subdomains(domain):
    url = f"https://widipe.com/subdomain?domain={domain}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("status"):
            return data["data"]
        else:
            print("No subdomains found.")
            return []
    else:
        print(f"Failed to fetch subdomains: {response.status_code}")
        return []

def check_status_code(subdomain):
    try:
        response = requests.get(f"http://{subdomain}", timeout=5)
        return response.status_code
    except requests.exceptions.Timeout:
        print(f"Timeout accessing {subdomain}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error accessing {subdomain}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {subdomain}: {e}")
        return None

def subdo(domain):
    subdomains = get_subdomains(domain)
    results = []

    for sub in subdomains:
        status_code = check_status_code(sub)
        results.append({"SUBDOMAIN": sub, "STATUS CODE": status_code})

    df = pd.DataFrame(results)
    print(df)
    df.to_csv("subdomain_status.csv", index=False)

