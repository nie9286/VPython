
import re

f = open("SL_Log2.txt", "r")

scenes = []
shaders = []
Characters = []
biomes = []
landscape = []
buildings = []
props = []
vehicle = []
weapons = []
powerBags = []
interactiveObjects = []
vfx = []
UI = []
misc = []
WwiseAudio = []
others = []

for line in f.readlines():                          #依次读取每行  
    line = line.strip()                             #去掉每行头尾空白  
    if(re.search("Warning",line) or re.search("error",line)):
        if(re.search("01_Scenes",line)):
            scenes.append(line)
        elif(re.search("02_Shaders",line)):
            shaders.append(line)
        elif(re.search("03_Characters",line)):
            Characters.append(line)
        elif(re.search("04_Biomes",line)):
            biomes.append(line)
        elif(re.search("05_Landscape",line)):
            landscape.append(line)
        elif(re.search("06_Buildings",line)):
            buildings.append(line)
        elif(re.search("07_Props",line)):
            props.append(line)
        elif(re.search("08_Vehicles",line)):
            vehicle.append(line)
        elif(re.search("09_Weapons",line)):
            weapons.append(line)  
        elif(re.search("10_PowerBags",line)):
            powerBags.append(line)    
        elif(re.search("11_InteractiveObjects",line)):
            interactiveObjects.append(line)    
        elif(re.search("12_VFX",line)):
            vfx.append(line)   
        elif(re.search("13_UI",line)):
            UI.append(line)
        elif(re.search("15_Misc",line)):
            misc.append(line)
        elif(re.search("16_WwiseAudio",line)):
            WwiseAudio.append(line)
        else:
            others.append(line)

def WriteToFile(listObj,name):
    if(len(listObj) > 0):
        with open(name, 'w') as f:
            for item in listObj:
                f.write("%s\n" % item)


#WriteToFile(scenes,"scene.txt")
#WriteToFile(shaders,"shaders.txt")
#WriteToFile(Characters,"Characters.txt")
#WriteToFile(biomes,"biomes.txt")
#WriteToFile(landscape,"landscape.txt")
#WriteToFile(buildings,"buildings.txt")
#WriteToFile(props,"props.txt")
#WriteToFile(vehicle,"vehicle.txt")
#WriteToFile(weapons,"weapons.txt")
#WriteToFile(powerBags,"powerBags.txt")
#WriteToFile(interactiveObjects,"interactiveObjects.txt")
#WriteToFile(vfx,"vfx.txt")
#WriteToFile(UI,"UI.txt")
#WriteToFile(misc,"misc.txt")
#WriteToFile(WwiseAudio,"WwiseAudio.txt")
#WriteToFile(others,"others.txt")


def printline_n(listObj):
    if(len(listObj) > 0):
        for item in listObj :
            print("%s\n" % item)
        for x in range(3):
            print("===============================================================================================================" + str(x))

printline_n(scenes)
printline_n(shaders)
printline_n(Characters)
printline_n(biomes)
printline_n(landscape)
printline_n(buildings)
printline_n(props)
printline_n(vehicle)
printline_n(weapons)       
printline_n(powerBags) 
printline_n(interactiveObjects) 
printline_n(vfx) 
printline_n(UI) 
printline_n(misc) 
printline_n(WwiseAudio)
printline_n(others)
          

    