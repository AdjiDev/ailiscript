from colorama import init, Style

# Initialize Colorama
init()

def gradient(text):
    start_color = (0, 255, 0)  # Pink
    end_color = (255, 165, 0)      # Magenta
    steps = len(text)
    
    for i in range(steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // steps
        g = start_color[1] + (end_color[1] - start_color[1]) * i // steps
        b = start_color[2] + (end_color[2] - start_color[2]) * i // steps
        
        color = f"\033[38;2;{r};{g};{b}m"
        print(color + text[i], end="")
    print(Style.RESET_ALL)

data = r"""
─────────────────────────────────────────────────────────────────────────────────────
|     NAME     |     COMMANDS     |     TIMEOUT     |          DESCRIPTION          |
─────────────────────────────────────────────────────────────────────────────────────
| Basic V1     | basicv1, bv1     | NaN             | Basic http floods             |
| Basic V2     | basicv2, bv2     | 2 Minutes       | Basic http floods with header |
| Basic V3     | basicv3, bv3     | 2 Minutes       | Basic fully proxied attack    |
| Bypass V1    | bypassv1, bsv1   | 2 Minutes       | Basic bypass                  |
| Bypass V2    | bypassv2, bsv2   | 2 Minutes       | Basic bypass proxied          |
| Bypass V3    | bypassv2, bsv3   | 2 Minutes       | Bypass fully proxied attack   |
| Syn floods   | syn              | NaN             | Basic Syn floods              |
| ping         | ping             | NaN             | Ping floods                   |
| tcp          | tcp              | NaN             | Basic tcp floods              |
| tlsv1        | tlsbasic         | 2 Minute        | Basic tls floods              |
| tlsv2        | tlsadv           | 2 Minute        | Basic tls chance to bypass    |
─────────────────────────────────────────────────────────────────────────────────────
# Version 2.0.1
# Licensed by Apache 2
# Credits: support@ailibytes.xyz

Disclaimer: 
This program is intended for educational and testing purposes only. 
Unauthorized use of this tool may violate laws and regulations.
"""

data_2 = r"""
────────────────────────────────────────────────────────────────────────────
|   NO   |     NAME     |     COMMANDS     |          DESCRIPTION          |
────────────────────────────────────────────────────────────────────────────
|   1    | Whois        | whois, ipinfo    | IP info iPs                   |
|   2    | Traceroute   | traceroute, trace| Trace route to a destination  |
|   3    | DNS Lookup   | nslookup, dig    | Lookup DNS records            |
|   4    | Geolocation  | geoloc, location | Search infomation location    |
|   5    | Subdomain    | subdo, subdomain | Find hidden subdomain         |
|   6    | Wifi MAP     | wifimap          | Find WiFi BSSID in range      |
────────────────────────────────────────────────────────────────────────────
"""

data_other = """
────────────────────────────────────────────────────────────────────────────
|   NO   |     NAME     |     COMMANDS     |          DESCRIPTION          |
────────────────────────────────────────────────────────────────────────────
|   1    | Chatgpt      | ask              | Ask Ai                        |
|   2    | Bing search  | bing             | Bing search                   |
────────────────────────────────────────────────────────────────────────────
"""

info = """
~ ?, h, help - show help menu
~ stress, ddos, stresser - show ddos menu
~ osint, findinfo, trackmenu - show tracker menu
~ other, misc ~ show misc menu

Note:
~ Please use VPN for using this script thank you
"""

def data1():
    gradient(data)

def data2():
    gradient(data_2)

def data3():
    gradient(info)

def data4():
    gradient(data_other)

data1()
data2()
