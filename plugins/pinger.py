import sys
import threading
from scapy.all import ICMP, IP, sr1
from time import sleep

class ICMPPinger:
    def __init__(self, target, max_packets, num_threads):
        self.target = target
        self.max_packets = max_packets
        self.num_threads = num_threads

    def send_ping(self, count, thread_id):
        for i in range(count):
            packet = IP(dst=self.target) / ICMP()
            response = sr1(packet, timeout=1, verbose=False)

            if response:
                print(f"[+] Thread {thread_id}: Ping {i + 1} to {self.target}: Reply from {response.src}")
            else:
                print(f"[-] Thread {thread_id}: Ping {i + 1} to {self.target}: No response")
            sleep(1)

    def start(self):
        packets_per_thread = self.max_packets // self.num_threads

        print(f"Starting ICMP ping test to {self.target} with {self.max_packets} packets and {self.num_threads} threads.")

        threads = []
        for thread_id in range(self.num_threads):
            thread = threading.Thread(target=self.send_ping, args=(packets_per_thread, thread_id + 1))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

def main():
    if len(sys.argv) != 4:
        print("Usage: python ping_icmp.py <ip/domain> <max_packets> <threads>")
        sys.exit(1)

    target = sys.argv[1]
    max_packets = int(sys.argv[2])
    num_threads = int(sys.argv[3])

    print("Starting Ping Test")
    print(f"Target: {target}")
    print(f"Max Packets: {max_packets}")
    print(f"Threads: {num_threads}\n")

    pinger = ICMPPinger(target, max_packets, num_threads)
    pinger.start()

if __name__ == "__main__":
    main()
