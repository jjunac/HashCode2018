(R, C, F, N, B, T) = tuple(map(int, input().split()))
rides = []

for l in [input() for _ in range(N)]:
    a = l.split()
    rides.append({'a': a[0], 'b': a[1], 'x': a[2], 'y': a[3], 's': a[4], 'f': a[5]})

