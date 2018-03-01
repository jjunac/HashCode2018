import math
import sys

#sys.stdin = open("inputs/d_metropolis.in", 'r')

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

vehicles = []

# Put code here

rides.sort(key=start)

find = False

def no_bonus():
    global r2, lastest, pos_end, find
    for r2 in rides:
        if lastest + dist(pos_end[0], pos_end[1], r2['a'], r2['b']) + dist(r2['a'], r2['b'], r2['x'], r2['y']) < r2[
            'f']:
            vehicles[i].append(r2['i'])
            lastest = r2['f']
            pos_end = [r2['x'], r2['y']]
            rides.remove(r2)
            find = True
            break


def bonus():
    global r2, lastest, pos_end, find
    for r2 in rides:
        if lastest + dist(pos_end[0], pos_end[1], r2['a'], r2['b']) < r2['s']:
            vehicles[i].append(r2['i'])
            lastest = r2['f']
            pos_end = [r2['x'], r2['y']]
            rides.remove(r2)
            find = True
            break


for i in range(F):
    if not rides:
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
            break


for v in vehicles: print(str(len(v)) + " " + " ".join(map(str, v)))
