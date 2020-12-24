# @ArmeetJatyani
# December 2020

# imports
import os
import json
from tqdm import tqdm
import cv2
import requests 
import json 
import base64
import matplotlib.pyplot as plt 
import matplotlib.image as img
import time

# authentication
print("-- AUTHENTICATION --")
try:
    api_key = os.environ["FACEPP_KEY"]
    api_secret = os.environ["FACEPP_SECRET"]
    print("\nfound env variables")
except Exception:
    api_key = input("Enter API Key: ")
    api_secret = input("Enter API Secret: ")

print("-- AUTHENTICATION COMPLETE --\n\n")

def run_for_one(filepath, pretty_json):
    req_url = "https://api-us.faceplusplus.com/facepp/v3/detect"
    in_file = open(filepath, "rb")

    # prepare r_data
    r_data = {}
    r_data["api_key"] = api_key
    r_data["api_secret"] = api_secret
    r_data["return_landmark"] = 2
    r_data[
        "return_attributes"] = "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus"

    # prepare r_file
    r_file = dict(image_file = in_file.read())

    # make POST req
    r = requests.post(req_url, data=r_data, files = r_file)

    if(pretty_json):
        return (json.dumps(r.json(), indent = 4))
    else:
        return (json.dumps(r.json()))
    # close all files
    in_file.close()

def run(directory, pretty_json):
    req_url = "https://api-us.faceplusplus.com/facepp/v3/detect"

    for filepath in tqdm(os.listdir(directory)):
        in_filepath = directory + filepath
        out_filepath = directory.replace("in", "out") + "json/"  + (filepath.replace("in", "out").replace(".png", ".json"))

        # print(in_filepath)
        # print(out_filepath)

        # open in/out files
        in_file = open(in_filepath, "rb")
        out_file = open(out_filepath, "w")

        # prepare r_data 
        r_data = {}
        r_data["api_key"] = api_key
        r_data["api_secret"] = api_secret
        r_data["return_landmark"] = 2
        r_data["return_attributes"] = "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus"
        
        # prepare r_file
        r_file = dict(image_file = in_file.read())
        
        # make POST req
        r = requests.post(req_url, data=r_data, files = r_file)

        if(pretty_json):
            out_file.write(json.dumps(r.json(), indent = 4))
        else: 
            out_file.write(json.dumps(r.json()))
        # close all files
        in_file.close()
        out_file.close()
    

# print("-- RUNNING DATA (ETHNICITY: SIKH) --")
# print("-- GENDER: MALE -- ")
# run("./data/sikh/in/male/", True)
# print("-- GENDER: FEMALE -- ")
# run("./data/sikh/in/female/", True)
# print("\n\n-- COMPLETE --")

print(run_for_one("./data/img.png", True))