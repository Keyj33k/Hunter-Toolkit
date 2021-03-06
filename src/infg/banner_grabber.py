#!/usr/bin/env python3

try:
    from datetime import datetime as dtt
    import time
    import socket
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.


    """)
    
# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.1.9                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

w = "\033[0;37m"
g = "\033[0;32m"
r = "\033[0;31m"


class BannerGrabber:

    def __init__(
            self,
            target_address: str,
            target_port: int
    ):
        self.target_address = target_address
        self.target_port = target_port

    def main(self):
        while True:
            if self.target_address == 'x' or self.target_address == 'exit':
                break
            elif self.target_port == 0:
                break

            try:
                with socket.socket(
                        socket.AF_INET,
                        socket.SOCK_STREAM
                ) as socket_sock:
                    socket_sock.connect_ex((
                        self.target_address,
                        self.target_port
                    ))
                    socket_sock.settimeout(5)
                    service = socket_sock.recv(1024).decode()

                print(f"\n{w}[{r}*{w}] Start scanning {self.target_address} at {dtt.now()}")
                time.sleep(1.5)
                print(f"{r}=" * 65)
                print(f"{w}[{g}+{w}] Port {self.target_port} {r}->{w} {service}")
                print(f"{r}=" * 65)
                print(chr(0xa))
                input(f"{w}[{r}*{w}] Press enter key to continue")
                break
            except socket.error as sockerr:
                print(sockerr)
                break

