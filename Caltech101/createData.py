import os
from os import walk
import shutil
print '\n'*100
f = []
d = []
newDataLoc = '/media/shreez/Data/Data/New_101_ObjectCategories'
dataLoc = '/media/shreez/Data/Data/101_ObjectCategories'
folderNames = ['test', 'train', 'val', 'allData', 'temp']

def flip(p, q):
# p < q and p + q < 1
    import random
    if random.random() < p:
        num = 1
    elif random.random() < q and random.random() >= p:
        num = 2
    else:
        num = 3

    return num

def move_files(src, dst):
    import shutil
    shutil.move(src, dst)


# create directories if they don't exist
for fol_name in folderNames:
	f_path = newDataLoc + '/' + fol_name
	if not os.path.exists(f_path):
		os.makedirs(f_path)

folderNames = ['test', 'train', 'val']
# delete files if they exist in the directories
for fol_name in folderNames:
	f_path = newDataLoc + '/' + fol_name
	for i_file in os.listdir(f_path):
		del_file = os.path.join(f_path, i_file)
		print "del_file = %s" %del_file
		try:
			if os.path.isfile(del_file):
				os.unlink(del_file)
				print "!!HERE!!"
			# elif os.path.isdir(del_file): shutil.rmtree(del_file)
		except Exception, e:
			print e

# get all directory names
for (dirpath, dirnames, filenames) in walk(dataLoc):
    allDirs = dirnames
    break # the walk function reads one node at a time - 
          # all dir names are at the top node - 
          # after that it walks into each directory 

# move files to 'allData' loc and rename files by appending the category name
dst = '/media/shreez/Data/Data/New_101_ObjectCategories' + '/' + 'allData'
temp_dst = newDataLoc + '/' + 'temp'
for dir in allDirs:
    src = dataLoc + '/' + dir
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy2(full_file_name, temp_dst)

    [os.rename(temp_dst + '/' + f, temp_dst + '/' + dir + '_' + f) for f in os.listdir(temp_dst)]

    val_data_percent    = 0.2
    train_data_percent = 0.7
    train_dir = newDataLoc + '/' + 'train'
    val_dir = newDataLoc + '/' + 'val'
    test_dir = newDataLoc + '/' + 'test'
    for file_name in os.listdir(temp_dst):
        full_file_name = os.path.join(temp_dst, file_name)
        num = flip(val_data_percent, train_data_percent)
        if num == 1:
            move_files(full_file_name, val_dir)
        elif num == 2:
            move_files(full_file_name, train_dir)
        else:
            move_files(full_file_name, test_dir)

#%%
def addFileName(f,k, file_path, flag_file_open):

    wf = open(file_path, 'a+')
    ss = f + ' ' + ' %d \n' %k
    wf.write(ss)
    

def makeDataList(src, categories, file_path):
    import os
    import re
    import numpy as np
    file_names = os.listdir(src)
    nCategories = len(categories)
    numeric_key = 0
    flag_file_open = False
    for idx in np.arange(nCategories):
        key = categories[idx]
        for file in file_names:
            if re.match(key, file):
                addFileName(file, numeric_key, file_path, flag_file_open)
                flag_file_open = True
        numeric_key  = numeric_key + 1

src_test = '/media/shreez/Data/Data/New_101_ObjectCategories/val'
src_categories = allDirs
file_path = '/media/shreez/Data/Data/New_101_ObjectCategories/val/val.txt'
makeDataList(src_test, src_categories, file_path)
