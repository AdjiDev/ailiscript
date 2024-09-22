import requests
import json

NOMINATIM_URL = "https://nominatim.openstreetmap.org"

HEADERS = {
    'User-Agent': 'Ailibytes-Security/2.0.1 ( support@ailibytes.xyz )'
}

def pretty_print(data):
    """Utility function to pretty-print JSON data."""
    return json.dumps(data, indent=4, ensure_ascii=False)

def search_maps(query=""):
    """Search for a location using the Nominatim OSM search API."""
    if not query:
        return "Query is required to search maps."

    url = f"{NOMINATIM_URL}/search"
    
    params = {
        'q': query,
        'format': 'json',  
        'addressdetails': 1,  
        'limit': 1  
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status() 
        data = response.json()
        
        if not data:
            return "No results found."
        
        return pretty_print(data[0])  
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the request: {str(e)}"

def lat_lon_lookup(lat, lon):
    """Look up address using latitude and longitude (reverse geocoding)."""
    if not lat or not lon:
        return "Latitude and Longitude are required."

    url = f"{NOMINATIM_URL}/reverse"
    
    params = {
        'lat': lat,
        'lon': lon,
        'format': 'json',  
        'addressdetails': 1  
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()  
        data = response.json()
        
        if 'error' in data:
            return f"Error: {data['error']}"
        
        return pretty_print(data.get('address', 'No address found for these coordinates.'))
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred during the request: {str(e)}"

if __name__ == "__main__":
    result = search_maps("Berlin, Germany")
    print(result)
    
    address = lat_lon_lookup(52.5200, 13.4050)  
    print(address)
