import os.path
import openpyxl as xl
import pandas as pd
path = './DENV1/'
path1 = 'temp_output.csv'
path2 = 'Output_Template.xlsx'
dir_list = os.listdir(path)
f = open("temp_output.csv", "w")
f.close()
for each_dir in dir_list:
    #print(each_dir)
    b = os.path.isdir(path+each_dir)
    if b :
        ##print(each_dir)
        ## append all new variable to below array
        extractarray=[]
        extractarray.append(each_dir)
        count=0
        for line in open(path+each_dir+"/log.txt"):
            count += 1
            print("%d %s ," %(count, line) )
            if count>=27 and count<=36:
                WORDArray=line.split()
                WORDArray=WORDArray[1:]
                for word in WORDArray:
                    extractarray.append(word)
        print(extractarray)
        f = open("temp_output.csv", "a")
        for each_coloumn in extractarray:
            f.write("%s ," % each_coloumn)
        f.write("\n")
        f.close()
templatefile = pd.read_excel(path2,index=False)
csvfile = pd.read_csv(path1,header=None,skiprows=1)
writer = pd.ExcelWriter("Final_OutPut.xlsx",engine='xlsxwriter')
workbook=writer.book
#writer.sheets[0] = csvfile
merge_format_firstcell = workbook.add_format({'align': 'center',
                                   'valign': 'vcenter',
                                   'border': 1})
merge_format1 = workbook.add_format({'align': 'center',
                                   'valign': 'vcenter',
                                   'border': 1,
                                   'bg_color': '#5B9BD5'})
merge_format2 = workbook.add_format({'align': 'center',
                                   'valign': 'vcenter',
                                   'border': 1,
                                   'bg_color': '#70AD47'})
merge_format3 = workbook.add_format({'align': 'center',
                                   'valign': 'vcenter',
                                   'border': 1,
                                   'bg_color': '#FFC000'})
merge_format4 = workbook.add_format({'align': 'center',
                                   'valign': 'vcenter',
                                   'border': 1,
                                   'bg_color': '#ED7D31'})
merge_format=[merge_format1,merge_format2,merge_format3,merge_format4]

templatefile.to_excel(writer, sheet_name='Sheet1',startrow=0 ,index=False )
csvfile.to_excel(writer,startrow=2,sheet_name='Sheet1', startcol=0 ,index=False ,header=None)
worksheet = writer.sheets['Sheet1']
j=0
i=0
x=0
worksheet.merge_range(0,0,1,0,'Ligand', merge_format_firstcell )
while i < 28:
    worksheet.merge_range(0,i+1,0,i+3, 'Mode'+str(j+1), merge_format[x])
    
    worksheet.conditional_format(1,i+1,1,i+3, {'type': 'no_errors','format': merge_format[x]})   
    i=i+3
    j=j+1
    x=x+1
    if x==4:
        x=0
writer.save()