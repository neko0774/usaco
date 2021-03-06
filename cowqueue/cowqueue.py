
import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")




N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]
cows.sort()
judge = 0
for i,j in cows:
    if judge>i:
        judge +=j
    else:
        judge = i+j 
print(judge)