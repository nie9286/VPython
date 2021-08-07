import os

class TextureSettings:
    def __init__(self):
        self.tag = "_tag"
        self.EnumRemap = "_EnumRemap"
        self.pack = 512
        self.highEnd = 512
        self.high = 512
        self.mid = 512
        self.low = 512
        self.lowEnd = 512

groups = []
#=============================================World==================================================
#1
texWorld = TextureSettings()
texWorld.tag = "World"
texWorld.EnumRemap = "World"
texWorld.pack = 8192
texWorld.highEnd = 1024
texWorld.high = 512
texWorld.mid = 256
texWorld.low = 128
texWorld.lowEnd = 8192
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
texCinematic = TextureSettings()
texCinematic.tag = "Cinematic"
texCinematic.EnumRemap = "UI-Splash"
texCinematic.pack = 1024
texCinematic.highEnd = 1024
texCinematic.high = 1024
texCinematic.mid = 1024
texCinematic.low = 512
texCinematic.lowEnd = 256
groups.append(texCinematic)
#=============================================Effects==================================================
#14
texEffects = TextureSettings()
texCinematic.tag = "Effects"
texCinematic.EnumRemap = "Effects"
texCinematic.pack = 128
texCinematic.highEnd = 128
texCinematic.high = 128
texCinematic.mid = 128
texCinematic.low = 64
texCinematic.lowEnd = 64
groups.append(texEffects)
#15
texEffectsAtlas = TextureSettings()
texEffectsAtlas.tag = "EffectsNotFiltered"
texEffectsAtlas.EnumRemap = "EffectsAtlas"
texEffectsAtlas.pack = 1024
texEffectsAtlas.highEnd = 1024
texEffectsAtlas.high = 1024
texEffectsAtlas.mid = 512
texEffectsAtlas.low = 256
texEffectsAtlas.lowEnd = 256
groups.append(texEffectsAtlas)
#=============================================Skybox==================================================
#16
texSkybox = TextureSettings()
texSkybox.tag = "Skybox"
texSkybox.EnumRemap = "Skybox"
texSkybox.pack = 1024
texSkybox.highEnd = 1024
texSkybox.high = 1024
texSkybox.mid = 512
texSkybox.low = 512
texSkybox.lowEnd = 256
groups.append(texSkybox)
#=============================================UI==================================================
#17
texUI = TextureSettings()
texUI.tag = "UI"
texUI.EnumRemap = "UI"
texUI.pack = 1024
texUI.highEnd = 1024
texUI.high = 1024
texUI.mid = 1024
texUI.low = 1024                    # No Scale for UI
texUI.lowEnd = 1024                 # No Scale for UI
#=============================================Lightmap==================================================
#17
texLightmap = TextureSettings()
texLightmap.tag = "Lightmap"
texLightmap.EnumRemap = "Lightmap"
texLightmap.pack = 1024
texLightmap.highEnd = 1024
texLightmap.high = 1024
texLightmap.mid = 1024
texLightmap.low = 256
texLightmap.lowEnd = 128
groups.append(texLightmap)
#=============================================RenderTarget==================================================
#19
texRenderTarget = TextureSettings()
texRenderTarget.tag = "RenderTarget"
texRenderTarget.EnumRemap = "RenderTarget"
texRenderTarget.pack = 32
texRenderTarget.highEnd = 32
texRenderTarget.high = 32
texRenderTarget.mid = 32
texRenderTarget.low = 32
texRenderTarget.lowEnd = 32
groups.append(texRenderTarget)
#=============================================PropsImportant==================================================
#20
texPropsImportant = TextureSettings()
texPropsImportant.tag = "MobileFlattened"
texPropsImportant.EnumRemap = "PropsImportant"
texPropsImportant.pack = 1024
texPropsImportant.highEnd = 1024
texPropsImportant.high = 1024
texPropsImportant.mid = 1024
texPropsImportant.low = 512
texPropsImportant.lowEnd = 256
groups.append(texPropsImportant)
#=============================================BuildingImportant==================================================
#21
texBuildingImportant = TextureSettings()
texBuildingImportant.tag = "ProcBuilding_Face"
texBuildingImportant.EnumRemap = "BuildingImportant"
texBuildingImportant.pack = 8192
texBuildingImportant.highEnd = 8192
texBuildingImportant.high = 8192
texBuildingImportant.mid = 8192
texBuildingImportant.low = 8192
texBuildingImportant.lowEnd = 8192
groups.append(texBuildingImportant)





dir_path = os.path.dirname(os.path.realpath(__file__))

filePath = dir_path +  "/DefaultDeviceProfiles.ini"

config = ''
newLines = []
remapReplaces = []

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
                    remapReplaces.append("TEXTUREGROUP_" + group.tag + ".DisplayName"+"="+group.EnumRemap + "_" + str(group.pack) + "\n")
                break   
    newLines.append(newLine)
f.close()

fout = open(filePath,"wt")
for line in newLines:
    fout.write(line)
fout.close()


#====================================Update DefaultEngine.ini===============================================
filePath = dir_path +  "/DefaultEngine.ini"
f = open(filePath,'r')
lines = f.readlines()
newLines = []

for line in lines:
    newLine = line
    if line.startswith("TEXTUREGROUP_"):
        for lineRemap in remapReplaces:
            lineStart = lineRemap.split("=")[0]
            if(line.startswith(lineStart)):
                newLine = lineRemap
                break
    newLines.append(newLine)


fout = open(filePath,"wt")
for line in newLines:
    fout.write(line)
fout.close()
           


