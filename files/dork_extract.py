from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from colorama import  *

SLEEP_TIME = 2
init(autoreset=True)



def ext_dork(target="", filetype="", intext="", intitle="", inurl=""):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://dorkgenerator.com/")
        sleep(SLEEP_TIME)

        if target:
            find_target = driver.find_element(By.ID, "siteInput")
            find_target.send_keys(target)

        if filetype:
            find_filetype = driver.find_element(By.ID, "fileTypeInput")
            find_filetype.send_keys(filetype)

        if intext:
            find_intext = driver.find_element(By.ID, "intextInput")
            find_intext.send_keys(intext)

        if intitle:
            find_intitle = driver.find_element(By.ID, "intitleInput")
            find_intitle.send_keys(intitle)

        if inurl:
            find_inurl = driver.find_element(By.ID, "inurlInput")
            find_inurl.send_keys(inurl)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SLEEP_TIME)

        find_button = driver.find_element(By.XPATH, "//button[normalize-space()='Generate Dork']")
        find_button.click()
        sleep(SLEEP_TIME)

        # Sonucu al
        find_resultBar = driver.find_element(By.ID, "generatedDork")
        result = find_resultBar.text

        print(f"{Fore.GREEN} \nOluşturulan Dork:  {Style.RESET_ALL} {Fore.RED} {result} {Style.RESET_ALL}")
        return result

    except Exception as e:
        print(f"{Fore.RED}Hata oluştu :{Style.RESET_ALL} {e}")
        return None

    finally:
        driver.quit()


