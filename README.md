# CyberKits
Perlengkapan Cyber Dalam Melakukan Pentest Dan Pertahanan Server Dari Aktivitas Penyerangan Peretas<br>
Masih Tahab Pengembangan :)
<br>
## Installation Pentest-KITS
Instal keperluan Pentest-KITS di debian linux
```bash
  apt install nmap 
  apt install figlet
  apt install jq
  git clone https://github.com/Len-L/CyberKits.git
  cd CyberKits/Pentest-KITS 
  pip install -r requirements.txt
```    
## Installation Defense-KITS
Instal keperluan Defense-KITS di Server Ubuntu
```bash
  cd CyberKits/Defense-KITS
  python3 main.py
  
  #Output sebagai berikut======
  
  1. Setup Defense-KITS 
  2. Scanner Vulnerability Server
  3. Anti Virus (Clamav) 
  99. Exit
  [Defense-KITS]_Options-> 1
 
  1. install Kebutuhan Tools
  2. Perkuat Server Dengan Tools Rekomendasi Kami
  [Defense-KITS/Setup]_Options-> 1
```    

## Features Pentest-KITS
- Vulnerability Scanner 
- Exploit SSRF Otomatis
- Bypass 403 (Bypass Forbidden Page)
- Pencari Parameter

## Features Defense-KITS
- Vulnerability Scanner Di Server
- Anti Virus

## Penggunaan/Contoh Pentest-KITS
```javascript
cd CyberKits/Pentest-KITS
python3 main.py

#Output akan seperti ini======

1. Scanning
2. SSRF
3. Bypass 403
4. Pencari Parameter
99. Exit
[Pentest-KITS]_Options->
```

## Penggunaan/Contoh Defense-KITS
```javascript
cd CyberKits/Defense-KITS
python3 main.py

#Output akan seperti ini======

1. Setup Defense-KITS 
2. Scanner Vulnerability Server
3. Anti Virus (Clamav) 
99. Exit
 
[Defense-KITS]_Options-> 

```



