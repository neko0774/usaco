import sys
from bisect import bisect_left, bisect_right
sys.stdin = open("haybales.in", "r")
sys.stdout = open("haybales.out", "w")
input = sys.stdin.buffer.readline

def query(a,b):
    return bisect_right(A, b)-bisect_left(A, a)

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
A.sort()

for _ in range(Q):
    a, b = map(int, input().split())
    print(query(a,b))