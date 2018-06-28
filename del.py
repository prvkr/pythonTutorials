import os

os.chdir('D:\\python\\New folder')

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        os.unlink(filename)
        
