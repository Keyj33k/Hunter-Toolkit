from termcolor import colored

def main(banner): 

    print(colored("""
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

    [1] WITCHER
    [2] MD5CRYPT
    [3] IPEYE
    [4] BANNER_GRABBER
    [5] B64CRYPT
    [6] WHEREAREYOU
    [98] CLEAR
    [99] EXIT
    """, "yellow"))

main(banner=True)