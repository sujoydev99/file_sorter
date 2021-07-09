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
     os.makedirs(destinationRoot+"/Frame_"+str(i+1)+"/Input/normal")
     os.makedirs(destinationRoot+"/Frame_"+str(i+1)+"/Input/projection")
     os.makedirs(destinationRoot+"/Frame_"+str(i+1)+"/Project")
     os.makedirs(destinationRoot+"/Frame_"+str(i+1)+"/Result")
     os.makedirs(destinationRoot+"/Frame_"+str(i+1)+"/Temp")
    #  image loop
     for j in range (0, increment):
         print(arr[j*counter+i])
         shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Frame_"+str(i+1)+"/Input/normal/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
         shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Frame_"+str(i+1)+"/Input/projection/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
        #  shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Frame_"+str(i+1)+"/Project/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
        #  shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Frame_"+str(i+1)+"/Result/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
        #  shutil.copy(sourceRoot+"/"+arr[j*counter+i], destinationRoot+"/Frame_"+str(i+1)+"/Temp/"+(str(j+1).zfill(prefixLength))+"."+arr[j*counter+i].split(".")[1])
         