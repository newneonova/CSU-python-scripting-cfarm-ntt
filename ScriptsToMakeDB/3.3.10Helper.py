import os

Raw='JX4_table.csv'

OutString = list()
AltString ="INSERT INTO cfarm.lookups(lookup_id, lookup_group_name, code, name, description, active,ordinal)"

print('parsing table')
count=0
ValBase = 22100
Ord = 0
with open(Raw) as f:
    for line in f:
        if count==0:
            count=1
        else:
            THELINE = line.strip().split(',')
            NewLine = "Values ("+str((ValBase+Ord))+",'APEX_TRACTOR','"+THELINE[2]+"','"+THELINE[3]+"','"+THELINE[1]+" "+THELINE[0]+"','Y',"+str(Ord)+");"
            Ord=Ord+1
            OutString.append(AltString)
            OutString.append(NewLine)

open(r'OUT.txt','w').write('\n'.join(OutString))
