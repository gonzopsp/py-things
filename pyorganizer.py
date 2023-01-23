import os
import shutil
##extensions
pic=[".jpg",".png",".bmp",".jpeg"]
docs=[".pdf",".docx",".ppt",".xlsx",".txt",".pptx",".xls",".doc"]
compressed=[".zip",".rar",".gz"]
sounds=[".mp3",".wav",".flac",".aif",".mid"]




path = os.getcwd()
    
print(path)
dirpic=os.path.join(path, "pics")
dirdocs=os.path.join(path,'docs')
dircomp=os.path.join(path,'comp')
dirsounds=os.path.join(path,'sounds')
#print(dirpic,dirdocs,dircomp,dirsounds)
##program
##creating folders

try:
    os.mkdir(dirpic)
except OSError as error:
    print(error)
    
try:
    os.mkdir(dirdocs)
except OSError as error:
    print(error)

try:
    os.mkdir(dircomp)
except OSError as error:
    print(error)

try:
    os.mkdir(dirsounds)
except OSError as error:
    print(error)

##file creation
##does file exists?  idk what would happend if it exists


##file organizer
for x in os.listdir():
    found=False
    
    print(f"analizing {x}")
    filename, file_extension = os.path.splitext(x)

    #print("checking if its a pic")
    if file_extension in pic:
        print(f"file is {x} a pic with extension {file_extension}\n")

        
        shutil.move(x,dirpic)
        print("moved to: /pics\n")
        next
        
    #print("checking if its a doc")
    elif file_extension in docs:
        shutil.move(x,dirdocs)
        print(f"file is {x} a doc with extension {file_extension}\n")
        print("moved to: /docs\n")
        next

    #print("checking if its a comp")
    elif file_extension in compressed:
        shutil.move(x,dircomp)
        print(f"file is {x} a comp with extension {file_extension}\n")
        print("moved to: /comp\n")
        next

    #print("checking if its a sound")
    elif file_extension in sounds:
        shutil.move(x,dirsounds)
        print(f"file is {x} a sound with extension {file_extension}\n")
        print("moved to: /sounds\n")
        next
        
    else:
        print(f"extension {file_extension} not listed\n")
        

print(f"finished scanning path: {os.getcwd()} ")

        
    




