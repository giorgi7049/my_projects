from winregistry import WinRegistry as Reg


def delete_rdp_license():
    key = r'HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod'
    volume = 'L$RTMTIMEBOMB_1320153D-8DA3-4e8e-B27B-0D888223A588'
    reg = Reg()
    try:
        if reg.read_key(key) and reg.read_value(key, volume):
            reg.delete_value(key, volume)
        print('RPD Licensi is delete')
    except Exception as ex:
        print('RDP Key or Volume are not finding')
    finally:
        reg.close()
        print('Registry is closed')


delete_rdp_license()
