import winreg

access_register = winreg.ConnectRegistry('DoorSRV', winreg.HKEY_LOCAL_MACHINE)
access_key = winreg.OpenKey(access_register, r'SYSTEM\ControlSet001\Control\Terminal Server\RCM\GracePeriod', 0,
                            winreg.KEY_ALL_ACCESS)


def delete_value():
    try:
        if winreg.QueryValueEx(access_key, '123'):
            print('---------value found----------')
            winreg.DeleteValue(access_key, '123')
            print('value deleted cussec')
    except FileNotFoundError as e:
        print('value not found')


delete_value()
