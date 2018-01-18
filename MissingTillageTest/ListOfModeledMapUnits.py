import os

SpinupTable=r'TillageTable.txt'




AllCrop=set()
CropWithC = set()
CropWithMow = set()
CropWithCRMP = set()
CropWithA = set()
CropWithAC = set()
CropWithHERB = set()
print('parsing tillage table')
with open(SpinupTable) as f:
    for line in f:
        THELINE = line.split(';')
        crop = THELINE[1]
        till = THELINE[2]
        AllCrop.add(crop)
        if(str(till) =='1004'):
            CropWithAC.add(crop)
        if(str(till) =='1005'):
            CropWithA.add(crop)
        if(str(till) =='1006'):
            CropWithC.add(crop)
        if(str(till) =='1007'):
            CropWithMow.add(crop)
        if(str(till) =='1008'):
            CropWithCRMP.add(crop)
        if(str(till) =='1009'):
            CropWithHERB.add(crop)               



print("Here are the present Map units")

open('1004','w').write('\n'.join(list(AllCrop-CropWithAC)))
open('1005','w').write('\n'.join(list(AllCrop-CropWithA)))
open('1006','w').write('\n'.join(list(AllCrop-CropWithC)))
open('1007','w').write('\n'.join(list(AllCrop-CropWithMow)))
open('1008','w').write('\n'.join(list(AllCrop-CropWithCRMP)))
open('1009','w').write('\n'.join(list(AllCrop-CropWithHERB)))
