
import subprocess as qq
import os
import datetime



while True:
    print(" ")
    print("1. Setup Defense-KITS ")
    print("2. Penguatan Server Apache2")
    print("99. Exit")
    print(" ")
    
    opsi = input("[Defense-KITS/Setup]_Options-> ")

    if opsi=="1":
        print(" ")
        print("1. install Kebutuhan Defense-Kits [Wajib] ")
        print("2. Perkuat Server Dengan Tools Rekomendasi Kami")
        print(" ")
        opsi = input("[Defense-KITS/Setup]_Options-> ")
        if opsi=="1":
            try:
                qq.run(["sudo", "apt", "install", "nmap", "-y"], check=True)
            except subprocess.CalledProcessError:
                print(" ")
                print("===Terjadi Error Saat Menginstal Nmap")
                exit()
            try:
                qq.run(["sudo", "apt", "install", "clamav", "-y"], check=True)
            except subprocess.CalledProcessError:
                print(" ")
                print("===Terjadi Error Saat Menginstal Clamav")
                exit() 


        elif opsi=="2":
            print("fail2ban: untuk memblokir alamat IP yang menunjukkan aktivitas mencurigakan, seperti upaya login yang gagal berulang kali.")
            f2b = input("apakah anda minat menginstallnya?(y/n)-> ")
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

            

    elif opsi=="99":
        print(" ")
        print("Semoga Bermanfaat :)")
        break

    else:
        print(" ")
        print("Tolong Masukan Opsi Sesuai Angka Yang Ada")





