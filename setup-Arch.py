import os 

banner = f"""
    \033[32m
        ╭━━━╮╱╱╱╭╮╱╱╱╱╱╱╭╮╭━┳━━┳━━━━┳━━━╮
        ┃╭━╮┃╱╱╱┃┃╱╱╱╱╱╱┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ┃┃╱╰╋╮╱╭┫╰━┳━━┳━┫╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ┃┃╱╭┫┃╱┃┃╭╮┃┃━┫╭┫╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ┃╰━╯┃╰━╯┃╰╯┃┃━┫┃┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰━━━┻━╮╭┻━━┻━━┻╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯
        ╱╱╱╱╭━╯┃
        ╱╱╱╱╰━━╯
"""

print(banner)
print("\033[32m")
print("Install Nmap")
os.system("pacman -S --noconfirm nmap")
print("Install Figlet")
os.system("pacman -S --noconfirm figlet")
print("Install JQ")
os.system("pacman -S --noconfirm jq")
print("Install SMBClient")
os.system("pacman -S --noconfirm smbclient")
print("Install Mat2")
os.system("pacman -S --noconfirm mat2")
print("Install requirements.txt")
os.system("pip install -r Pentest-KITS/requirements.txt")
print("Install fail2ban")
os.system("pacman -S --noconfirm fail2ban")
print("Install clamav")
os.system("pacman -S --noconfirm clamav")
print("Install Honeypots")
os.system("pip3 install honeypots")
print("Install Apache2")
os.system("pacman -S --noconfirm apache")
print("Setting Anti DDOS")
os.system("iptables -t mangle -A PREROUTING -m conntrack --ctstate INVALID -j DROP") #block invalid packet
os.system("iptables -t mangle -A PREROUTING -p tcp ! --s --noconfirmyn -m conntrack --ctstate NEW -j DROP") #Block New Packet Yang Not SYN
os.system("iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP") #Block Nilai MSS Yang Tidak Normal
#Block Packet Dengan Bogus TCP Flag
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP")
os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP")
