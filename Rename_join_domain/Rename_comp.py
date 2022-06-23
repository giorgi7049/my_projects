import subprocess as sb
import winreg as win
import time
import socket
import wmi

''' გლობალური ცვლადების გამოცხადება '''
std_out = 'The changes will take effect after you restart the computer'
comp_name = sb.run(f'powershell hostname', shell=True, stdout=sb.PIPE)
compName_return = str(comp_name.stdout)
p1 = compName_return.lstrip(r"b'")
p2 = p1.rstrip(r"\r\n'")
p2.upper()
credentional = 'giorgi.javakhidze'

''' WMI-დან ვიღებთ Comp და NetBios სახელებს '''
def get_wmi():
    w= wmi.WMI()
    for s in w.Win32_ComputerSystem():
        print(f'Domain:\t\t {s.domain}')
        print(f'Net Bios:\t {s.caption}')

''' Windows-ის რეგისტრში ვთიშავთ Auto logon-ს '''
def regedit():
    keyVal = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
    try:
        key = win.OpenKey(win.HKEY_LOCAL_MACHINE, keyVal, 0, win.KEY_ALL_ACCESS)
    except:
        key = win.CreateKey(win.HKEY_LOCAL_MACHINE, keyVal)
    win.SetValueEx(key, "AutoAdminLogon", 1, win.REG_SZ, '0')
    win.CloseKey(key)

''' ვაყენებთ Powershell-ის სკრიპტის შესრულების პოლიტიკას '''
def set_policy():
    try:
        sb.run(f'powershell Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force')
    except:
        print('Cennot Set Execution Policy')

''' სახელის გადარქმევა '''
def rename_comp():
    input_com = str(input("Set New Name: ").upper())
    try:
        if p2 != input_com:
            sb.run(f'powershell Rename-Computer -NewName {input_com} -DomainCredential {credentional}', shell=True)
            print('Name set success')
        elif p2 == input_com:
            print('Please Set another Name')
            rename_comp()
    except Exception as e:
        print('Somthing wrong restart program')

''' Domain-ში გაწევრიანება '''
def join_domain():
    print('Try to Join Domain')
    print('------------------')
    input_domain = str(input("Add Domain Name: "))
    sb.run(f'powershell Add-Computer -DomainName {input_domain} -Credential {credentional}', shell=True)

''' Domain-იდან კომპის გამოყვანა '''
def remove_domain():
    print('Try to remove Computer from Domain')
    print('----------------------------------')
    sb.run(f'powershell Remove-Computer -UnjoinDomainCredential {credentional} -Force -Restart')

''' კომპიუტერის სახელზე პრეფიქსის დამატება '''
def prefix():
    sb.run(f'powershell Rename-Computer -NewName BORJ-{p2}', shell=True)

''' ახალი მომხმარებლის დამატება და ადმინისტრატორის ჯგუფში გაწევრიანება '''
def new_user(user_name):
    sb.run(f'powershell New-LocalUser -Name {user_name} -NoPassword', shell=True, )
    sb.run(f'powershell Add-LocalGroupMember -Group Administrators -Member {user_name}', shell=True)

''' კომპიუტერის დარესტარტება '''
def restart(i):
    if 'y' == i:
        sb.run(f'powershell Restart-Computer', shell=True)
        print('Computer will be restarted')
    elif 'n' == i:
        main()

''' პროგრამის მენიუს რეალიზაცია '''
def run(i):
    if 1 == i:
        rename_comp()
        main()
    elif 2 == i:
        join_domain()
        main()
    elif 3 == i:
        remove_domain()
        main()
    elif 4 == i:
        prefix()
        main()
    elif 5 == i:
        restart(str(input('Restart Computer Y/N: ')))
    elif 6 == i:
        new_user(input("New User:"))
        main()
    else:
        print('Choise another command')
        run(i)


def get_IP():
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

def main():
    get_wmi()
    get_IP()
    set_policy()
    print(f'Comp Name:\t {p2}')
    print(f'IP address:\t {get_IP()}')
    print('------------------')
    print('Rename Computer: 1')
    print('Join Domain : 2')
    print('Remove computer from Domain: 3')
    print('Set Prefix : 4')
    print('Restart Computer: 5')
    print('Create new User: 6')
    print('------------------')
    run(int(input('Set Option: ')))
    time.sleep(5)


if __name__ == '__main__':
    main()
