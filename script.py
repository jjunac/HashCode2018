import math
import sys

#sys.stdin = open("inputs/a_example.in", 'r')

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

rides.sort(key=lambda r: dist_ride(r))

i = 0
for i in range(F):
    r = rides[i]
    vehicles.append("1 " + str(r['i']))

for v in vehicles: print(v)
