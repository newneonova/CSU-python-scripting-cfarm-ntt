import os.path
PrismDB='GridXGridYGridXWindowGridYWindow.txt'
WDir='W/'

#First check PrismDB to see for how many and which lines
#gridWindow can't be derived by the rule we found
#grid % 3, if 2 then window, if 1 then add 1, if 0 the subtract 1

#Then check for each derived window pair
#if a prism weather file exists for it.

#'W/prism_'+gridYWindow+'/'+gridYwindow+'_'+gridXwindow+'.bz2'

def Offset(C):
    N=C%3
    if(N==2):
        return 0
    if(N==1):
        return 1
    if(N==0):
        return -1
        


WindowWrong=list()
MissingFile=list()
c=0
with open(PrismDB,'r') as f:
    for line in f:
        if(c%1000==0):
            print(c)
        c=c+1
        SPLITTED = line.split(';')
        x=int(SPLITTED[0])
        y=int(SPLITTED[1])
        SPLITTED[2].strip()
        SPLITTED[3]=SPLITTED[3].strip('\n')
        xw=int(SPLITTED[2]) if SPLITTED[2] else 0
        yw=int(SPLITTED[3]) if SPLITTED[3] else 0
        if(x+Offset(x) != xw or y+Offset(y) != yw):
            WindowWrong.append(line)
        FileString = 'W/prism_'+str(y+Offset(y))+'/'+str(y+Offset(y))+'_'+str(x+Offset(x))+'.bz2'
        if(not os.path.isfile(FileString)):
            MissingFile.append(line)

open('WindowMisalign_'+str(len(WindowWrong))+'.txt','w').write(''.join(WindowWrong))
open('MissingPrismFile'+str(len(MissingFile))+'.txt','w').write(''.join(MissingFile))

