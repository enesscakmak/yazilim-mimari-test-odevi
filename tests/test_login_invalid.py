from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Tarayıcı başlat
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Kullanıcı adı ve şifreyi yanlış gir
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("wrongUser")
password_input.send_keys("wrongPass")
password_input.send_keys(Keys.RETURN)

time.sleep(2)  # Sayfanın yüklenmesi için kısa bekleme

# Hata mesajını kontrol et
error_message = driver.find_element(By.ID, "flash").text
assert "Your username is invalid!" in error_message

print("Login testi: Hata mesajı başarıyla görüntülendi.")

# Tarayıcıyı kapat
driver.quit()
