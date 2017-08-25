import os

SpinupTable=r'RawData\eqruns2017_spinup_sitefile_lookup.csv'
Fips=r'RawData\ListOfFips.txt'
MapUnit=r'RawData\UserMapUnits.txt'

SpinupFips = set()
SpinupUnit = set()
ActualFips = set()
ActualUnit = set()

print('parsing spinup table')
with open(SpinupTable) as f:
    for line in f:
        THELINE = line.split(',')
        SpinupFips.add(THELINE[1])
        SpinupUnit.add(THELINE[2])
print('parsing fips')
with open(Fips) as f:
    for line in f:
        ActualFips.add(line.strip(' \t\n\r'))
print('parsing map units')
with open(MapUnit) as f:
    for line in f:
        ActualUnit.add(line.strip(' \t\n\r'))

AbsentFips = ActualFips - SpinupFips
AbsentUnit = ActualUnit - SpinupUnit

print('Fips not present:'+str(len(AbsentFips))+' or '+str(len(AbsentFips)/len(ActualFips)*100)+'%')
print('Mapunits not present:'+str(len(AbsentUnit))+' or '+str(len(AbsentUnit)/len(ActualUnit)*100)+'%')

print('writing missing map units and fips')
open('RawData\MissingFips_'+str(len(AbsentFips))+'.txt','w').write('\n'.join(list(AbsentFips)))
open('RawData\MissingMapUnits_'+str(len(AbsentUnit))+'.txt','w').write('\n'.join(list(AbsentUnit)))
