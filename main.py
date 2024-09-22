import os
import socket
import sys
from colorama import init, Style
from lib.menu import data1, data2, data3, data4
#from lib.ngetik import adji
from plugins import subdo
from plugins.basic_v1 import send_req_basic_v1
from plugins.basic_v2 import send_requests_with_timeout_v2
from plugins.basic_v3 import send_requests_with_proxies_and_ua_v3
from plugins.bypass_v1 import send_req_bypass_v1
from plugins.bypass_v2 import bypass_test_v2, send_req_bypass_v2
from plugins.bypass_v3 import bypass_test_v3, send_req_bypass_v3
from plugins.syn_floods import syn_flood_test
from plugins.chatgpt import send_prompt
from plugins.bing_scraper import bing_search
from plugins.tls_basic import send_requests_with_timeout_basic_tls_v1
from plugins.tls_advanced import send_requests_with_timeout_tls_v3
from plugins.traceroute import traceroute_lookup
from plugins.geolocation import search_maps, lat_lon_lookup
from plugins.whois import whois_lookup
from plugins.wifimap import scan_wifi

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gradient_banner(text):
    start_color = (0, 255, 255)  #warna pink
    end_color = (255, 0, 255)  #warna kunig
    steps = len(text)
    
    for i in range(steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // steps
        g = start_color[1] + (end_color[1] - start_color[1]) * i // steps
        b = start_color[2] + (end_color[2] - start_color[2]) * i // steps
        
        color = f"\033[38;2;{r};{g};{b}m"
        print(color + text[i], end="")
    print(Style.RESET_ALL)

def gradient_text(text):
    start_color = (255, 182, 193)  # Biru
    end_color = (0, 255, 255)  # Magenta
    steps = len(text)
    
    gradient_output = ""
    for i in range(steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // steps
        g = start_color[1] + (end_color[1] - start_color[1]) * i // steps
        b = start_color[2] + (end_color[2] - start_color[2]) * i // steps
        
        color = f"\033[38;2;{r};{g};{b}m"
        gradient_output += color + text[i]
    
    gradient_output += Style.RESET_ALL
    return gradient_output

def get_hostname():
    """Returns the current hostname."""
    return socket.gethostname()

def get_current_directory():
    """Returns the current working directory."""
    return os.getcwd()

def main():
    banner = """
    A       I      L     I     S      C        R      I       P      T
_________________________________________________________________________
___    |___  _/__  /____  _/_  ___/_  ____/__  __ \___  _/__  __ \__  __/ # Adjisan junior dev
__  /| |__  / __  /  __  / _____ \_  /    __  /_/ /__  / __  /_/ /_  /  # 2024 ailibytes.xyz
_  ___ |_/ /  _  /____/ /  ____/ // /___  _  _, _/__/ /  _  ____/_  / # Licensed By Apache 2    
/_/  |_/___/  /_____/___/  /____/ \____/  /_/ |_| /___/  /_/     /_/# Version 2.0.1_alpha

# For student and educational purposes only😀
# Telegram     : https://t.me/rizkykianadji
    """
    
    gradient_banner(banner)
    
    while True:
        try:
            hostname = get_hostname()
            text = f"""ailiscript@{hostname}~# """
            gradient_out = gradient_text(text)
            shell_input = input(gradient_out)

            if shell_input.lower() in ["exit", "quit"]:
                print("Exiting AILIScript...")
                sys.exit()

            elif shell_input.lower().startswith("basicv1") or shell_input.lower().startswith("bv1"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 4:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        send_req_basic_v1(url, packets, threads)
                    else:
                        print("Usage: basicv1 <url> <packets> <threads>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("tlsbasic"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 4:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        send_requests_with_timeout_basic_tls_v1(url, packets, threads)
                    else:
                        print("Usage: tlsbasic <url> <packets> <threads>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("tlsadv"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 5:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        proxy = parts[4]
                        send_requests_with_timeout_tls_v3(url, packets, threads, proxy)
                    else:
                        print("Usage: tlsadv <url> <packets> <threads> <proxy>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("basicv3") or shell_input.lower().startswith("bv3"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 5:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        proxy = parts[4]
                        ua = "ua.txt"  # User-Agent file
                        send_requests_with_timeout_tls_v3(url, packets, threads, proxy, ua)
                    else:
                        print("Usage: basicv3 <url> <packets> <threads> <proxy>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("bypassv1") or shell_input.lower().startswith("bs1"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 5:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        send_req_bypass_v1(url, packets, threads)
                    else:
                        print("Usage: bypassv1 <url> <packets> <threads>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("bypassv2") or shell_input.lower().startswith("bv2"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 5:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        proxies_file = parts[4]  # Proxies file
                        user_agents_file = 'user_agents.txt'  # Default User-Agent file
                        bypass_test_v2(url, packets=packets, threads=threads, proxies_file=proxies_file, user_agents_file=user_agents_file)
                    else:
                        print("Usage: bypassv2 <url> <packets> <threads> <proxies_file>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("bypassv3") or shell_input.lower().startswith("bv3"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 5:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        proxies_file = parts[4]  # Proxies file
                        user_agents_file = 'user_agents.txt'  # Default User-Agent file
                        bypass_test_v3(url, packets=packets, threads=threads, proxies_file=proxies_file, user_agents_file=user_agents_file)
                    else:
                        print("Usage: bypassv3 <url> <packets> <threads> <proxies_file>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("synflood") or shell_input.lower().startswith("syn"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 4:
                        ip = parts[1]
                        port = int(parts[2])
                        packets = int(parts[3])
                        threads = 10  # Default number of threads
                        syn_flood_test(ip, port, packets=packets, threads=threads)
                    else:
                        print("Usage: synflood <ip> <port> <packets>")
                except ValueError:
                    print("Error: Port and packets must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("bing"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 3:
                        query = parts[1]
                        length = int(parts[2])
                        results = bing_search(query, length)

                        for result in results:
                            print(f"Title: {result['title']}\nLink: {result['link']}\nSnippet: {result['snippet']}\n")
                    else:
                        print("Usage: bing <query> <length>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("geoloc"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 2:
                        location = parts[1]
                        result = search_maps(location)
                        print(result)
                    else:
                        print("Usage: geoloc <location>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("latlon"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 3:
                        lat = float(parts[1])
                        lon = float(parts[2])
                        address = lat_lon_lookup(lat, lon)
                        print(address)
                    else:
                        print("Usage: latlon <latitude> <longitude>")
                except ValueError:
                    print("Error: Latitude and longitude must be numbers.")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("ask"):
                try:
                    parts = shell_input.split(maxsplit=2)
                    if len(parts) == 3:
                        prompt = parts[1]
                        text = parts[2]
                        result = send_prompt(prompt, text)
                        print(result)
                    else:
                        print("Usage: chat <prompt> <text>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("traceroute"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 2:
                        ip = parts[1]
                        result = traceroute_lookup(ip)
                        print(result)
                    else:
                        print("Usage: traceroute <ip>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("whois"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 2:
                        ip = parts[1]
                        result = whois_lookup(ip)
                        print(result)
                    else:
                        print("Usage: whois <ip>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower() in ["stresser", "ddos", "stress", "ddosmenu"]:
                data1()

            elif shell_input.lower() in ["osint", "findinfo", "info", "trackmenu"]:
                data2()

            elif shell_input.lower() in ["help", "h", "?"]:
                data3()

            elif shell_input.lower() in ["other", "misc", "othermenu"]:
                data4()

            elif shell_input.lower() in ["cls", "clear"]:
                clear()
                main()

            elif shell_input.lower() in ["wifimap", "wifi"]:
                scan_wifi()
            
            elif shell_input.lower().startswith("subdo"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 2:
                        domain = parts[1]
                        result = subdo(domain)
                        print(result)
                    else:
                        print("Usage: subdo <domain>")
                except Exception as e:
                    print(f"Error: {e}")

            elif shell_input.lower().startswith("basicv2") or shell_input.lower().startswith("bv2"):
                try:
                    parts = shell_input.split()
                    if len(parts) == 4:
                        url = parts[1]
                        packets = int(parts[2])
                        threads = int(parts[3])
                        send_requests_with_timeout_v2(url, packets, threads)
                    else:
                        print("Usage: basicv2 <url> <packets> <threads>")
                except ValueError:
                    print("Error: Packets and threads must be integers.")
                except Exception as e:
                    print(f"Error: {e}")

            else:
                print(f"You entered: {shell_input}")

        except KeyboardInterrupt:
            print("\nUser interrupted, exiting...")
            break



if __name__ == "__main__":
    clear()
    main()
