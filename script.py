import math
import sys

#sys.stdin = open("inputs/b_should_be_easy.in", 'r')

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

#rides.sort(key=finish)

for i in range(F):

    if not rides:
        vehicles.append([])
        continue

    pos = [0, 0]
    lastest = 0

    res = []

    while lastest < T:
        possible = [r for r in rides if lastest + dist(pos[0], pos[1], r['a'], r['b']) < r['s'] and 3 * dist(pos[0], pos[1], r['a'], r['b']) < r['s'] - lastest]
        if not possible:
            possible = [r for r in rides if lastest + dist(pos[0], pos[1], r['a'], r['b']) < r['s']]
        if not possible:
            break

        r = min(possible, key=lambda r: dist(pos[0], pos[1], r['a'], r['b']))

        lastest = r['f']
        pos_end = [r['x'], r['y']]
        res.append(r['i'])
        rides.remove(r)

    vehicles.append(res)

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
        for r2 in rides:
            if lastest + dist(pos_end[0], pos_end[1], r2['a'], r2['b']) < r2['s']:
                vehicles[i].append(r2['i'])
                lastest = r2['f']
                pos_end = [r2['x'], r2['y']]
                rides.remove(r2)
                find = True
                break
        if not find:
            break"""

for v in vehicles: print(str(len(v)) + " " + " ".join(map(str, v)))
