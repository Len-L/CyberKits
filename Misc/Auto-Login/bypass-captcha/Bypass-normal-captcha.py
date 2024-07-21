# Sebelum menggunakan sebaiknya melihat video tutorial di bagian Demo [LINK-YOUTUBE-VIDEO]
# pip install 2captcha-python
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import time
import os

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
browser = webdriver.Chrome()
browser.get('https://2captcha.com/demo/normal')                                 # url yang ada captchanya

captcha_img = browser.find_element(By.CLASS_NAME, '_captchaImage_rrn3u_9')      # class dari gambar captcha nya
captcha_img.screenshot('captchas/captcha.jpg')                                  

api_key = os.getenv('APIKEY_2CAPTCHA', 'API_Key-Anda')                          # API Key Anda

solver = TwoCaptcha(api_key)

try:
    result = solver.normal('captchas/captcha.jpg')                               

except Exception as e:
    print(e)

else:
    code = result['code']
    print(code)

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'simple-captcha-field'))) # ID tempat masukin kata kata dari captcha
    browser.find_element(By.ID, 'simple-captcha-field').send_keys(code)               # ID tempat masukin kata kata dari captcha

    browser.find_element(By.CLASS_NAME, "_actionsItem_1f3oo_41").click()     # class tombol check

time.sleep(120)



