import math
import sys

sys.stdin = open("inputs/b_should_be_easy.in", 'r')


def dist(a, b, x, y):
    return abs(a - x) + abs(b - y)


def dist_ride(r):
    return dist(r['a'], r['b'], r['x'], r['y'])


def finish(r):
    return r['f']


def start(r):
    return r['s']


def p(j):
    rj = rides[j]
    m = j - 1
    for k in reversed(rides[:j]):
        if m not in toIgnore:
            if (k['f'] + dist(k['x'], k['y'], rj['a'], rj['b'])) < rj['f'] - dist_ride(rj):
                break
        m -= 1
    if m == 0:
        P[j] = 0
        return

    P[j] = m


def bondOpt():
    M[0] = -1
    for j in range(1, len(rides)):
        M[j] = max(dist_ride(rides[j]) + M[P[j]], M[j - 1])


def find_solution(j, tab):
    if j == -1:
        return tab
    elif dist_ride(rides[j]) + M[P[j]] > M[j - 1]:
        tab.append(j)
        return find_solution(P[j], tab)
    else:
        return find_solution(j - 1, tab)


(R, C, F, N, B, T) = tuple(map(int, input().split()))
rides = []

i = 0
for l in [input() for _ in range(N)]:
    a = list(map(int, l.split()))
    rides.append({'a': a[0], 'b': a[1], 'x': a[2], 'y': a[3], 's': a[4], 'f': a[5], 'i': i})
    i += 1

vehicles = []
M = [0] * len(rides)
P = [0] * len(rides)
# Put code here

toIgnore = []
rides.sort(key=lambda r: r['f'])
for i in range(len(rides)):
    p(i)

for j in reversed(range(len(rides))):
    if j not in toIgnore:
        bondOpt()
        tabLol = find_solution(j, [])
        vehicles.append(str(len(tabLol)) + " " + " ".join(list(map(str, tabLol))))
        toIgnore.extend(tabLol)

for v in vehicles:
    print(v)
