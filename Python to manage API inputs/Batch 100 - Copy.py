import shutil, os, zipfile

RootFolder = 'rerulIL'
Raw = os.path.join(RootFolder, 'Raw') 
Dest=os.path.join(RootFolder, 'Chunked')
if not os.path.exists(Dest):
    os.makedirs(Dest)
    INum=0
    Fcount=0
    DestLoc = os.path.join(Dest, 'Res'+str(INum))
    os.makedirs(DestLoc)
    for filename in os.listdir(Raw):
        if filename.endswith(".xml"):
            file = os.path.join(Raw, filename)
            dest = os.path.join(DestLoc, filename)
            shutil.move(file,dest)
            Fcount=Fcount+1
            if Fcount>500:
                print('zipping '+os.path.join(RootFolder,'Res'+str(INum)+'.zip'))
                #Z = zipfile.ZipFile(os.path.join(RootFolder,'Res'+str(INum)+'.zip'),'w', zipfile.ZIP_DEFLATED,1)
                #for each in os.listdir(DestLoc):
                #    try:
                #        Z.write(os.path.join(DestLoc,each))
                #    except IOError:
                #        None
                #Z.close()
                #shutil.rmtree(DestLoc)
                print('finished creating zipfile')
                Fcount=0
                INum=INum+1
                DestLoc = os.path.join(Dest, 'Res'+str(INum))
                os.makedirs(DestLoc)

    #Z = zipfile.ZipFile(os.path.join(RootFolder,'Res'+str(INum)+'.zip'),'w')
    #for each in os.listdir(DestLoc):
    #    try:
    #       Z.write(os.path.join(DestLoc+each))
    #    except IOError:
    #        None
    #Z.close()
    #shutil.rmtree(DestLoc)
