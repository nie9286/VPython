import socket
import os
import re

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)

command = "-tracehost=" + local_ip +  " -statnamedevents -trace=cpu,gpu,frame"


filename = "UE4CommandLine.txt"

f = open(filename,"w")
f.write(command)
f.close()

packageName = "/Solarland"
device_file = '/sdcard/UE4Game' +packageName + "/"+ filename


def get_devices():
    p = os.popen('adb devices')
    devices_str = p.read()
    devices = re.findall(r'(\w+)\s+device\s', devices_str)
    return devices

def pushFile(device,target_file,device_file):
    cmd = 'adb -s %s push %s %s' % (device,target_file,device_file)
    print(cmd)
    p = os.popen(cmd)
    result = p.read()
    print (result)

devices = get_devices()
for device in devices:
    print(device)
    pushFile(device,filename,device_file)