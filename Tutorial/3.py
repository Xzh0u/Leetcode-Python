import sys
t = int(sys.stdin.readline())
ans = 0
lines = []
for i in range(t):
    lines.append(sys.stdin.readline().strip('\n'))
for line in lines:
    if int(line) % 3 == 1:
        ans = ans + 1
print(ans)