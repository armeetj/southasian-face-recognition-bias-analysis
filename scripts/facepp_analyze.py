import os
import json
from tqdm import tqdm
import cv2
import requests 
import json 
import base64

api_key = ""
api_secret = ""
def run(directory, prefix):
    req_url = "https://api-us.faceplusplus.com/facepp/v3/detect"

    for filepath in tqdm(os.listdir(directory)):
        filepath = directory + filepath
        print("\nFile: " + str(filepath))
        # read file
        file = open(filepath, "r")
        file.read()

        # prepare POST req
        r_data = {}
        r_data["api_key"] = api_key
        r_data["api_secret"] = api_secret
        r_data["iamge_file"] = file
        r_data["return_landmark"] = 2
        r_data["return_attributes"] = "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus"

        r = requests.post()
        file.close()
    

print("-- AUTHENTICATION --")
api_key = input("Enter API Key: ")
api_secret = input("Enter API Secret: ")
print("-- AUTHENTICATION COMPLETE --\n\n")
print("-- RUNNING DATA (ETHNICITY: SIKH) --")
run("./data/sikh/in/male", "")
print("\n\n-- COMPLETE --")