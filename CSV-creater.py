import os.path 
import csv
path = './DENV1/'
#isdir = os.path.isdir(path) 
#subdirs = [x[0] for x in os.walk(path)]
##print(subdirs)
dir_list = os.listdir(path)
##print(dir_list)
isDirectory = os.path.isdir(path)
##print(isDirectory)
for each_dir in dir_list:
    #print(each_dir)
    b = os.path.isdir(path+each_dir)
    if b :
        print(each_dir)
        

#for file in os.listdir((each_dir)):
    #if file.endswith(".txt"):
        #print(os.path.join((each_dir), file))

import pathlib
for txt_file in pathlib.Path('(each_dir)').glob('**/*.txt'):
    if file.endswith(".txt"):
        print(os.path.join((each_dir), file))
            

    #with open('data1.csv', 'w', newline='') as file:
    #    writer = csv.writer(file)
    #    writer.writerow(["each_dir"])
        #open (each_dir)
        #open(log.txt)
        #print(log.txt)
    






    ## https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/ ##