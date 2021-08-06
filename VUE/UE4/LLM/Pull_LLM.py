import os
import re

scirptPath = os.path.dirname(os.path.realpath(__file__))
packageName = "/SolarLand"
device_file = '/sdcard/UE4Game' +packageName + packageName +'/Saved/Profiling/LLM'
copyToDir = scirptPath




def get_devices():
    p = os.popen('adb devices')
    devices_str = p.read()
    devices = re.findall(r'(\w+)\s+device\s', devices_str)
    return devices

def pushFile(device,target_file,device_file):
    cmd = 'adb -s %s pull %s %s' % (device,device_file,target_file)
    print(cmd)
    p = os.popen(cmd)
    result = p.read()
    print (result)

devices = get_devices()
for device in devices:
    print(device)
    pushFile(device,copyToDir,device_file)



