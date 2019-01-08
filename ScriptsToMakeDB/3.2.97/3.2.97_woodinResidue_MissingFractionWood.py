import os



LookupToName='LookupsToName.txt'
NameTOnFacAg = 'woodratiotable.csv'
NameToLookup=dict()
OutStrings=list()


with open(LookupToName) as f:
    for line in f:
        L=line.strip().split(';');
        NameToLookup[L[2].replace('"','')]=L[0]
with open(NameTOnFacAg) as f:
    for line in f:
        L=line.split(',')
        ID = NameToLookup[L[0]]
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    n_fraction_wood = "+str(.0011)+" WHERE lookup_id ="+str(ID))
      
 
open(r'MissingNFracWood.txt','w').write('\n'.join(OutStrings))
