# CyberKits
Perlengkapan Cyber Dalam Melakukan Pentest Dan Pertahanan Server Dari Aktivitas Penyerangan Peretas<br>
<br>
## Installation Pentest-KITS 
Instal keperluan Pentest-KITS di debian linux
```bash
  #> apt install nmap 
  #> apt install figlet
  #> apt install jq
  #> apt install mat2 #Linux Only
  #> git clone https://github.com/Len-L/CyberKits.git
  #> cd CyberKits/Pentest-KITS 
  #> pip install -r requirements.txt
```    
## Installation Defense-KITS
Instal keperluan Defense-KITS di Server Ubuntu
```javascript
  #> cd CyberKits/Defense-KITS
  #> python3 setup.py
  
  #Output sebagai berikut======

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
- Vulnerability Scanner + Auto Exploit Vulnerability 
- Exploit SSRF Otomatis [Support SSL]
- Bypass 403 (Bypass Forbidden Page)
- Pencari Parameter (Mining URLS) 
- Temporary Email (anonim-kit) 
- MetaData Cleaner (anonim-kit) [Linux Only]

## Defense-KITS Features 
- Honeypot 
- Vulnerability Scanner Di Server
- Anti Virus
- Hardening Server Apache2
- Auto Ban IP (jika Percobaan terus menerus gagal)
- Anti DDOS

## Penggunaan Pentest-KITS
```javascript
#> cd CyberKits/Pentest-KITS
#> python3 main.py

#Output akan seperti ini======

        ╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╭╮╭━┳━━┳━━━━┳━━━╮
        ┃╭━╮┃╱╱╱╱╭╯╰╮╱╱╱╱╭╯╰╮┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ┃╰━╯┣━━┳━╋╮╭╋━━┳━┻╮╭╯┃╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ┃╭━━┫┃━┫╭╮┫┃┃┃━┫━━┫┃╱┃╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ┃┃╱╱┃┃━┫┃┃┃╰┫┃━╋━━┃╰╮┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰╯╱╱╰━━┻╯╰┻━┻━━┻━━┻━╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯
1. Scanning
2. SSRF
3. Bypass 403
4. Pencari Parameter
5. Temporary Email [anonim-kit]
6. MetaData Cleaner [anonim-kit]
99. Exit
[Pentest-KITS]_Options->
```

## Penggunaan Defense-KITS
```javascript
#> cd CyberKits/Defense-KITS
#> python3 admin_control.py

#Output akan seperti ini======

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
99. Exit
 
[Defense-KITS/Admin-Control]_Options-> 

```



