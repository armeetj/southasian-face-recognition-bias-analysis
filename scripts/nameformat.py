# imports
import os
from tqdm import tqdm
from multipledispatch import dispatch
import random
import time

@dispatch(str, str, bool)
def rename_data(directory, prefix_format, verbose):
    index = 0
    if(verbose): 
        for filename in tqdm(os.listdir(str(directory))):
            os.rename((directory + filename), (directory + prefix_format + str(index) + ".png"))
            index += 1
            time.sleep(0.006)
    else: 
        for filename in (os.listdir(str(directory))):
            os.rename((directory + filename), (directory + prefix_format + str(index) + ".png"))
            index += 1

@dispatch(str, str)   
def rename_data(directory, prefix_format): 
    rename_data(directory, prefix_format, True)

def scramble_file_names(directory):
    i = 0
    for file in os.listdir(directory):
        os.rename(directory + file, directory + str(i) + ".png")
        i += 1

print("-- FORMATTING DATA (ETHNICITY: SIKH) --")
# scramble_file_names("./data/sikh/in/male/")
# rename_data("./data/sikh/in/male/", "male_in_")
# scramble_file_names("./data/sikh/in/female/")
# rename_data("./data/sikh/in/female/", "female_in_")
# scramble_file_names("./data/latino/in/male/")
# rename_data("./data/latino/in/male/", "male_in_")
scramble_file_names("./data2/tamil_nadu/in/male/")
rename_data("./data2/tamil_nadu/in/male/", "male_in_")
print("-- COMPLETE --")

