import os

cfarmCID = 'CFARMCROPSANDIDS.csv'
ApexLink = 'ApexCrop.csv'
Raw = 'JX4_table full.csv'

CfarmCropName = dict()
ApexcropName = dict()
PlanterDict = dict() #crop : lookup ID
HarvDict = dict() #crop : lookup id
CType=dict()


CatDict = dict() #type; lookup
CatDict['Small_Not_forage']=22001
CatDict['Close_seeded_legumes']=22000
CatDict['Row_crops']=22002
CatDict['Fallow']=22003
CatDict['Pasture_or_range']=22004
CatDict['Meadow']=22005
CatDict['Woods']=22006

AltString ="INSERT INTO cfarm.crop_apex(crop_lookup_id, apex_crop_id, apex_crop_category_id, planting_tractor_id, harvest_tractor_id)"

count=0
ValBase = 22100
Ord = 0
with open(Raw) as f:
    for line in f:
        if count==0:
            count=1
        else:
            THELINE = line.strip().split(',')
            CropLine = THELINE[1].split(';')
            for Crop in CropLine:
                C=Crop.strip()
                if(THELINE[4]=='Planter'):
                    PlanterDict[C]=ValBase+Ord
                if(THELINE[4]=='harvester'):
                    HarvDict[C]=ValBase+Ord           
            Ord=Ord+1


with open(cfarmCID) as f:
    for line in f:
        THELINE = line.strip().split(',')
        CfarmCropName[THELINE[1]]=THELINE[0] #cropname to crop id

count=0
with open(ApexLink) as f:
    for line in f:
        if(count==0):
            count=1
        else:
            THELINE = line.strip().split(',')
            ApexcropName[THELINE[0]] = THELINE[3]
            CType[THELINE[0]] = CatDict[THELINE[2]]

OutString = list()

for crop in CType:
    OutString.append(AltString)
    Cstring = "Values("+str(CfarmCropName[crop])+","+str(ApexcropName[crop])+","+str(CType[crop])+","+str(PlanterDict[crop])+","+str(HarvDict[crop])+");"
    OutString.append(Cstring)



print('parsing table')


open(r'OUT.txt','w').write('\n'.join(OutString))
