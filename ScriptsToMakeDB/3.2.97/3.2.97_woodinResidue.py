import os



LookupToName='LookupsToName.txt'
NameTOnFacAg = 'woodratiotable.csv'
NameToLookup=dict()
OutStrings=list()

LeadPart='INSERT INTO cfarm.crop_wood_ratio_table (lookup_id, leaf_death_rate, wood_juvenile_root_death_rate,wood_mature_root_death_rate,n_fraction_fine_roots,n_fraction_leaves) VALUES ('

with open(LookupToName) as f:
    for line in f:
        L=line.strip().split(';');
        NameToLookup[L[2].replace('"','')]=L[0]
with open(NameTOnFacAg) as f:
    for line in f:
        L=line.split(',')
        ID = NameToLookup[L[0]]
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    leaf_death_rate = "+str(L[1])+" WHERE lookup_id ="+str(ID))
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    wood_juvenile_root_death_rate = "+str(L[2])+" WHERE lookup_id ="+str(ID))
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    wood_mature_root_death_rate = "+str(L[3])+" WHERE lookup_id ="+str(ID))
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    n_fraction_fine_roots = "+str(L[4])+" WHERE lookup_id ="+str(ID))
        OutStrings.append(" UPDATE cfarm.harvest_residue SET    n_fraction_leaves = "+str(L[5])+" WHERE lookup_id ="+str(ID))
      
 
open(r'appendTable.txt','w').write('\n'.join(OutStrings))
