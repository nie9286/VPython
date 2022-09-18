import os
import re
import time

def get_devices():
    p = os.popen('adb devices')
    devices_str = p.read()
    devices = re.findall(r'(\w+)\s+device\s', devices_str)
    return devices

def getFocusedPackageAndActivity():
        pattern = re.compile(r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+") #这里使用了正则表达式，对输出的内容做了限制，只会显示类似"com.mediatek.factorymode/com.mediatek.factorymode.FactoryMode"的字符串
        out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read() #window下使用findstr
        list = pattern.findall(out)
        component = list[0] #输出列表中的第一条字符串
        return component

def ExitApp(device, activeName):
    cmd = 'adb -s %s shell am force-stop %s' % (device, activeName)
    p = os.popen(cmd)
    result = p.read()
    print(result)

def LaunchApp(device, packageName, call_back=None):
    cmd = 'adb -s %s shell am start -S -W %s' % (device,packageName)
    p = os.popen(cmd)
    result = p.read()
    print(result)
    if call_back is not None:
        call_back()



active = getFocusedPackageAndActivity()
a = active.split("/")
packageName = a[0]

devices = get_devices()

for device in devices:
    print(device)
    print(packageName)
    ExitApp(device,packageName)


time.sleep(2)


def LaunchCallback():
    print("Restart the APP")

for device in devices:
    print(device)
    print(active)
    LaunchApp(device,active,LaunchCallback)





