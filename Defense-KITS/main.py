
import subprocess as qq
import os
import datetime



while True:
    print(" ")
    print("1. Setup Defense-KITS ")
    print("2. Scanner Vulnerability Server")
    print("3. Anti Virus (Clamav) ")
    print("99. Exit")
    print(" ")
    
    opsi = input("[Defense-KITS]_Options-> ")

    if opsi=="1":
        print(" ")
        print("1. install Kebutuhan Tools")
        print("2. Perkuat Server Dengan Tools Rekomendasi Kami")
        print(" ")
        opsi = input("[Defense-KITS/Setup]_Options-> ")
        if opsi=="1":
            try:
                subprocess.run(["sudo", "apt", "install", "nmap", "-y"], check=True)
            except subprocess.CalledProcessError:
                print(" ")
                print("===Terjadi Error Saat Menginstal Nmap")
                exit()
            try:
                subprocess.run(["sudo", "gem", "install", "wpscan"], check=True)
            except subprocess.CalledProcessError:
                print(" ")
                print("===Terjadi Error Saat Menginstall WPScan")
                exit()
            try:
                subprocess.run(["sudo", "apt", "install", "clamav", "-y"], check=True)
            except subprocess.CalledProcessError:
                print("===Terjadi Error Saat Menginstal Clamav")
                exit() 


        if opsi=="2":
            print("fail2ban:")
            print("snort:")
            print("Cari honey")

    if opsi=="2":
        print(" ")
        def scan_server(report_file):
            scan_results = qq.run(["nmap", "-sC", "-sV", "--script", "vuln", "localhost"], capture_output=True).stdout.decode()
            with open(report_file, "w") as f:
                f.write(f"===Laporan Pemindaian Kerentanan Server===\n")
                f.write(f"Tanggal: {datetime.datetime.now().strftime('%d-%m-%Y')}\n")
                f.write(f"Host: {os.uname().nodename}\n\n")
                f.write("## HASIL NMAP\n")
                f.write(scan_results)
        if __name__ == "__main__":
            report_file = "laporan_kerentanan.txt"
            scan_server(report_file)
        print("Hasil sudah di save -> laporan_kerentanan.txt")

    if opsi=="3":
        qq.run(['clamav'])





    if opsi=="99":
        print(" ")
        print("Semoga Bermanfaat :)")
        break




