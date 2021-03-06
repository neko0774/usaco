
import sys
sys.stdin = open("berries.in", "r")
sys.stdout = open("berries.out", "w")
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
B = [int(i) for i in input().split()]
#K<=10 全探索
#一定条件下で　バスケットの中身を可能な限り等しくする
#条件　取得ベリーの数の最大化
#最小値と最大値の差を小さくする　×

B.sort(reverse=True)

#N>=K
