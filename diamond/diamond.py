import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
D = [0]*N
for i in range(N):
    D[i] = int(input())
D.sort(reverse=True)
ans = 0
#print(D)
for i in range(N):
    cnt = 1
    for j in range(i+1, N):#should use more efficient search
        if D[i]-D[j] > K:#N <= 10**3
            break
        cnt += 1
    ans = max(ans, cnt)
print(ans)#(N^2+NlogN)