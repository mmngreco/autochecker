import os
import time
import configparser

from pathlib import Path

from selenium import webdriver


def setup():
    global CONFIG, URL, CHROME_DRIVER_PTH

    CWD = Path(__file__).parent
    os.chdir(CWD)

    CONFIG_PTH = Path("./config.ini")
    CONFIG = load_config_ini(CONFIG_PTH)
    CHROME_DRIVER_PTH = Path(CONFIG["DRIVER"]["chrome"])
    URL = CONFIG["LOGIN"]["url"]


def load_config_ini(path):
    path_str = str(path)  # ensure str type.
    config = configparser.ConfigParser()
    config.read(path_str)
    return config


def open_driver():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--start-maximized")
    options.add_argument("--test-type")
    driver = webdriver.Chrome(
        chrome_options=options, executable_path=str(CHROME_DRIVER_PTH)
    )
    driver.get(URL)


def click_check_btn():
    global driver
    check_btn = driver.find_elements_by_xpath(
        '//*[@id="app"]/div/div/main/div/div/div[2]/section/div[2]/span[2]/button'
    )[0]
    check_btn.click()


def log_in_btn():
    global driver
    login_info = CONFIG["LOGIN"]

    username = driver.find_elements_by_xpath('//*[@id="username"]')[0]
    password = driver.find_elements_by_xpath('//*[@id="password"]')[0]
    log_in_btn = driver.find_elements_by_xpath(
        '//*[@id="app"]/div/form/span/button'
    )[0]

    username.send_keys(login_info["user"])
    password.send_keys(login_info["pass"])
    log_in_btn.click()


def main():
    global driver

    try:
        setup()
        open_driver()
        time.sleep(1)
        log_in_btn()
        time.sleep(2)
        click_check_btn()
        time.sleep(1)
        print("Checked!")
    except Exception as e:
        print(e)

    try:
        driver.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
