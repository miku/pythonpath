import fileinput

L, R = [], []
for line in fileinput.input():
    a, b = line.strip().split()
    L.append(int(a))
    R.append(int(b))

L = sorted(L)
R = sorted(R)

print(sum(abs(a - b) for a, b in zip(L, R)))
