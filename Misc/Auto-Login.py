
# Sebelum menggunakan sebaiknya melihat video tutorial di bagian Demo[LINK-YOUTUBE-VIDEO]

import sys

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    print("Library Selenium sudah terinstall.")

    target_url = "https://Contoh.servers.L/admin/login.php"     # ganti url
    username = "Leon"                                           # ganti usernamenya
    password = "passwordAnda"                                   # ganti passwordnya
    username_field_selector = "#username"                       # sesuaikan id/class pada kolom username
    password_field_selector = "#password"                       # sesuaikan id/class pada kolom password
    submit_button_selector = "#submitLogin1"                    # sesuaikan id/class pada tombol submit
    driver = webdriver.Chrome()
    driver.get(target_url)
    username_field = driver.find_element(By.CSS_SELECTOR, username_field_selector)
    username_field.send_keys(username)
    password_field = driver.find_element(By.CSS_SELECTOR, password_field_selector)
    password_field.send_keys(password)
    submit_button = driver.find_element(By.CSS_SELECTOR, submit_button_selector)
    submit_button.click()
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
        # install Selenium
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


