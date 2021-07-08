import os
import sys
import shutil


# cli args
sourceRoot=sys.argv[1]
destinationRoot = sys.argv[2]
batchSize = sys.argv[3]

# cleanup
shutil.rmtree(destinationRoot, ignore_errors=True)
os.mkdir(destinationRoot)

# mutation vars
increment = int(batchSize)
arr=os.listdir(sourceRoot)
arr=sorted(arr)
counter = int(len(arr)/int(increment))
fileCounter = 0

# folder loop
for i in range(1,counter+1):
     print("processing folder no. " + str(i))
     os.makedirs(destinationRoot+"/Folder_"+str(i)+"/input/normal")
     os.makedirs(destinationRoot+"/Folder_"+str(i)+"/input/projection")
    #  image loop
     for j in range (0, increment):
         shutil.copy(sourceRoot+"/"+arr[fileCounter], destinationRoot+"/Folder_"+str(i)+"/input/normal/"+arr[fileCounter])
         shutil.copy(sourceRoot+"/"+arr[fileCounter], destinationRoot+"/Folder_"+str(i)+"/input/projection/"+arr[fileCounter])
         fileCounter += 1 
         