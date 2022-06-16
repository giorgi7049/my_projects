from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver_chrome = webdriver.Chrome()


name = 'giorgi7049'
passwd = 'marcoPOLO0909'


def enter_teslamedia():
    try:
        driver_chrome.get("https://teslavideomedia.com/login")
        driver_chrome.find_element(By.ID, "van-field-1-input").clear()
        driver_chrome.find_element(By.ID, "van-field-1-input").send_keys(name)
        driver_chrome.find_element(By.ID, "van-field-2-input").clear()
        driver_chrome.find_element(By.ID, "van-field-2-input").send_keys(passwd)
        btn_elm = driver_chrome.find_element(By.CLASS_NAME, "van-button--primary")
        btn_elm.click()
    except Exception as ex:
        print(ex)


def close_add():
    driver_chrome.implicitly_wait(3)
    clk_span = driver_chrome.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/div/div/span/img')
    clk_span.click()


def go_task():
    btn_task = driver_chrome.find_element(By.XPATH, '//*[@id="app"]/div/button[3]/div[1]/img')
    btn_task.click()
    driver_chrome.implicitly_wait(3)
    finish_task()


def finish_task():
    clk_to_finish = driver_chrome.find_element(By.CLASS_NAME, 'm-gold-btn')
    clk_to_finish.click()
    driver_chrome.implicitly_wait(5)
    clk_to_finish1 = driver_chrome.find_element(By.CLASS_NAME, 'van-dialog__confirm')
    clk_to_finish1.click()
    close_add()



def close_chrome():
    driver_chrome.close()
    driver_chrome.quit()


def main():
    enter_teslamedia()
    close_add()
    go_task()
    finish_task()
    close_chrome()


if __name__ == '__main__':
    main()
