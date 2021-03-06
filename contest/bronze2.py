#N <= 10**5
#O(N^2) == false

#付近の場所だけ確認する
#ans +- 5

def judge(x,y,table):
    cel = [[0,1], [1,0], [-1, 0], [0, -1]]
    cnt = 0
    for i in cel:
        pos_x = x+i[0]
        pos_y = y+i[1]
        if pos_x >= 0 and pos_y>=0:
            cnt += table[pos_x][pos_y]
    return 1 if cnt==3 else 0

def main(N):    
    cel = [[0, 0],[0,1], [1,0], [-1,0], [0,-1]]
    table = [[0]*(10**3+1) for _ in range(10**3+1)]#cow no　場所
    flag = [[0]*(10**3+1) for _ in range(10**3+1)]#条件を満たしていたか
    ans = 0
    for _ in range(N):
        x,y = map(int, input().split())
        table[x][y] = 1
        for i in cel:
            pos_x, pos_y = x+i[0], y+i[1]#update 処理ok
            if pos_x>=0 and pos_y>=0 and table[pos_x][pos_y]:
                check = judge(pos_x, pos_y, table)#ここの処理がだめ？
                if flag[pos_x][pos_y] and not check:
                    ans -= 1
                    flag[pos_x][pos_y] = 0
                elif not flag[pos_x][pos_y] and check:
                    ans += 1
                    flag[pos_x][pos_y] = 1
        print(ans)
    return



N = int(input())
main(N)