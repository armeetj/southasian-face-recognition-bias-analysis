import pandas

def run(directory):
    df = pandas.read_csv(directory + "out.csv")

run("./data/sikh/out/male/")