# @ArmeetJatyani
# December 2020

# imports
import os
import json
from tqdm import tqdm
import cv2
import matplotlib.pyplot as plt

# draw bounding rectangles and dots
def run(directory):
    for filepath in tqdm(os.listdir(directory)):
        json_filepath = (directory.replace("in", "out") + "json/"  + (filepath.replace("in", "out"))).replace(".png", ".json")
        in_filepath = directory + filepath
        out_filepath = directory.replace("in", "out") + "png/"  + (filepath.replace("in", "out"))

        json_file = (open(json_filepath, "r"))
        img = cv2.imread(in_filepath)
        img_data = json.loads(json_file.read())
        json_file.close()

        try:
            face_num = img_data["face_num"]
        except Exception:
            print(json_filepath)
            continue
        if face_num == 1:
            top_x = img_data["faces"][0]["face_rectangle"]["left"]
            top_y = img_data["faces"][0]["face_rectangle"]["top"]
            bottom_x = top_x + img_data["faces"][0]["face_rectangle"]["width"]
            bottom_y = top_y + img_data["faces"][0]["face_rectangle"]["height"]
            img = cv2.rectangle(img, pt1=(top_x, top_y), pt2=(bottom_x, bottom_y), color=(255, 0, 255), thickness=2)
        cv2.imwrite(out_filepath, img)

run("./data/sikh/in/male/")