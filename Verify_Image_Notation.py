import os
import glob
directory='C:\\Users\\general\\Desktop\\prithvi_scp\\22Apr2020\\img'
os.chdir(directory)
files=glob.glob('*.txt')
for x in files:
    print(x)
    f = open(x, 'r')
    x = f.read()
    print(x)
