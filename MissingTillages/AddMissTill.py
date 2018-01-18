import os

MissingHERB=[265,266,267,268,269,270,271,272,273,900,901,902,903,904,905,906,907,908,909,910,911,912,913]
MissingCRMP = [265,272,267,268,273,266,271,269,270]
MissingMOW = [265,272,267,268,273,266,271,269,270]
MissingGROW = [265,272,267,268,273,266,271,269,270]

SQL =''

SQL+='#Adding Missing HERB tillages\n'

for ID in MissingHERB:
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1009,0,'HERB',1050);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1009,0,'HERB',1051);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1009,0,'HERB',1052);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1009,0,'HERB',1053);\n"

SQL+='\n\n#Adding Missing CRMP MOW and GROW tillages\n'

for ID in MissingCRMP:
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1008,0,'CRMP',1050);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1008,0,'CRMP',1051);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1008,0,'CRMP',1052);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1008,0,'CRMP',1053);\n"
    
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1007,0,'MOW',1050);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1007,0,'MOW',1051);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1007,0,'MOW',1052);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1007,0,'MOW',1053);\n"

    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1006,0,'C',1050);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1006,0,'C',1051);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1006,0,'C',1052);\n"
    SQL+="INSERT INTO cfarm.crop_cultivation_events(crop_lookup_id,tillage_lookup_id,relative_day,model_parameter,season_id) Values("+str(ID)+",1006,0,'C',1053);\n"

open('TILL.txt','w').write(SQL)
