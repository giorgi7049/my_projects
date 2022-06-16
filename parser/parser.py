from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver_chrome = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-feature=AutomationControlled")


name = 'gjavakhidze'
passwd = 'gio@7049'


# Emis-ში შესვლა
def enter_emis():
    try:
        driver_chrome.get("https://statsng.emis.ge/index.php/login")
        driver_chrome.find_element(By.ID, "domain_username").clear()
        driver_chrome.find_element(By.ID, "domain_username").send_keys(name)
        driver_chrome.find_element(By.ID, "domain_password").clear()
        driver_chrome.find_element(By.ID, "domain_password").send_keys(passwd)
        option = driver_chrome.find_element(By.ID, "domain_name")
        option.get_attribute("option value")
        option.send_keys("SCHOOLS.EMIS.GE")
        btn_elm = driver_chrome.find_element(By.CLASS_NAME, "btn-primary")
        btn_elm.click()
    except Exception as ex:
        print(ex)


# ვიზიტის დაფიქსორება
def reg_emis():
    try:
        driver_chrome.find_element(By.ID, "sidebar_visits").click()
        driver_chrome.find_element(By.CLASS_NAME, "btn-primary").click()
    except Exception as ex:
        print(ex)
        print('You are not at school !!!')



# დრაივერის დახურვა
def close_driver():
    driver_chrome.close()
    driver_chrome.quit()


def chrome_version():
    chrome_ver = driver_chrome.capabilities['version']
    print(chrome_ver)


def main():
    enter_emis()
    reg_emis()
    driver_chrome.implicitly_wait(3)
    close_driver()


if __name__ == "__main__":
    main()
