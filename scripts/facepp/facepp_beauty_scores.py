import pandas

def run(directory):
    df = pandas.read_csv(directory + "out.csv")
    return [(sum(df["male_beauty_score"]) / len(df["male_beauty_score"])), (sum(df["female_beauty_score"]) / len(df["female_beauty_score"]))]

print("Format:  (male beauty score, female beauty score)")
print("Sikh Males")
print(run("./data/sikh/out/male/"))
print("Sikh Females")
print(run("./data/sikh/out/female/"))

print("White Males")
print(run("./data/white/out/male/"))
print("White Females")
print(run("./data/white/out/female/"))

print("Latino Males")
print(run("./data/latino/out/male/"))
print("Latino Females")
print(run("./data/latino/out/female/"))