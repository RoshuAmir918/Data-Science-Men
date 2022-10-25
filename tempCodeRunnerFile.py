df = pandas.read_csv(os.path.abspath(os.getcwd()) + "/Data-Science-Men/atlantic_refined.csv")
for x in df["Event"]:
    print(x)