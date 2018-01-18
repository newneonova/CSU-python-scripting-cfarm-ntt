import os.path, shutil
PrismDB='NewMisWeatherList.txt'
WDir='W/'
FullWdir='//cnrdom.colostate.edu/wcnr-network/Research/Paustian/CFARM/daycentservice/2017EqRuns_marke/prism_contUS2016/'
AddToW='AddToW/'

#First check PrismDB to see for how many and which lines
#gridWindow can't be derived by the rule we found
#grid % 3, if 2 then window, if 1 then add 1, if 0 the subtract 1

#Then check for each derived window pair
#if a prism weather file exists for it.

#'W/prism_'+gridYWindow+'/'+gridYwindow+'_'+gridXwindow+'.bz2'

def Offset(C):
    return 0
    N=C%3
    if(N==2):
        return 0
    if(N==1):
        return 1
    if(N==0):
        return -1
        


MissingWFname=list()
MissingFile=list()
c=0
with open(PrismDB,'r') as f:
    for line in f:
        if(c%1000==0):
            print(c)
        c=c+1
        SPLITTED = line.strip().split(';')
        x=int(SPLITTED[1])
        y=int(SPLITTED[0])
        FileString = 'prism_'+str(y+Offset(y))+'/'+str(y+Offset(y))+'_'+str(x+Offset(x))+'.bz2'
        FullFileString = 'prism_'+str(y+Offset(y))+'/'+str(y+Offset(y))+'_'+str(x+Offset(x))+'.wth.bz2'
        if(not os.path.isfile(WDir+FileString)):
            if(os.path.isfile(FullWdir+FullFileString)):
                if(not os.path.isdir(AddToW+'prism_'+str(y+Offset(y))+'/')):
                   os.mkdir(AddToW+'prism_'+str(y+Offset(y))+'/')
                shutil.copyfile(FullWdir+FullFileString,AddToW+FileString)
            else:
                   MissingWFname.append('prism_'+str(y+Offset(y))+'/'+str(y+Offset(y))+'_'+str(x+Offset(x))+'.wth.bz2\n')
                   MissingFile.append(line)
MissingFile=list(set(MissingFile))
MissingWFname=list(set(MissingWFname))
open('FinalNewMissingPrismFile'+str(len(MissingFile))+'.txt','w').write(''.join(MissingFile))
open('FinalAbsentWeatherFiles'+str(len(MissingWFname))+'.txt','w').write(''.join(MissingWFname))
