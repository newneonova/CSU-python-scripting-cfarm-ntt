Names = ['graceg@gmavt.net','tomharrness@myfairpoint.net','judestervt@hotmail.com','maxwellfarm1@myfairpoint.net','nelsonboysdairy@gmail.com','homesteadfarm1@msn.com']
OutString=''
Astring = "email_id = '"

for name in Names:
    OutString = OutString + ' OR '+Astring+name+"'"
