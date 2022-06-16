import time
import webbrowser as web
import os
import subprocess as sb


def gettasks(name):
    taskkill = f"taskkill /im {name} /f"
    r = os.popen('tasklist /v').read().strip().split('\n')
    print('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in s:
            os.system(taskkill)
    open_url()
    return []


def nexu(name):
    taskkill = f"taskkill /im {name} /f"
    r = os.popen('tasklist /v').read().strip().split('\n')
    print('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print(f's in {s}')
            os.system(taskkill)
    java()
    return []


def java():
    sb.Popen(
        ['java', '-Djavafx.preloader=lu.nowina.nexu.NexUPreLoader -Dglass.accessible.force=false', '-jar',
         r'C:\nexu\nexu-bundle\nexu.jar'])


def open_url():
    url = r'https://nexu.municipal.gov.ge/main?token=NIlJeocTCe1RbzAeErel3KkHG3bAMfoL'
    web.register('chrome.exe', None, web.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
    web.get('chrome.exe').open(url)


if __name__ == "__main__":
    print(r"C:\nexu\nexu-bundle\nexu.jar")
    print(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    nexu('java.exe')
    time.sleep(10)
    gettasks('chrome.exe')
