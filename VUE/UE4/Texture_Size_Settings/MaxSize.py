filePath = "S:/Singularity_dev-programmer/Frontend/Games/Solarland/Config/DefaultDeviceProfiles.ini"

f = open(filePath,'r')

lines = f.readlines()

BaseProfileName = ''
label = "+TextureLODGroups=(Group=TEXTUREGROUP_"

class TextureSettings:
    def __init__(self,_tag:str,_EnumRemap:str,_pack:int,_highEnd:int,_heigh:int,_mid:int,_low:int,_lowEnd:int):
        self.tag = _tag
        self.EnumRemap = _EnumRemap
        self.pack = _pack
        self.highEnd = _highEnd
        self.high = _heigh
        self.mid = _mid
        self.low = _low
        self.lowEnd = _lowEnd
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
#2
texWorldNormal = TextureSettings()
texWorldNormal.tag = "WorldNormalMap"
texWorldNormal.EnumRemap = "WorldNormalMap"
texWorldNormal.pack = 512
texWorldNormal.highEnd = 512
texWorldNormal.high = 512
texWorldNormal.mid = 256
texWorldNormal.low = 32     #低端机不需要WorldNormal
texWorldNormal.lowEnd =32   #低端机不需要WorldNormal
#3
texWorldSpecular = TextureSettings()
texWorldSpecular.tag = "WorldSpecular"
texWorldSpecular.EnumRemap = "WorldGlobalMap"
texWorldSpecular.pack = 512
texWorldSpecular.highEnd = 512
texWorldSpecular.high = 512
texWorldSpecular.mid = 512
texWorldSpecular.low = 32       #低端机不需要WorldSpecular
texWorldSpecular.lowEnd = 32    #低端机不需要WorldSpecular
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
#=============================================Cinematic==================================================
#13







for line in lines:
    if line.startswith('BaseProfileName'):
        BaseProfileName = line
    if line.startswith("+TextureLODGroups=(Group=TEXTUREGROUP_World"):
        tokens = line.split(',')
        groupName = tokens[0].split(label)[1]
        print(groupName)
        for token in tokens[1:]:
            print(token)
                

    #if line.startswith("+TextureLODGroups"):
    #    print(line)


f.close()