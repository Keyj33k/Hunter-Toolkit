from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from termcolor import colored
from datetime import datetime
from threading import Thread
from scapy.all import *
import phonenumbers
import requests
import hashlib
import socket
import base64
import socket
import pandas
import time
import sys
import os
import re


def banner():   
   print("""
         █    █                 █
         █    █                 █
         █    █ █   █  █▒██▒  █████   ███    █▒██▒
         █    █ █   █  █▓ ▒█    █    ▓▓ ▒█   ██  █
         ██████ █   █  █   █    █    █   █   █
         █    █ █   █  █   █    █    █████   █
         █    █ █   █  █   █    █    █       █
         █    █ █▒ ▓█  █   █    █░   ▓▓  █   █
         █    █ ▒██▒█  █   █    ▒██   ███▒   █
   
     <by@keyjeek>  |  Follow the white rabbit... 
     <contact:nomotikag33n@gmail.com>           
     [i] Hunter is a small toolkit to perform information gathering   
     [i] Type x to exit Hunter.              
     """)
banner()

def HUNT3R():
    def menu():
        print("""
            [1] Witcher
            [2] md5encrypt
            [3] eye
            [4] eye_of_sauron
            [5] base64encode
            [6] WIFI-Stalker    >>     need monitor mode
            [7] Whereareyou
            [x] Exit
    """)
    menu()
    
    def hunter():
        choice = input("[*] Number: ")
        if choice == 'x':
            print("[i] Exit")
            sys.exit()

        elif choice == '1':
            os.system('clear')
            def witcher():
                print("""
                      █                  █
            █     █          █           █
            █░ █ ░█          █           █
            █░▒█▒░█ ███    █████   ▓██▒  █▒██▒   ███    █▒██▒
            ▓▒███▒█   █      █    ▓█  ▓  █▓ ▒█  ▓▓ ▒█   ██  █
            ▒▒█▒█▒▓   █      █    █░     █   █  █   █   █
            ▒██ ██▓   █      █    █      █   █  █████   █
            ▒█▓ ▓█▒   █      █    █░     █   █  █       █
            ░█▒ ▒█▒   █      █░   ▓█  ▓  █   █  ▓▓  █   █
             █   █▒ █████    ▒██   ▓██▒  █   █   ███▒   █
                 <by@keyjeek>  |  Follow the white rabbit...
                 <contact:nomotikag33n@gmail.com>      
                 [i] Witcher is a simple port scanner.  
                 [i] Type x to exit Witcher. 
                """)

                ip_compile = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
                port_min = 0
                print(chr(0xa))
                port_max = int(input("[*] Enter maximum port: \n[*]--> "))
                open_ports = []
                tstart = datetime.now()
                
                while True:
                    target_ip = input("[*] Target IP: \n[*]--> ")
                    if target_ip == 'x':
                        print("[i] Exit")
                        return HUNT3R()
                    elif ip_compile.search(target_ip):
                        print(f"[i] {target_ip} is valid. Please wait, it'll take some time..")
                        print(chr(0xa))
                        def spinning_cursor():
                            while True:
                                for cursor in '|/-\\':
                                    yield cursor
                        spinner = spinning_cursor()
                        print("[i] loading..")
                        for _ in range(port_max):   
                            sys.stdout.write(next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.2)
                            sys.stdout.write('\b')           
                        break
                print(chr(0xa))
                print("[i] Listing open connections..")
                print(chr(0xa))
                try:
                    for port in range(port_min, port_max + 1):
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: ## sock_DGRAM/UPD
                            s.settimeout(0.5) 
                            s.connect((target_ip, port))
                            open_ports.append(port)
                except Exception:
                    os.system('clear')
                    print("Can't connect to target!")
                    time.sleep(3)
                    input("Press any key..")
                    return HUNT3R()
                for port in open_ports:
                    print(f"[+] TCP/{port}  open")
                tend = datetime.now()
                diff = tend - tstart
                print(chr(0xa))
                print("[!] Scan complete in " + str(diff) + " seconds")
                print("[i] Witcher done.")
                print(chr(0xa))
                return HUNT3R()
            witcher() 

        elif choice == '2':
            os.system('clear')
            def md5encrypt():
                def banner():
                    print("""   
                        █
                        █  █████                                              █
                        █  █                                                  █
             ██▓█▓   ██▓█  █       ███   █▒██▒   ▓██▒   █▒██▒ █░  █  █▓██   █████
             █▒█▒█  █▓ ▓█  ████▒  ▓▓ ▒█  █▓ ▒█  ▓█  ▓   ██  █ ▓▒ ▒▓  █▓ ▓█    █
             █ █ █  █   █     ░█▓ █   █  █   █  █░      █     ▒█ █▒  █   █    █
             █ █ █  █   █       █ █████  █   █  █       █      █ █   █   █    █
             █ █ █  █   █       █ █      █   █  █░      █      █▓▓   █   █    █
             █ █ █  █▓ ▓█  █░  █▓ ▓▓  █  █   █  ▓█  ▓   █      ▓█▒   █▓ ▓█    █░
             █ █ █   ██▓█  ▒███▓   ███▒  █   █   ▓██▒   █      ▒█    █▓██     ▒██
                                                               ▒█    █
                                                               █▒    █
                                                              ██     █
            <by@keyjeek>  |  Follow the white rabbit...
            <contact:nomotikag33n@gmail.com>       
            [i] md5encrypt is made to encrypt your string to an 128 bit hash value
            [i] Type x to exit md5encrypt.
                """)
                    
                banner()
                def md5():
                    def encrypt(): 
                        hash_val = input("\n[*] Enter your text to hash: ")
                        if hash_val == 'x':
                            print("[i] Exit")
                            return HUNT3R()
                        result = hashlib.md5(hash_val.encode())
                        print("[+] Result: ", end ="")
                        print(result.hexdigest())
                    encrypt()
                    def decrypt():
                        print(chr(0xa))
                        question_brute = input("[?] Decrypt/bruteforce the hash? y/n: ")
                        if question_brute == 'y':
                            print("[i] Use this Link: https://www.md5online.org/md5-decrypt.html ")## This program is using a big database to bruteforce the hash for you
                            return encrypt()
                        elif question_brute == 'x':
                            print("[i] Exit")
                            return HUNT3R()
                        elif question_brute == 'n':
                            question_exit = input("[?] Do you want to exit? y/n ")
                            if question_exit == 'y':
                                print("[i] Exit")
                                return HUNT3R()
                            elif question_exit == 'x':
                                print("[i] Exit")
                                return HUNT3R()
                            elif question_exit == 'n':
                                return encrypt()
                            else:
                                print("[i] Invalid input")
                                return HUNT3R()
                    decrypt()
                md5()
            md5encrypt()

        elif choice == '3':
            print("""
                 █████  █████░
                   █    █   ▓█
                   █    █    █  ███   █░  █   ███
                   █    █   ▓█ ▓▓ ▒█  ▓▒ ▒▓  ▓▓ ▒█
                   █    █████░ █   █  ▒█ █▒  █   █
                   █    █      █████   █ █   █████
                   █    █      █       █▓▓   █
                   █    █      ▓▓  █   ▓█▒   ▓▓  █
                 █████  █       ███▒   ▒█     ███▒
                                       ▒█
                                       █▒
                                      ██
             <by@keyjeek>  |  Follow the white rabbit...")
             <contact:nomotikag33n@gmail.com>       ")
             [i] IPEye is a Tool to find out
                 --> some information about an IP.  ")
             [i] Type x to exit IPEye.")
            """)
            
            os.system('clear')
            def eye(): 
                scanner = input('[*] IP: ')
                if scanner == 'x':
                    print("[i] Exit")
                    sys.exit()
                elif scanner == "exit":
                    print("[i] Exit")
                    sys.exit
                try:
                    response = requests.post("http://ip-api.com/batch", json=[{"query":scanner}]).json()
                except Exception:
                    print("Can't connect. An error was defined!")
                    print(chr(0xa))
                    input("Press any key to continue..")
                    os.system('clear')
                    return HUNT3R()
                os.system('clear')
                for ip in response:
                    for k, j in ip.items():
                        print(k,j)
                print(chr(0xa))
                print("[i] Scanner done.")
                print(chr(0xa))
                return HUNT3R()
            eye()

        elif choice == '4':
            os.system('clear')
            def eye_of_sauron():
                print("""
                
              ▓███▒   ██   █    █ █████   ▓██▓  ██   █        ███████▒   ▒█ ██████
             █▓  ░█   ██   █    █ █   ▓█ ▒█  █▒ ██░  █        █     ░█   █░ █
             █       ▒██▒  █    █ █    █ █░  ░█ █▒▓  █        █      ▒█ █▒  █
             █▓░     ▓▒▒▓  █    █ █   ▒█ █    █ █ █  █        █       █▓█   █
              ▓██▓   █░░█  █    █ █████  █    █ █ ▓▓ █        ██████  ▒█▒   ██████
                 ▓█  █  █  █    █ █  ░█▒ █    █ █  █ █        █        █    █
                  █ ▒████▒ █    █ █   ░█ █░  ░█ █  ▓▒█        █        █    █
             █░  ▓█ ▓▒  ▒▓ █▒  ▒█ █    █ ▒█  █▒ █  ░██        █        █    █
             ▒████░ █░  ░█  ████  █    ▒  ▓██▓  █   ██        ██████   █    ██████
                                                      ██████
                <by@keyjeek>  |  Follow the white rabbit...")
                <contact:nomotikag33n@gmail.com>       ")
                [i] This Tool is made for banner grabbing   ")
                """)
                
                def grabber(i, p):
                    sock = socket.socket()
                    sock.connect((i, int(p)))
                    banner = sock.recv(1024)
                    print(banner)
                def main():
                    if len(sys.argv) <= 1:
                        print("[!] Use --help\n")
                    elif sys.argv[1] == "--help":
                        print("[*] Usage: python3 eye_of_sauron.py <IP/Domain> <port> ")
                        exit(0)
                    elif len(sys.argv) == 3:
                        print("[!] success!")
                        k = sys.argv[1]
                        j = sys.argv[2]
                        grabber(k, j)
                        exit(0)                       
                main()
            eye_of_sauron()

        elif choice == '5':
            os.system('clear')
            def base64encode():
                def banner():
                    print("""
                                                                  █
             █████░  ▒███▒    ██                                  █
             █   ▒█ ░█▒  ▓   ▒██                                  █
             █    █ █▒       █░█   ███   █▒██▒   ▓██▒   ███    ██▓█   ███
             █   ▒█ █▒███   ▓▓ █  ▓▓ ▒█  █▓ ▒█  ▓█  ▓  █▓ ▓█  █▓ ▓█  ▓▓ ▒█
             █████░ █▓  ▓█ ░█  █  █   █  █   █  █░     █   █  █   █  █   █
             █   ▒█ █    █ █▒  █  █████  █   █  █      █   █  █   █  █████
             █    █ █    █ ██████ █      █   █  █░     █   █  █   █  █
             █   ▒█ ▒▓  ▓█     █  ▓▓  █  █   █  ▓█  ▓  █▓ ▓█  █▓ ▓█  ▓▓  █
             █████░  ▓███      █   ███▒  █   █   ▓██▒   ███    ██▓█   ███▒
                    <by@keyjeek>  |  Follow the white rabbit...
                        <contact:nomotikag33n@gmail.com>       
                    [i] This Tool helps to encode and decode your text in base64.  
                    [i] Type x to exit Base64encode.
                """)
                banner()
                def menu():
                    print("""
                        [1] Encoder
                        [2] Decoder
                        [x] Exit 
                    """)
                menu()
                def chse():
                    choice = input("[*] Enter choice: ")
                    if choice == '1':
                        print(chr(0xa))
                        hash_value = input("[*] Enter message: ")
                        if hash_value == 'x':
                            print(chr(0xa))
                            exit_choice = input("[?] Do you want to exit? y/n ")
                            if exit_choice == 'y':
                                print("[i] Exit")
                                return HUNT3R()
                            elif exit_choice == 'n':
                                return chse()
                            else:
                                print("[i] Invalid Input")
                                return chse()
                        m_bytes = choice.encode('ascii')
                        b64_e = base64.b64encode(m_bytes)
                        b64_hash = b64_e.decode('ascii')
                        print(b64_hash)
                        return chse()       
                    elif choice == '2':
                        print(chr(0xa))
                        b64_hash_val = input("[*] Enter hash to decode: ")
                        print(chr(0xa))
                        if b64_hash_val == 'x':
                            print("[i] Exit")
                            return HUNT3R()
                        b64_d = b64_hash_val.encode('ascii')
                        m_bytes = base64.b64decode(b64_d)
                        result = m_bytes.decode('ascii')
                        print(result)
                        return chse()
                    elif choice == 'x':
                        print("[i] Exit")
                        return HUNT3R()
                    else:
                        print("[i] Invalid input")
                        return HUNT3R()
                chse()
            base64encode()

        elif choice == '6':
            def wifiStalker():
                networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
                networks.set_index("BSSID", inplace=True)
                def callback(packet):
                    if  packet.haslayer(Dot11Beacon):
                        bssid = packet[Dot11].addr2
                        ssid = packet[Dot11Elt].info.decode()
                        try:
                            dbm_signal = packet.dBm_AntSignal
                        except:
                            dbm_signal = "N/A"
                        stats = packet[Dot11Beacon].network_stats()
                        channel = stats.get("channel")
                        crypto = stats.get("crypto")
                        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)
                def print_all():
                    while True:
                        os.system("clear")
                        print(networks)
                        time.sleep(0.5)                    
                if __name__ == "__main__":
                    interface = "wlan0mon"
                    printer = Thread(target=print_all)
                    printer.daemon = True
                    printer.start()
                    sniff(prn=callback, iface=interface)
                def change_channel():
                    ch = 1
                    while True:
                        os.system(f"iwconfig {interface} channel {ch}")
                        ch = ch%14+1
                        time.sleep(0.5)
                        channel_change = Thread(target=change_channel)
                        channel_changer.daemon = True
                        channel_changer.start()
            wifiStalker()
        
        elif choice == '7':
            os.system('clear')
            def number_tracker():
                print(colored("""
        █     █ █    █ ██████ █████  ██████ █████  █    █
        █░ █ ░█ █    █ █      █   ▓█ █      █   ▓█ █    █
        █░▒█▒░█ █    █ █      █    █ █      █    █ █    █
        ▓▒███▒█ █    █ █      █   ▒█ █      █   ▒█ █    █
        ▒▒█▒█▒▓ ██████ ██████ █████  ██████ █████  █    █
        ▒██ ██▓ █    █ █      █  ░█▒ █      █  ░█▒ █    █
        ▒█▓ ▓█▒ █    █ █      █   ░█ █      █   ░█ █    █
        ░█▒ ▒█▒ █    █ █      █    █ █      █    █ █▒  ▒█
        █   █▒ █    █ ██████ █    ▒ ██████ █    ▒  ████

            <by@keyjeek>  |  Follow the white rabbit...
                <contact:nomotikag33n@gmail.com>    
            [i] Phonenumber tracking tool
                """, "blue"))

                while True:
                    print(chr(0xa))
                    number = input('[*] Phonenumber: ')
                    if number == "x":
                        print(colored("[i] Exit", "red"))
                        return HUNT3R()
                    elif number == "exit":
                        print(colored("[i] Exit", "red"))
                        return HUNT3R()
                    ## check if valid
                    print(chr(0xa))
                    valid_check = phonenumbers.parse(number)
                    is_valid = phonenumbers.is_valid_number(valid_check)
                    print("Valid: ")
                    print(is_valid)
                    ## check timezone
                    timezone_number = phonenumbers.parse(number, "en")
                    print(timezone.time_zones_for_number(timezone_number))
                    ## get location
                    target_number = phonenumbers.parse(number, "CH")
                    print(geocoder.description_for_number(target_number, "en"))
                    ## get provider information
                    provider_info = phonenumbers.parse(number, "RO")
                    print(carrier.name_for_number(provider_info, "en"))
                    print(chr(0xa))
                    input('Press any key..')
                    return number_tracker()
            number_tracker()
        
        else:
            print(colored("[i] Invalid input", "red"))
            return HUNT3R()

    hunter()
    
HUNT3R()
