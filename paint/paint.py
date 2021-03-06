import sys
sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")
'''
#なんで動かんの？
def main(a,b,c,d):
    #a<b
    #c<d
    ans = d-c+b-a
    if a<=c<=b: return d-a
    elif c<=a<=d: return b-c
    elif a<c and d<b: return b-a
    elif c<a and b<d: return d-c
    return ans
a, b = map(int, input().split())
c, d = map(int, input().split())
print(main(a,b,c,d))
'''
#この方法はしたくない
#imos
a,b = map(int, input().split())
c,d = map(int, input().split())
fence = [0]*102
fence[a] += 1
fence[b] += 1
fence[c] -= 1
fence[d] -= 1
for i in range(1,102):
    fence[i] += fence[i-1]
print(fenec[-1])