import os

class TextureSettings:
    def __init__(self):
        self.tag = "_tag"
        self.EnumRemap = "_EnumRemap"
        self.pack = 0
        self.highEnd = 0
        self.high = 0
        self.mid = 0
        self.low = 0
        self.lowEnd = 0

groups = []
#=============================================World==================================================
#1
texWorld = TextureSettings()
texWorld.tag = "World"
texWorld.EnumRemap = "World"
texWorld.pack = 512
texWorld.highEnd = 512
texWorld.high = 512
texWorld.mid = 256
texWorld.low = 128
texWorld.lowEnd = 128
groups.append(texWorld)
#2
texWorldNormal = TextureSettings()
texWorldNormal.tag = "WorldNormalMap"
texWorldNormal.EnumRemap = "WorldNormalMap"
texWorldNormal.pack = 512
texWorldNormal.highEnd = 512
texWorldNormal.high = 512
texWorldNormal.mid = 256
texWorldNormal.low = 1     #低端机不需要WorldNormal
texWorldNormal.lowEnd = 1   #低端机不需要WorldNormal
groups.append(texWorldNormal)
#3
texWorldSpecular = TextureSettings()
texWorldSpecular.tag = "WorldSpecular"
texWorldSpecular.EnumRemap = "WorldGlobalMap"
texWorldSpecular.pack = 512
texWorldSpecular.highEnd = 512
texWorldSpecular.high = 512
texWorldSpecular.mid = 512
texWorldSpecular.low = 1       #低端机不需要WorldSpecular
texWorldSpecular.lowEnd = 1    #低端机不需要WorldSpecular
groups.append(texWorldSpecular)
#=============================================Character==================================================
#4
texCharacter = TextureSettings()
texCharacter.tag = "Character"
texCharacter.EnumRemap = "Character"
texCharacter.pack = 1024
texCharacter.highEnd = 1024
texCharacter.high = 1024
texCharacter.mid = 1024
texCharacter.low = 512
texCharacter.lowEnd = 512
groups.append(texCharacter)
#5
texCharacterNormalMap = TextureSettings()
texCharacterNormalMap.tag = "CharacterNormalMap"
texCharacterNormalMap.EnumRemap = "CharacterPreview"
texCharacterNormalMap.pack = 1024
texCharacterNormalMap.highEnd = 1024
texCharacterNormalMap.high = 1024
texCharacterNormalMap.mid = 1024
texCharacterNormalMap.low = 512     #Character Preview will use Highest Resolution
texCharacterNormalMap.lowEnd = 512  #Character Preview will use Highest Resolution
groups.append(texCharacterNormalMap)
#6
texCharacterSpecular = TextureSettings()
texCharacterSpecular.tag = "CharacterSpecular"
texCharacterSpecular.EnumRemap = "CharacterSpecular"
texCharacterSpecular.pack = 1024
texCharacterSpecular.highEnd = 1024
texCharacterSpecular.high = 1024
texCharacterSpecular.mid = 1024
texCharacterSpecular.low = 512
texCharacterSpecular.lowEnd = 512
groups.append(texCharacterSpecular)
#=============================================Weapon==================================================
#7
texWeapon = TextureSettings()
texWeapon.tag = "Weapon"
texWeapon.EnumRemap = "Weapon"
texWeapon.pack = 1024
texWeapon.highEnd = 1024
texWeapon.high = 1024
texWeapon.mid = 1024
texWeapon.low = 512
texWeapon.lowEnd = 512
groups.append(texWeapon)
#8
texWeaponNormalMap = TextureSettings()
texWeaponNormalMap.tag = "WeaponNormalMap"
texWeaponNormalMap.EnumRemap = "WeaponPreview"
texWeaponNormalMap.pack = 1024
texWeaponNormalMap.highEnd = 1024
texWeaponNormalMap.high = 1024
texWeaponNormalMap.mid = 1024
texWeaponNormalMap.low = 1024       #Weapon Preview will use Highest Resolution
texWeaponNormalMap.lowEnd = 1024    #Weapon Preview will use Highest Resolution
groups.append(texWeaponNormalMap)
#9
texWeaponSpecular = TextureSettings()
texWeaponSpecular.tag = "WeaponSpecular"
texWeaponSpecular.EnumRemap = "WeaponSpecular"
texWeaponSpecular.pack = 1024
texWeaponSpecular.highEnd = 1024
texWeaponSpecular.high = 1024
texWeaponSpecular.mid = 1024
texWeaponSpecular.low = 512
texWeaponSpecular.lowEnd = 512
groups.append(texWeaponSpecular)
#=============================================Vehicle==================================================
#10
texVehicle = TextureSettings()
texVehicle.tag = "Vehicle"
texVehicle.EnumRemap = "Vehicle"
texVehicle.pack = 1024
texVehicle.highEnd = 1024 
texVehicle.high = 1024
texVehicle.mid = 1024
texVehicle.low = 512
texVehicle.lowEnd = 512
groups.append(texVehicle)
#11
texVehicleNormalMap = TextureSettings()
texVehicleNormalMap.tag = "VehicleNormalMap"
texVehicleNormalMap.EnumRemap = "VehiclePreview"
texVehicleNormalMap.pack = 1024
texVehicleNormalMap.highEnd = 1024 
texVehicleNormalMap.high = 1024
texVehicleNormalMap.mid = 1024
texVehicleNormalMap.low = 1024      #Vehicle Preview will use Highest Resolution
texVehicleNormalMap.lowEnd = 1024   #Vehicle Preview will use Highest Resolution
groups.append(texVehicleNormalMap)
#12
texVehicleSpecular = TextureSettings()
texVehicleSpecular.tag = "VehicleSpecular"
texVehicleSpecular.EnumRemap = "VehicleSpecular"
texVehicleSpecular.pack = 1024
texVehicleSpecular.highEnd = 1024 
texVehicleSpecular.high = 1024
texVehicleSpecular.mid = 512
texVehicleSpecular.low = 256     
texVehicleSpecular.lowEnd = 256   
groups.append(texVehicleSpecular)
#=============================================Cinematic==================================================
#13


current = os.getcwd()
current = current.replace("\\","/")
filePath = current +  "/Texture_Size_Settings/DefaultDeviceProfiles.ini"

config = ''
newLines = []


f = open(filePath,'r')
lines = f.readlines()
for line in lines:
    newLine=line
    if line.startswith('['):    #This is a config head......
        config=line
    elif(line.startswith("+TextureLODGroups=")):  #This line ls about texture LOD
        tokens = line.split(',')
        groupName = tokens[0].split("+TextureLODGroups=(Group=TEXTUREGROUP_")[1]
        for group in groups:
            if(groupName == group.tag):
                if config.find("Solar_Android_Low-end DeviceProfile") != -1:                
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.lowEnd))
                elif config.find("Solar_Android_Low DeviceProfile") != -1:                  
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.low)) 
                elif config.find("Solar_Android_Mid DeviceProfile") != -1:                 
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.mid)) 
                elif config.find("Solar_Android_High DeviceProfile") != -1:
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.high))
                elif config.find("Solar_Android_High-end DeviceProfile") != -1:
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.highEnd))
                elif config.find("Android DeviceProfile") != -1:
                    newLine = line.replace(tokens[7],"MaxLODSize="+str(group.pack))
                break   
    newLines.append(newLine)
f.close()

fout = open("out.txt","wt")
for line in newLines:
    fout.write(line)
fout.close()
