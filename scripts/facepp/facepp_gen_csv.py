import csv
import pandas
import os
from tqdm import tqdm
import json
import time

def run(directory):
    df = pandas.DataFrame(
        columns=["id", "predicted_ethnicity", "predicted_emotion", "predicted_gender", "male_beauty_score",
                 "female_beauty_score"])
    counter = 0;
    for filepath in tqdm(os.listdir(directory + "json")):
        output_file = directory + "out.csv"
        in_filepath = directory + "json/" + filepath


        json_file = open(in_filepath, "r")
        try:
            json_file = json.loads(json_file.read())
            json_file = json_file["faces"][0]["attributes"]
            predicted_emotion_list = (json_file["emotion"])
            predicted_emotion = ["", -9999]
            for i in predicted_emotion_list:
                if(predicted_emotion_list[i] > predicted_emotion[1]):
                    predicted_emotion[0] = i
                    predicted_emotion[1] = predicted_emotion_list[i]
            df = df.append([
                {
                "id": counter,
                    "predicted_ethnicity": (json_file["ethnicity"]["value"]) if (len(json_file["ethnicity"]["value"]) > 0) else "N/A",
                    "predicted_emotion": str(predicted_emotion[0]),
                    "predicted_gender": json_file["gender"]["value"],
                    "male_beauty_score": json_file["beauty"]["male_score"],
                    "female_beauty_score": json_file["beauty"]["female_score"]}])
        except Exception:
            print(in_filepath)
        counter += 1
    df.to_csv(output_file)

run("./data2/facepp/north_punjab/out/male/")
run("./data2/facepp/north_punjab/out/female/")