# success
import sys
sys.setrecursionlimit(1000000)
    
M, N, K = map(int,sys.stdin.readline().split())

square = list()
table = [[ 0 for _ in range(M)] for _ in range(N)]
# print("len")

# print(table.__len__())
# print(table[0].__len__())

def DFS(x, y, table):
    # print("DFS", x, y)
    # print(table)
    table[x][y] = 1
    area = 1
    if x < table.__len__() -1:
        # print("search x", x)
        if table[x+1][y] == 0:
            # print("search ",x+1, y)
            t_area, table = DFS(x+1, y, table)
            area = area + t_area

    if x > 0:
        # print("search x", x)
        if table[x-1][y] == 0:
            # print("search ",x+1, y)
            t_area, table = DFS(x-1, y, table)
            area = area + t_area

    if y < table[0].__len__() - 1:
        # print("search y",y, "table len", table.__len__())
        if table[x][y+1] == 0:
            # print("search ",x, y+1)
            t_area, table = DFS(x, y+1, table)
            area = area + t_area

    if y > 0:
        # print("search y",y, "table len", table.__len__())
        if table[x][y-1] == 0:
            # print("search ",x, y+1)
            t_area, table = DFS(x, y-1, table)
            area = area + t_area

    return area, table

# print(table)

for k in range(K):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    square.append([x1, y1, x2, y2])
    for x in range(x2-x1):
        for y in range(y2-y1):
            table[x1+x][y1+y] = 1
            

num_of_area = 0
total_area = list()
que=list()

for m in range(M):
    for n in range(N):
        if table[n][m] == 0:
            total_area.append(DFS(n,m, table)[0])
            num_of_area = num_of_area + 1
            

#print(table)
print(num_of_area)
print(*sorted(total_area), sep=" ")

        
