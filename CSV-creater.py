import os.path
path = './DENV1/'
#isdir = os.path.isdir(path) 
#subdirs = [x[0] for x in os.walk(path)]
##print(subdirs)
dir_list = os.listdir(path)
##print(dir_list)
isDirectory = os.path.isdir(path)
##print(isDirectory)
f = open("temp_output.txt", "w")
for each_dir in dir_list:
    #print(each_dir)
    b = os.path.isdir(path+each_dir)
    if b :
        print(each_dir)
        ## append all new variable to below array 
        eachline_array=[]*
        ## appending first coloumn
        eachline_array.append(each_dir)




        #write to file at each loop end 
        f = open("temp_output.csv", "a")
        for each_coloumn in eachline_array:
            f.write("%s ," % each_coloumn)
        f.write("\n")
        f.close()
    #print(b)