import os

SpinupTable=r'RawData\eqruns2017_spinup_sitefile_lookup_2017_09_30.csv'


SpinupUnit = set()


print('parsing spinup table')
with open(SpinupTable) as f:
    for line in f:
        THELINE = line.split(',')
        SpinupUnit.add(THELINE[2])


print("Here are the present Map units")

open(r'RawData\MapUnitsInSpinup_'+str(len(SpinupUnit))+'.txt','w').write('\n'.join(list(SpinupUnit)))
