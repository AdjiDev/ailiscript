import requests
import json

BASE_URL = "https://widipe.com/prompt/gpt"

HEADERS = {
    'Content-Type': 'application/json'
}

def send_prompt(prompt, text):
    """
    Send a prompt to the API endpoint and retrieve the response.
    
    Args:
        prompt (str): The prompt to be sent (e.g., the name to assign).
        text (str): The text for the chatbot to respond to.
        
    Returns:
        str: The chatbot's response or an error message.
    """
    params = {
        "prompt": prompt,
        "text": text
    }
    
    try:
        response = requests.get(BASE_URL, params=params, headers=HEADERS)
        
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("status"):
            return data.get("result", "No result provided by the API.")
        else:
            return "API returned an error: no valid response."
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
"""
if __name__ == "__main__":
    prompt = "Your name is aili"
    text = "hi"
    
    result = send_prompt(prompt, text)
    
    print(result)
"""
