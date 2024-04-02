import subprocess as qq
import os
import datetime



while True:
    print(" ")
    print("1. Start Semua Service")
    print("2. Scanner Vulnerability Server")
    print("3. Anti Virus (Clamav)")
    print("4. [Fail2Ban] Cek Log")
    print("5. [Fail2ban] Unban IP")
    print("99. Exit")
    print(" ")
    
    opsi = input("[Defense-KITS/Admin-Control]_Options-> ")
    print(" ")

    if opsi=="1":
        try:
            qq.run(["sudo", "service", "fail2ban", "start"], check=True)
        except:
            print("Fail2ban Tidak Di Temukan")

    elif opsi=="2":
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

    elif opsi=="3":
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
        

        elif clamav=="2":
            print("Sedang Scanning Virus............")
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Home-dir_AntiVirus.log", "/home"])
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Var-dir_AntiVirus.log", "/var"])
            qq.run(["sudo", "clamscan", "-r", "-v", "--infected", "-l", "log-antivirus/Etc-dir_AntiVirus.log", "/etc"])
            print(" ")
            print("jangan Khawatir, semua hasil analisa Antivirus sudah di Save -> /log-antivirus")
    
    elif opsi=="4":
        print(" ")
        print("Fail2ban Log=========================================")
        qq.run(["tail", "/var/log/fail2ban.log"])
        print("Fail2ban Log=========================================")
        print(" ")
    
    elif opsi=="5":
        print("")
        print("contoh: sshd")
        service = input("Masukan Service-> ")
        ipnakal = input("Masukan IP Yang Mau Di Unban-> ")
        qq.run(["sudo", "fail2ban-client", "set", service, "unbanip", ipnakal])
        print(" ")

    elif opsi=="99":
        print(" ")
        print("Semoga Bermanfaat :)")
        break

    else:
        print(" ")
        print("Tolong Masukan Opsi Sesuai Angka Yang Ada")




