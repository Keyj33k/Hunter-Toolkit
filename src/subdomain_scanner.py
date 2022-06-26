#!/usr/bin/env python3

try:
    import requests
    import time
    import os
except ImportError:
    raise RuntimeError("""
    Oops,

    this tool uses important modules, which don't seem to be 
    installed at the moment.

    Use the requirements file and this command:
    "pip3 install -r requirements.txt" 

    You will find this file in the req directory.


    """)

class SubdomainScanner:

    def __init__(
            self,
            uniformresourcelocator: str
    ):
        self.uniformresourcelocator = uniformresourcelocator

    def main(self):
        while True:
            found_subdomain = []
            if self.uniformresourcelocator == 'exit' or self.uniformresourcelocator == 'x':
                break

            try:
                with open("subdomains.txt", "r") as FILE:
                    read_file = FILE.read()
                    subdomain = read_file.splitlines()
                    for list_domains in subdomain:
                        uniformresourcelocator = f"http://{list_domains}.{self.uniformresourcelocator}"
                        time.sleep(1)

                        try:
                            requests.get(uniformresourcelocator)
                        except requests.ConnectionError:
                            pass
                        else:
                            print(
                                "Discovered:",
                                uniformresourcelocator
                            )
                            found_subdomain.append(
                                uniformresourcelocator
                            )

                input("Press enter key to continue")
                break
            except FileNotFoundError:
                print("You need the subdomain file in the current directory to run this tool.")
                break
            except KeyboardInterrupt:
                print("You need the subdomain file in the current directory to run this tool.")
                break


