import matplotlib.pyplot as plt
import csv
file = open("osudata.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
user_info = []

class osuInfo():
    def __init__(self, rank, username, pp):
        self.rank = rank
        self.username = username
        self.pp = pp
        self.map = {}
        self.info = {}


for row in csvreader:
    if not row:
        continue
    if len(row)<=3:
        osuobj = osuInfo(row[0], row[1], row[2])
        user_info.append(osuobj)
    if len(row)>3:
        for g in range(len(row[5])):
            if row[5][g] == ".":
                grade = row[5][g+1]
                break

        user_info[-1].info[(row[0], row[3])]=[float(row[4]), grade, row[6]]

file.seek(0)        
header = []
header = next(csvreader)

def frequency():
    map_freq = {}
    for row in csvreader:
        if not row:
            continue
        if len(row)>3:
            if (row[0], row[3]) not in map_freq:
                map_freq[(row[0], row[3])] = 1
            else:
                map_freq[(row[0], row[3])] += 1
    return map_freq

def map_info(map, user_info):
    x = []
    y = []
    z = []
    for user in user_info:
        if map in user.info:
            x.append(user.info[map][0])
            y.append(round(float(user.info[map][2]),2))
            z.append(user.info[map][1])
    return x, y, z


map_freq = frequency()
map_freq = dict(sorted(map_freq.items(), key=lambda item: item[1], reverse=True))
# print(map_freq)

for map in map_freq:
    x, y, z = map_info(map, user_info)
    # print(y)
    plt.title(map)
    plt.scatter(x, y)
    plt.xlabel("PP")
    plt.ylabel("Accuracy")
    plt.show()


