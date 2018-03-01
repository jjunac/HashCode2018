import math
import sys

# sys.stdin = open("inputs/a_example.in", 'r')

def dist(a, b, x, y):
    return math.fabs(a-x) + math.fabs(b-y)

def dist_ride(r):
    return dist(r['a'], r['b'], r['x'], r['y'])

(R, C, F, N, B, T) = tuple(map(int, input().split()))
rides = []

i = 0
for l in [input() for _ in range(N)]:
    a = list(map(int, l.split()))
    rides.append({'a': a[0], 'b': a[1], 'x': a[2], 'y': a[3], 's': a[4], 'f': a[5], 'i': i})
    i += 1

vehicles = []

# Put code here

rides.sort(key=lambda r: dist_ride(r))

for i in range(F):
    if not rides:
        break
    r = rides.pop(0)
    vehicles.append([r['i']])

    pos = [r['x'], r['y']]
    lastest = r['f']
    while lastest < T:
        find = False
        for r2 in rides:
            if lastest + dist(pos[0], pos[1], r2['a'], r2['b']) < r2['s']:
                vehicles[i].append(r2['i'])
                lastest = r2['f']
                pos = [r2['x'], r2['y']]
                rides.remove(r2)
                find = True
                break
        if not find:
            break

for v in vehicles: print(str(len(v)) + " " + " ".join(map(str, v)))
