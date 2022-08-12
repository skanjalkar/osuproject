from tkinter import font
import matplotlib.pyplot as plt
import csv
import numpy as np

class Player():
    def __init__(self) -> None:
        self.username = ""
        self.rank = 0
        self.total_pp = 0.0
        self.scores = [] # list of scores

class Score():
    def __init__(self) -> None:
        self.map_name = ""
        self.map_id = 0
        self.map_url = ""
        self.mods = ""
        self.pp = 0.0
        self.grade = ""
        self.accuracy = 0.0

def parse(file_name):
    user_info = []
    file = open(file_name)
    csv_reader = csv.reader(file)
    row = next(csv_reader)
    row = next(csv_reader)
    row = next(csv_reader)
    while row is not None:
        # Parse player info
        p = Player()
        p.rank, p.username, p.total_pp = int(row[0]), row[1], float(row[2])
        row = next(csv_reader)
        row = next(csv_reader)
        while row is not None and len(row) != 3:
            s = Score()
            s.map_name = row[0]
            s.map_id = int(row[1])
            s.map_url = row[2]
            s.mods = row[3]
            s.pp = float(row[4])
            s.grade = row[5][6]
            s.accuracy = round(float(row[6]),2)
            p.scores.append(s)
            try:            
                row = next(csv_reader)
                row = next(csv_reader)
            except StopIteration:
                row = None                
        user_info.append(p)
    return user_info

data = parse("osudata.csv")

# function which returns a dict.

#############################

def frequency(data):
    map_freq = {}
    for users in data:
        for score in users.scores:
            if (score.map_name, score.map_id) not in map_freq:
                map_freq[(score.map_name, score.map_id)] = 1
            else:
                map_freq[(score.map_name, score.map_id)] += 1
        
    return map_freq

map_freq = frequency(data)
map_freq = dict(sorted(map_freq.items(), key=lambda item: item[1], reverse=True))

def map_mod_scores(map_id, data):
    mod_score = {}
    for users in data:
        for score in users.scores:
            if score.map_id == map_id:
                if score.mods not in mod_score:
                    mod_score[score.mods] = [(score.pp, score.accuracy)]
                else:
                    mod_score[score.mods].append((score.pp, score.accuracy))
    return mod_score


def plot_graph(map_freq, data):
    for mapname, mapid in map_freq:
        mapscores = map_mod_scores(mapid, data)
        legends = []
        for key in mapscores:
            tx = []
            ty = []
            for i, j in mapscores[key]:
                tx.append(i)
                ty.append(j)
            plt.scatter(tx, ty, color=np.random.rand(3,))
            legends.append(key)
        # plt.figure(count)
        plt.title(mapname + f'({mapid})' + " || Frequency: " + str(map_freq[(mapname, mapid)]))
        plt.legend(legends, loc="lower right", prop={'size': 6})
        plt.xlabel("PP")
        plt.ylabel("Accuracy")
        plt.show()

plot_graph(map_freq, data)

