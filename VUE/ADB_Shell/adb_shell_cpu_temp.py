import os

#os.system("adb shell ls sys/class/thermal/")                            # List all Thermal_zone
os.system("adb shell cat /sys/class/thermal/thermal_zone*/type") 
os.system("adb shell cat /sys/class/thermal/thermal_zone*/temp")
