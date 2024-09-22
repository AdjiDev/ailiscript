import requests
from bs4 import BeautifulSoup

def bing_search(query, length=10):
    query = query.replace(' ', '+')
    
    url = f'https://www.bing.com/search?q={query}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        search_results = soup.find_all('li', class_='b_algo')
        
        results = []
        
        for idx, result in enumerate(search_results):
            if idx >= length:
                break
            
            title = result.find('h2').text if result.find('h2') else 'No title'
            link = result.find('a')['href'] if result.find('a') else 'No link'
            snippet = result.find('p').text if result.find('p') else 'No snippet'
            
            results.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
        
        return results
    else:
        return f"Error: Unable to reach Bing. Status code {response.status_code}"

# query = "ailibytes"
# length = 5
# results = bing_search(query, length)

# for result in results:
#    print(f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n")
