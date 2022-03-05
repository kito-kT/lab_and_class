import os as os
import random
import shutil, os

#python read in files from current working directory and store as an array

files = os.listdir() #store file names as an object 

numberOf_files = int(input('How many random files would you like to select? ')) # user picks number of random files to select

random_file = random.sample(files,numberOf_files) #select random files without replacement
print(len(random_file)," items stored... ") #confirm number of selected files is correct

dir_name = input("Name output directory... ") # user create and name  output directory 
os.mkdir(dir_name) #creates directory

for f in random_file:           # read each file in random_file list and copy to newly made directory
    shutil.copy(f, dir_name)