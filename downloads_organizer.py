# Andrew Erasmus
# Python automation to organize my files from my downloads into specified categories
# 2024/02/17

from os import listdir
from os.path import isfile, join

import os
import shutil

#path name of folder to be organized - in this case - downloads
file_path='C:/Users/User/Downloads'

files = [f for f in listdir(file_path) if isfile(join(file_path, f))] #get all the files in the list 

file_list=[] #list of all the file types
filetype_dict={} #dictionary for the filetypes for the folder names


for file in files:
    point_pos = file.rfind('.') # gets the last '.' in the string
    filetype=file[point_pos+1:] #gets only the extension of the filename 
    if filetype not in file_list:

        file_list.append(filetype) #add type to the list
        new_folder = file_path+'/'+filetype + '_folder' #create folder in downloads for this filetype
        filetype_dict[str(filetype)] = str(new_folder)

        #check if folder exists, if not then create a new one
        if os.path.isdir(new_folder) == True:
            continue
        else:
            os.mkdir(new_folder)

count = 1
for file in files:
    src_path=file_path+'/'+file
    point_pos = file.rfind('.') # gets the last '.' in the string
    filetype=file[point_pos+1:] #gets only the extension of the filename 
    if filetype in filetype_dict.keys(): #search for the filetype in the dictionary
        dest_path=filetype_dict[str(filetype)] #add to dictionary if not there already 
        shutil.move(src_path,dest_path) #moves file from src to dest
        
    print(count,'. File moved: ', src_path + ' >>> ' + dest_path)
    count+=1

