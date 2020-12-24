# @ArmeetJatyani
# December 2020

# imports
import os
import json
from tqdm import tqdm

# draw bounding rectangles and dots
def run(directory):
    for filepath in tqdm(os.listdir(directory)):
        in_filepath = directory + filepath
        out_filepath = directory.replace("in", "out") + "png/"  + (filepath.replace("in", "out"))
