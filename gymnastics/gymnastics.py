import sys
sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

k, n= map(int, input().split())
ans = 0
rank = [0]*k
for i in range(k):
    rank[i] = [int(j) for j in input().split()]


def check(x,y):
    global rank
    global k
    cnt = 0
    for z in rank:
        if z.index(x) > z.index(y):
            cnt += 1
    if cnt == 0 or cnt == k:
        return 1
    return 0

for i in range(n):
    for j in range(i+1,n):
        ans += check(i+1,j+1)
print(ans)
