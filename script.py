import math
import sys

#sys.stdin = open("inputs/e_high_bonus.in", 'r')

def dist(a, b, x, y):
    return math.fabs(a-x) + math.fabs(b-y)

def dist_ride(r):
    return dist(r['a'], r['b'], r['x'], r['y'])

def finish(r):
    return r['f']

def start(r):
    return r['s']

(R, C, F, N, B, T) = tuple(map(int, input().split()))
rides = []

i = 0
for l in [input() for _ in range(N)]:
    a = list(map(int, l.split()))
    rides.append({'a': a[0], 'b': a[1], 'x': a[2], 'y': a[3], 's': a[4], 'f': a[5], 'i': i})
    i += 1

vehicles = [{"rides": [], "lastest": 0, "pos": [0, 0]} for _ in range(F)]

# Put code here

rides.sort(key=lambda r: start(r) + dist(0,0, r['a'], r['b']))

find = False

for r in rides:
    possible = []
    if B == 1000:
        possible = [v for v in vehicles if v["lastest"] + dist(r["a"], r["b"], v["pos"][0], v["pos"][1]) <= r["s"]]
        if not possible:
            possible = [v for v in vehicles if
                        v["lastest"] + dist(r["a"], r["b"], v["pos"][0], v["pos"][1]) + dist_ride(r) <= r["f"]]

    else:
        possible = [v for v in vehicles if v["lastest"] + dist(r["a"], r["b"], v["pos"][0], v["pos"][1]) + dist_ride(r) <= r["f"]]

    if not possible:
        continue
    v = min(possible, key=lambda v: v["lastest"])
    v["rides"].append(r["i"])
    v["lastest"] = r["f"]
    v["pos"] = [r["x"], r["y"]]




for v in vehicles: print(str(len(v["rides"])) + " " + " ".join(map(str, v["rides"])))

"""if not rides:
    vehicles.append([])
    continue
r = rides.pop(0)
vehicles.append([r['i']])

pos_start = [r['a'], r['b']]
pos_end = [r['x'], r['y']]
lastest = r['f']
earliest = r['s']
while lastest < T:
    find = False
    if B == 1000:
        bonus()
        if not find:
            no_bonus()
    else:
        no_bonus()
    if not find:
        break"""


#for v in vehicles: print(str(len(v)) + " " + " ".join(map(str, v)))
