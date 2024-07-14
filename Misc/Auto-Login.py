
# Sebelum menggunakan sebaiknya melihat video tutorial di bagian Demo [LINK-YOUTUBE-VIDEO]

import sys

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
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    print("Library Selenium sudah terinstall.")
    target_url = "https://Contoh.Servers.L/Admin/Login.php"          # ganti url login
    username = "CyberKITS"                                           # ganti usernamenya
    password = "passwordAnda"                                        # ganti passwordnya
    username_field_selector = "#email"                               # sesuaikan id/class pada kolom username
    password_field_selector = "#password"                            # sesuaikan id/class pada kolom password
    driver = webdriver.Chrome()
    driver.get(target_url)
    username_field = driver.find_element(By.CSS_SELECTOR, username_field_selector)
    username_field.send_keys(username)
    password_field = driver.find_element(By.CSS_SELECTOR, password_field_selector)
    password_field.send_keys(password)
    btnLogin = driver.find_element(By.XPATH, "//button[text()='Log in']")   # ganti kata 'Log in' dengan text di button/tombol login
    btnLogin.submit()
    driver.implicitly_wait(10)
    print("selesai")
    input("Tekan Enter untuk tutup browser.....")  
    driver.quit() 

except ImportError:
  print("Library Selenium belum terinstall.")

  while True:
    jawaban = input("Apakah Anda ingin menginstall library Selenium sekarang? (ya/tidak): ")
    if jawaban.lower() == "ya":
      try:
        # install Selenium Dengan PIP
        sys.exec_command(["pip", "install", "selenium"])
        print("Library Selenium berhasil diinstall :)")
        break
      except Exception as e:
        print(f"Gagal menginstall Selenium: {e}")
    elif jawaban.lower() == "tidak":
      print("Anda memilih untuk tidak menginstall Selenium.")
      break
    else:
      print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

