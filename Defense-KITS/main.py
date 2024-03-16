
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


        if opsi=="2":
            print("fail2ban: untuk memblokir alamat IP yang menunjukkan aktivitas mencurigakan, seperti upaya login yang gagal berulang kali.")
            f2b = input("apakah anda minat menginstallnya?(y/n)-> ")
            # snort, cari honey
            if f2b=="y":
                try:
                    qq.run(["sudo", "apt", "install", "fail2ban"], check=True)
                except:
                    print(" ")
                    print("===Terjadi Error Saat Menginstall Fail2Ban")
                    exit()

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
        print(" ")
        print("1. Update Database AntiVirus")
        print("2. Scan Top 3 Folder")
        clamav = input("[Defense-KITS/AntiVirus]_Options->")
        if clamav=="1":
            try:
                qq.run(["sudo", "freshclam"], check=True)
                print(" ")
            except:
                qq.run(["sudo", "systemctl", "stop", "clamav-freshclam.service"])
                qq.run(["sudo", "freshclam"])
                print(" ")
        
        if clamav=="2":
            print("Sedang Scanning Virus............")
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Home-dir_AntiVirus.log", "/home"])
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Var-dir_AntiVirus.log", "/var"])
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Etc-dir_AntiVirus.log", "/etc"])
            print(" ")
            print("jangan Khawatir, semua hasil analisa Antivirus sudah di Save -> /log-antivirus")
            

    if opsi=="99":
        print(" ")
        print("Semoga Bermanfaat :)")
        break
