import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
# from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from cryptography.fernet import Fernet

# Develop By Yoel Mountanus Sitorus
# 5025211078 Informatics ITS 2021

LINK = "https://akademik.its.ac.id/"

def encrypt_credential(username, password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    msg = fernet.encrypt(f"{username}:{password}".encode())
    return key.decode("utf-8"), msg.decode("utf-8")

def save_credentials(username, password):
    key, msg = encrypt_credential(username, password)
    with open('cred.dll', 'w') as file:
        file.write(f"{key}\n{msg}")

def load_credentials():
    if not os.path.exists('cred.dll'):
        return None

    with open('cred.dll', 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            key = lines[0].strip()
            msg = lines[1].strip()
            fernet = Fernet(key.encode())
            data = fernet.decrypt(msg.encode()).decode("utf-8")
            data = data.split(":")
            return data[0], data[1]

    return None

def prompt_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    save_credentials(username, password)
    return username, password

def login(bot, username, password):
    bot.get(LINK)
    time.sleep(1)

    print("[Info] - Logging in...")
    username_input = WebDriverWait(bot, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='username']")))
    username_input.clear()
    username_input.send_keys(username)

    login_button = WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']")))
    login_button.click()

    password_input = WebDriverWait(bot, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
    password_input.clear()
    password_input.send_keys(password)

    login_button = WebDriverWait(bot, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    time.sleep(TIMEOUT)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def openWindows(bot, link, tabId):
    tabs.append(tabId)
    bot.execute_script(f"window.open('{link}', '{tabId}');")

def openWindowsExecute(bot, link, tabId, javascript):
    openWindows(bot, link, tabId)
    bot.switch_to.window(tabId)
    try:
        bot.execute_script(javascript)
    except WebDriverException as e:
        print(f"Error: {e}")

def openDosenIPD(bot, dosenCount, script):
    try:
        links = bot.execute_script(f"""
            let dosen = document.querySelectorAll('table.FilterBox');
            return Array.from(dosen[dosen.length-1].firstChild.childNodes).map(e => e.lastChild.firstChild.firstChild.href);
        """)
    except Exception as e:
        print("Sudah terisi!")
        return

    print(links)

    for link in links:
        openWindowsExecute(bot, link, f"dosen-{dosenCount}-{link[len(link)-1]}", script)
        time.sleep(5)
        bot.execute_script(f"document.querySelector('input[type=\"submit\"]').click()")
        time.sleep(2)
        bot.close()
        bot.switch_to.window(bot.window_handles[len(bot.window_handles)-1])

def openAllMataKuliahKuisioner(bot, script):
    try:
        mkCount = bot.execute_script("""
            let mk = document.querySelector('select#mk_kuesioner');
            return mk.childElementCount;
        """)
    except WebDriverException as e:
        mkCount = 0
        print(f"Error: {e}")

    dosenCount = 0

    for i in range(mkCount-1):
        dosenCount += 1
        openWindowsExecute(
            bot, 'https://akademik.its.ac.id/ipd_kuesionermk.php', 
            f"mk-{i+1}", f"document.querySelector('select#mk_kuesioner').selectedIndex = {i+1}; MKChange()"
            )

        try:
            WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
            try:
                bot.execute_script(script)
                time.sleep(5)
                bot.execute_script(f"document.querySelector('input[type=\"submit\"]').click()")
                time.sleep(2)
                openDosenIPD(bot, dosenCount, script)
            except Exception as e:
                print("[ERROR]")
        except Exception as e:
            openDosenIPD(bot, dosenCount, script)

        # bot.close()

    

def doIpd(bot):
    bot.get('https://akademik.its.ac.id/ipd_kuesionermk.php')
    WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    script = read_file("script.js")

    openAllMataKuliahKuisioner(bot, script)
    # openWindowsExecute(bot, "https://akademik.its.ac.id/ipd_kuesionermk.php", "1", script)
    # print(script)

def scrape():
    credentials = load_credentials()

    if credentials is None:
        username, password = prompt_credentials()
    else:
        username, password = credentials

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.TIMEOUT25.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)


    bot=webdriver.Chrome()

    login(bot, username, password)
    time.sleep(3)
    doIpd(bot)

    time.sleep(60)

    bot.quit()

if __name__ == '__main__':
    TIMEOUT = 15
    scrape()