# CyberKits
Cyber ​​​​Tools for Conducting Penetration Testing and Server Defense from Hacker Attack Activities<br>

```javascript

      ╭━━━╮╱╱╱╭╮╱╱╱╱╱╱╭╮╭━┳━━┳━━━━┳━━━╮
      ┃╭━╮┃╱╱╱┃┃╱╱╱╱╱╱┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
      ┃┃╱╰╋╮╱╭┫╰━┳━━┳━┫╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
      ┃┃╱╭┫┃╱┃┃╭╮┃┃━┫╭┫╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
      ┃╰━╯┃╰━╯┃╰╯┃┃━┫┃┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
      ╰━━━┻━╮╭┻━━┻━━┻╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯
      ╱╱╱╱╭━╯┃
      ╱╱╱╱╰━━╯
```

<br>

## Installation Pentest-KITS 
Install Pentest-KITS requirements on debian linux
```bash
  #> apt install nmap 
  #> apt install figlet
  #> apt install jq
  #> apt install smbclient
  #> apt install mat2 #Linux Only
  #> git clone https://github.com/Len-L/CyberKits.git
  #> cd CyberKits/Pentest-KITS 
  #> pip install -r requirements.txt
```
Venv PentestKITS: https://tinyurl.com/pentestKITS-venv
## Installation Defense-KITS
Install Defense-KITS requirements on Ubuntu Server
```javascript
  #> cd CyberKits/Defense-KITS
  #> python3 setup.py
  
  #Output======

        ╭━━━╮╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━┳━━┳━━━━┳━━━╮
        ╰╮╭╮┃╱╱╱┃╭╯╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ╱┃┃┃┣━━┳╯╰┳━━┳━╮╭━━┳━━╮┃╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ╱┃┃┃┃┃━╋╮╭┫┃━┫╭╮┫━━┫┃━┫┃╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ╭╯╰╯┃┃━┫┃┃┃┃━┫┃┃┣━━┃┃━┫┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰━━━┻━━╯╰╯╰━━┻╯╰┻━━┻━━╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯

1. Setup Defense-KITS 
2. Penguatan Server Apache2
3. Anti DDOS
4. [RUN] Honeypot
99. Exit
 
[Defense-KITS/Setup]_Options-> 1
```    

## Pentest-KITS Features 
- Vulnerability Scanner (Auto Exploit Vulnerability, SMB Enumeration)
- automatic Exploit SSRF [Support SSL]
- Bypass 403 (Bypass Forbidden Page)
- Parameter Finder (Mining URLS) 
- Temporary Email (anonim-kit) 
- MetaData Cleaner (anonim-kit) [Linux Only]
- Subdomain Scanner
- Online Exploit Finder

## Defense-KITS Features 
- Honeypot 
- Vulnerability Scanner Di Server
- WAF Level Aplikasi (ModSecurity)
- Anti Virus
- Hardening Server Apache2
- Auto Ban IP (if the experiment fails)
- Anti DDOS

## Misc
- Auto Login <br>
      - Bypass normal captcha

## Usage Pentest-KITS
```javascript
#> cd CyberKits/Pentest-KITS
#> python3 main.py

#Output======

        ╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╭╮╭━┳━━┳━━━━┳━━━╮
        ┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╱╭╯╰╮┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ┃╰━╯┣━━┳━╋╮╭╋━━┳━┻╮╭╯┃╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ┃╭━━┫┃━┫╭╮┫┃┃┃━┫━━┫┃╱┃╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ┃┃╱╱┃┃━┫┃┃┃╰┫┃━╋━━┃╰╮┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰╯╱╱╰━━┻╯╰┻━┻━━┻━━┻━╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯
1. Scanning
2. Exploit SSRF
3. Bypass 403
4. Parameter Finder [Mining URLS]
5. Temporary Email [anonim-kit]
6. MetaData Cleaner [anonim-kit] 
7. Subdomain Scanner
8. Online Exploit Finder
9. Files Sharing
99. Exit
[Pentest-KITS]_Options->
```

## Penggunaan Defense-KITS
```javascript
#> cd CyberKits/Defense-KITS
#> python3 admin_control.py

#Output======

        ╭━━━╮╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━┳━━┳━━━━┳━━━╮
        ╰╮╭╮┃╱╱╱┃╭╯╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ╱┃┃┃┣━━┳╯╰┳━━┳━╮╭━━┳━━╮┃╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ╱┃┃┃┃┃━╋╮╭┫┃━┫╭╮┫━━┫┃━┫┃╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ╭╯╰╯┃┃━┫┃┃┃┃━┫┃┃┣━━┃┃━┫┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰━━━┻━━╯╰╯╰━━┻╯╰┻━━┻━━╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯

1. Start Semua Service
2. Scanner Vulnerability Server
3. Anti Virus (Clamav)
4. [Fail2Ban] Cek Log
5. [Fail2ban] Unban IP
6. [ModSec] Cek Log
99. Exit
 
[Defense-KITS/Admin-Control]_Options-> 

```

## Demo

All CyberKITS Demo Videos:<br>
https://www.youtube.com/watch?v=iIwvKSeBbGg&list=PLYk3ddW0_4QOXWIYlb8dn1a4JqK6o3Xoj&pp=iAQB


