import shutil, os, zipfile

RootFolder = 'Runfolder_GreatPlainsMidwest2019'
Raw = os.path.join(RootFolder, 'Raw') 
Dest=os.path.join(RootFolder, 'Chunked')


for FOLDER in os.listdir(Dest):
    print('zipping '+os.path.join(RootFolder,FOLDER+'.zip'))
    Z = zipfile.ZipFile(os.path.join(RootFolder,FOLDER+'.zip'),'w', zipfile.ZIP_DEFLATED,1)
    for file in os.listdir(os.path.join(Dest,FOLDER)):
        FF = os.path.join(os.path.join(Dest,FOLDER),file)
        Z.write(FF)
    Z.close()
    print('file zipped')
    shutil.rmtree(os.path.join(Dest,FOLDER))
