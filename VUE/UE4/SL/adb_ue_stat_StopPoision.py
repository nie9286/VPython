import os
import re

def get_devices():
    p = os.popen('adb devices')
    devices_str = p.read()
    devices = re.findall(r'(\w+)\s+device\s', devices_str)
    return devices

def shellcmd(device_id,command):
    cmd = 'adb -s %s shell "%s"' % (device_id, command)
    print(cmd)
    p = os.popen(cmd)
    result = p.read()
    print(result)

devices = get_devices()
for device in devices:
    print(device)
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'SolarGM_Poison End'")




