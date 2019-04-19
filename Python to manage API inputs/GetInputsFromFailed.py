import shutil, os, zipfile


APIFailedFolder = 'C:\API\ApiFailed'
RootFolder = 'Runfolder_GreatPlainsMidwest2019'
SourceOfZips=os.path.join(RootFolder, 'Chunked')
Dest = os.path.join(RootFolder, 'Missing')
if not os.path.exists(Dest):
    os.makedirs(Dest)

SetOfFailedNames = set()

for Failed in os.listdir(APIFailedFolder):
    if Failed.endswith('lzma'):
        SetOfFailedNames.add(Failed.split("_2019")[0])

for Z in os.listdir(SourceOfZips):
    if Z.endswith('.zip'):
        with zipfile.ZipFile(os.path.join(SourceOfZips, Z),'r') as ZZ:
            for Entry in ZZ.namelist():
                if Entry.split('/')[1] in SetOfFailedNames:
                    print('Extracting '+Entry)
                    ZZ.extract(Entry,path=Dest)
