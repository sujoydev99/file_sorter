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

prefixLength = 0
temp = len(arr)
while (temp > 0):
  temp = temp//10
  prefixLength = prefixLength + 1
if(prefixLength<4):
    prefixLength = 4

# folder loop
for i in range(0,counter):
     print("processing folder no. " + str(i+1))
     os.makedirs(destinationRoot+"/Folder_"+str(i+1)+"/input/normal")
     os.makedirs(destinationRoot+"/Folder_"+str(i+1)+"/input/projection")
    #  image loop
     for j in range (0, increment):
         print(arr[j*counter+i])
         shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Folder_"+str(i+1)+"/input/normal/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
         shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Folder_"+str(i+1)+"/input/projection/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
         