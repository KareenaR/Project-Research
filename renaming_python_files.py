import os
path = "C:/Users/XXXX/"

files = os.listdir(path)

for file in files:
    file_name, file_ext = os.path.splitext(file) #splits the name of file in the actual name and extension
    firstpart, secondpart = file_name[:len(file_name)//2], file_name[len(file_name)//2:] #divide the filename in two equal parts and assign it to different values
    print(firstpart)  #printing it out to see if it works
    print(secondpart)
    newname = (str(secondpart) + str(firstpart) + str(file_ext)) #assign a new name by reversing the order in which it was named
    print(newname) #printing it out to see if it works
    os.rename(os.path.join(path, file), os.path.join(path, newname)) #renaming the files 


#If there are some problems with assigning the extension in the previous code, we can assign an extension in a separate code block as well 


for file in files:
    file_name, fileext = os.path.splitext(file)
    print(file_name)
    src = os.path.join(path, file)
    dst = os.path.join(path, file + '.csv')
    os.rename(src, dst)
              
