import subprocess as sb
import os
import time
import winshell
from win32com.client import Dispatch

''' ვაცხადებთ Windows 10 გასააქტიურებელი სკრიპტს dsa '''

win_act = ['cscript slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',
           'cscript slmgr.vbs /skms 172.19.160.18:1688',
           'cscript slmgr.vbs /ato']

''' ვაცხადებთ Office 2019 Pro გასააქტიურებელ სკრიფტს'''

off_act = ['cscript ospp.vbs /sethst:172.19.160.18',
           'cscript ospp.vbs /act']

''' ვამოწმებთ არსებობს თუ არა სისტემაში ოფისის საქაღალდეები'''

office_x64_path = os.path.abspath(r'C:\Program Files\Microsoft Office\Office16')
office_x86_path = os.path.abspath(r'C:\Program Files (x86)\Microsoft Office\Office16')

''' მეთოდი რომელიც ამუშავებს ზემოთ აღნიშნულ ინფორმაციას და ააქტიურებს პროდუცტს სერვერთან კავშირით'''


def windows_activate():
    for win in win_act:
        os.chdir(r'c:\windows\system32')
        sb.run(win, shell=True)
    print('------------Windows Activate success-------------\n\n')


def office_activation():
    try:
        if os.path.exists(office_x64_path):
            for off_x64 in off_act:
                os.chdir(office_x64_path)
                sb.run(off_x64, shell=True)
            print('\n -------------------- Office x64 Activate success ------------------- \n')
        elif os.path.exists(office_x86_path):
            for off_x86 in off_act:
                os.chdir(office_x86_path)
                sb.run(off_x86, shell=True)
            print('\n -------------------- Office x86 Activate success ------------------- \n')
    except:
        print('Office not found. Please install office')


def create_shortcut():
    startup_folder = winshell.startup()
    startup_path = os.path.join(startup_folder, 'activate.lnk')
    target_path = r'C:\!KMSAuto Net 2017\activate.exe'
    w_dir = r'C:\!KMSAuto Net 2017'

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(startup_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = w_dir
    shortcut.save()

def main():
    windows_activate()
    office_activation()
    create_shortcut()
    time.sleep(5)

if __name__ == '__main__':
    main()
