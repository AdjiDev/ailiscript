# plugins/traceroute.py

import requests
import json

def traceroute_lookup(ip):
    url = f"http://api.traceroute.me/v1/traceroute/{ip}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        if data.get('success', False):
            pretty_data = json.dumps(data['result'], indent=4)
            return pretty_data
        else:
            return f"Error: {data.get('message', 'Unable to retrieve data')}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
