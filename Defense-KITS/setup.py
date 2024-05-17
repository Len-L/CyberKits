
import subprocess as qq
import os
import re
import sys 

banner = f"""
    \033[32m  

        ╭━━━╮╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━┳━━┳━━━━┳━━━╮
        ╰╮╭╮┃╱╱╱┃╭╯╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭┻┫┣┫╭╮╭╮┃╭━╮┃
        ╱┃┃┃┣━━┳╯╰┳━━┳━╮╭━━┳━━╮┃╰╯╯╱┃┃╰╯┃┃╰┫╰━━╮
        ╱┃┃┃┃┃━╋╮╭┫┃━┫╭╮┫━━┫┃━┫┃╭╮┃╱┃┃╱╱┃┃╱╰━━╮┃
        ╭╯╰╯┃┃━┫┃┃┃┃━┫┃┃┣━━┃┃━┫┃┃┃╰┳┫┣╮╱┃┃╱┃╰━╯┃
        ╰━━━┻━━╯╰╯╰━━┻╯╰┻━━┻━━╯╰╯╰━┻━━╯╱╰╯╱╰━━━╯ 

"""



while True:
    print(banner)
    print("\033[32m")
    print("1. Setup Defense-KITS ")
    print("2. Penguatan Server Apache2")
    print("3. Anti DDOS")
    print("4. [RUN] Honeypot")
    print("99. Exit")
    print(" ")
    
    opsi = input("\33[94m[Defense-KITS/Setup]_Options-> ")
    print("\033[32m")

    if opsi=="1":
        print(" ")
        print("1. install Kebutuhan Defense-Kits [Wajib] ")
        print("2. Perkuat Server Dengan Tools Rekomendasi Kami")
        print(" ")
        opsi = input("\33[94m[Defense-KITS/Setup]_Options-> ")
        print("\033[32m")
        if opsi=="1":
            try:
                qq.run(["sudo", "apt", "install", "nmap", "-y"], check=True)
            except:
                print(" ")
                print("===Terjadi Error Saat Menginstal Nmap")
                exit()


        elif opsi=="2":
            print("1. Fail2Ban  (root)")
            print("2. Clamav  (root)")
            print("3. Honeypot  (normal user)")

            kuat = input("\33[94m[Defense-KITS/Setup]_Options-> ")
            print("\033[32m")

            if kuat=="1":
                print("fail2ban: untuk memblokir alamat IP yang menunjukkan aktivitas mencurigakan, seperti upaya login yang gagal berulang kali.")
                f2b = input("\33[94mapakah anda minat menginstallnya?(y/n)-> ")
                print("\033[32m")
                # snort, cari honey
                if f2b=="y":
                    try:
                        qq.run(["sudo", "apt", "install", "fail2ban", "-y"], check=True)
                        qq.run(["sudo", "service", "fail2ban", "start"])
                        print(" ")
                        print("Setup Fail2ban Selesai, Happy Enjoy :) ")
                    except:
                        print(" ")
                        print("===Terjadi Error Saat Menginstall Fail2Ban")
                        exit()

            elif kuat=="2":
                print("Clamav: suatu alat untuk membantu mendeteksi virus")
                clamav = input("\33[94mapakah anda minat menginstallnya?(y/n)-> ")
                print("\033[32m")
                if clamav=="y":
                    try:
                        qq.run(["sudo", "apt", "install", "clamav", "-y"], check=True)
                        print(" ")
                        print("Setup Clamav Selesai, Happy Enjoy :) ")
                    except:
                        print(" ")
                        print("===Terjadi Error Saat Menginstall Clamav")
                        exit()
            
            elif kuat=="3":
                print("Honeypot")
                honeypot = input("\33[94mapakah anda minat menginstallnya?(y/n)-> ")
                print("\033[32m")
                if honeypot=="y":
                    try:
                        qq.run(["pip3", "install", "honeypots"], check=True)


 
    elif opsi=="2":
        print(" ")
        ## Mengubah konfigurasi Apache.
        qq.run(["sudo", "a2enmod", "headers"], stdout=qq.PIPE)
        qq.run(["sudo", "a2enmod", "ssl"], stdout=qq.PIPE)
        qq.run(["sudo", "a2enmod", "rewrite"], stdout=qq.PIPE)

        ## Mengatur konfigurasi keamanan Apache.
        with open("/etc/apache2/apache2.conf", "a") as f:
            ## 2 line di bawah ini untuk menghapus spanduk versi server dan OS [mempersulit penyerang dalam proses pengintaian]
            f.write("ServerSignature Off\n") ##menghapus informasi versi
            f.write("ServerTokens Prod\n") ##mengubah Header menjadi produksi saja
            f.write("TraceEnable Off\n") ##Nonaktifkan Permintaan HTTP Jejak
            f.write("FileETag None\n")
            f.write("Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure\n") ##Setel cookie dengan HttpOnly dan bendera Aman
            f.write("Header always append X-Frame-Options SAMEORIGIN\n") ##Mencegah Clickjacking attacks
            f.write("Header set X-XSS-Protection '1; mode=block'\n") ##Perlindungan Terhadap XSS
            f.write("<Directory /var/www/html>\n")
            f.write("  Options -Indexes\n") ##Nonaktifkan daftar direktori (pengunjung tidak melihat semua file dan folder yang Anda miliki)
            f.write("  AllowOverride All\n")
            f.write("  Require all granted\n")
            f.write("</Directory>\n")

        # restart Apache.
        qq.run(["sudo", "systemctl", "restart", "apache2"], stdout=qq.PIPE)
        print(" ")
        print("Hardening Server Apache Telah Berhasil Dengan Baik ")
    
    elif opsi=="3":
        os.system("iptables -t mangle -A PREROUTING -m conntrack --ctstate INVALID -j DROP") #block invalid packet
        os.system("iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP") #Block New Packet Yang Not SYN
        os.system("iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP") #Block Nilai MSS Yang Tidak Normal
        #Block Packet Dengan Bogus TCP Flag
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP")
        os.system("iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP")
    
    elif opsi=="4":
        service_yang_ada = {  # sevice yang ada aja (kumpulannyaaaaaa.........)
        "ftp",
        "ssh",
        "http",
        "mysql",
        }

        def add_service(service_name):
            global command_string
            if service_name in service_yang_ada:  
                command_string += f"{service_name},"  
                print(f"Layanan '{service_name}' ditambahkan.")
            else:
                print(f"Layanan '{service_name}' tidak tersedia.")

        def get_user_input(service_name):
            while True:
                user_input = input(f"\33[94mApakah Anda ingin menambahkan '{service_name}'? (ya/tidak): \033[32m").lower()
                if user_input in ("ya", "tidak"):
                    return user_input == "ya"
                else:
                    print("Masukan tidak valid. Silahkan masukkan 'ya' atau 'tidak'.")

        command_string = "sudo -E python3 -m honeypots --setup "

        for service_name in service_yang_ada:  
            if get_user_input(service_name):
                add_service(service_name)


        def merge_strings(command_string, config_file):
            merged_string = f"{command_string} --config {config_file}"
            return merged_string

        config_file = "config.json"
        merged_command = merge_strings(command_string, config_file)
        #print(f"Perintah lengkap: {merged_command}")
        qq.run(merged_command, shell=True)

        


            

    elif opsi=="99":
        print(" ")
        print("Semoga Bermanfaat :)")
        break

    else:
        print(" ")
        print("Tolong Masukan Opsi Sesuai Angka Yang Ada")



