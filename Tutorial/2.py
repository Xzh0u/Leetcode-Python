import sys
n, m = sys.stdin.readline().split()
net = []
search = []
idx = []
for i in range(int(n)):
    tmp = sys.stdin.readline().strip('\n').split()
    idx.append(tmp[0])
    net.append(tmp[1])

for i in range(int(m)):
    search.append(sys.stdin.readline().strip('\n'))

for element in search:
    a = search.split('.')