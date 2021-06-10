# Success
import sys

def DFS(node):
    # graph :  [[2], [1, 3, 4], [2, 4], [3, 2], []]
    tmp_answer = True

    for n in range(graph[node].__len__()):
        if(color[graph[node][n]-1]==0):
            color[graph[node][n]-1]=color[node]*(-1)

            if( DFS(graph[node][n]-1) == False) :
                return False
        else:
            if color[graph[node][n]-1] == color[node]:
                return False

    return True

def BFS(node):
    tmp_answer = True
    node_queue = list()

    for n in range(graph[node].__len__()):
        if(color[graph[node][n]-1]==0):
            color[graph[node][n]-1]=color[node]*(-1)
            node_queue.append(graph[node][n]-1)

        else:
            if color[graph[node][n]-1] == color[node]:
                return False

    while node_queue:
        if(BFS(node_queue.pop()) == False):
            return False
    else:
        return True

sys.setrecursionlimit(10**6)
num_of_test = sys.stdin.readline() # use sys.stdin.readline() instead of input() , because it is more fast

for test in range(1, int(num_of_test) + 1):
    V,E = sys.stdin.readline().split()

    # if test case has just one vertice and one edges
    if V==1 and E==1:
        v1, v2 = sys.stdin.readline().split()
        print("YES")
        continue

    graph = list()
    node_queue = list()
    #colored = list()
    color = list()
    answer = True

    for i in range(int(V)):
        graph.append(list())
        #colored.append(0)
        color.append(0)

    #print("V, E ", V, E)
    for e in range(1, int(E) + 1):
        v1, v2 = sys.stdin.readline().split()
        
        v1 = int(v1)
        v2 = int(v2)

        graph[v1-1].append(v2)
        graph[v2-1].append(v1)

    #print("\ngraph : ", graph)
    answer = True
    #colored[0] = 1
    color[0] = 1

    # if BFS(0):
    #     print("YES")
    # else:
    #     print("NO")

    que = list()
    que.append(0)
    color[0]=1

    answer = "YES"

    while que:
        node = que.pop()

        for n in range(graph[node].__len__()):
            if color[graph[node][n]-1] == 0 : # if next node was not yet visited
                color[graph[node][n]-1] = color[node]*(-1) # set color different from current node
                que.append(graph[node][n]-1)
                # print("push ",graph[node][n]-1)
            else : # if it visited, compare color
                if color[graph[node][n]-1] == color[node] :
                    answer = "NO"
    
        # if there is unconnected node remains
        if not que:
            try:
                # set the node visited
                ret = color.index(0)

                # and push to que to BFS
                que.append(ret)
                color[ret]=1
            except:
                break

    print(answer)

