import subprocess as sb
import winreg

'''Powershell ის ბრძანებათა სია რომლის მიხედვითაც ვთიშავთ windows defender-ს და exclution-ში ვაგდებთ სასურველ 
საქაღალდეს და პროცესებს '''

defender_list = [
    r'powershell -inputformat none -outputformat none -NonInteractive -Command Set-MpPreference -DisableRealtimeMonitoring $true',
    r'powershell -inputformat none -outputformat none -NonInteractive -Command add-MpPreference -ExclusionExtension C:\Windows\SysWOW64\Mpk',
    r'powershell -inputformat none -outputformat none -NonInteractive -Command add-MpPreference -ExclusionExtension C:\ProgramData\KMSAuto\bin',
    r'powershell -inputformat none -outputformat none -NonInteractive -Command add-MpPreference -ExclusionPath C:\!KMSAuto',
    r'powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionProcess "MSEmulator"'
]


def compName():
    hostname = sb.run(r'powershell hostname', shell=True)
    return hostname


def disable_defender(dlist):
    for disdef in dlist:
        sb.run(disdef, shell=True)

print('Process Started')

compName()
# disable_defender(defender_list)

print('Process Finish')
