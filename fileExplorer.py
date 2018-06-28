import os

os.walk()

for folderName, subfolders, filenames in os.walk('D:\\python'):
        print('The folder is ' + folderName)
        print('The subfolder is ' + folderName + 'are: ' + str(subfolders))
        print('The filenames is ' + folderName + 'are: ' + str(filenames))
        print()
