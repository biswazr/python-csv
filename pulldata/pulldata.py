import os
import pandas as pd
import shutil
path='Final2.xlsx'
path_d="Output"
os.makedirs(path_d,exist_ok = True)
inputfile = pd.read_excel(path)
values=inputfile.iloc[:,0]
print(values)
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
for value in values:
    shutil.copy2("Ligands_S/"+value+".pdbqt",path_d)