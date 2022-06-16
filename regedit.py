import winreg as win
import

def regedit():
    keyVal = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
    try:
        key = win.OpenKey(win.HKEY_LOCAL_MACHINE, keyVal, 0, win.KEY_ALL_ACCESS)
    except:
        key = win.CreateKey(win.HKEY_LOCAL_MACHINE, keyVal)
    win.SetValueEx(key, "123", 0, win.REG_SZ, "5")
    win.CloseKey(key)


if __name__ == '__main__':
    regedit()


class character:
    def __init__(self, armor, attack):
        self.attack = attack
        self.armor = armor
