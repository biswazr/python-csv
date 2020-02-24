import os.path
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
    #print(b)