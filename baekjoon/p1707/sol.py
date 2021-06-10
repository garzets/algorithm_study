# FAILED
import sys

def DFS(node):
    # graph :  [[2], [1, 3, 4], [2, 4], [3, 2], []]
    tmp_answer = True

    #print("DFS node ",node + 1)
    for n in range(graph[node].__len__()):
        if(color[graph[node][n]-1]==0):
            color[graph[node][n]-1]=color[node]*(-1)

            if( DFS(graph[node][n]-1) == False) :
                return False
        else:
            #print("compare coloe ",graph[node][n],color[graph[node][n]-1], color[node], node+1)
            if color[graph[node][n]-1] == color[node]:
                #print("Not binary")
                return False

    return True

def BFS(node):
    # graph :  [[2], [1, 3, 4], [2, 4], [3, 2], []]
    tmp_answer = True
    node_queue = list()

    for n in range(graph[node].__len__()):
        if(color[graph[node][n]-1]==0):
            color[graph[node][n]-1]=color[node]*(-1)
            node_queue.append(graph[node][n]-1)

        else:
            #print("compare coloe ",graph[node][n],color[graph[node][n]-1], color[node], node+1)
            if color[graph[node][n]-1] == color[node]:
                #print("Not binary")
                return False

    #print("\nqueue", node_queue)

    while node_queue:
        if(BFS(node_queue.pop()) == False):
            return False
    else:
        return True

sys.setrecursionlimit(10**6)
num_of_test = sys.stdin.readline()
#print("number of test case ",num_of_test)


for test in range(1, int(num_of_test) + 1):
    V,E = sys.stdin.readline().split()

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
    # print("push 0")
    color[0]=1

    answer = "YES"

    while que:
        node = que.pop()
        # print("queue pop node",node)

        for n in range(graph[node].__len__()):
            if color[graph[node][n]-1] == 0 : # if next node was not yet visited
                color[graph[node][n]-1] = color[node]*(-1) # set color different from current node
                que.append(graph[node][n]-1)
                # print("push ",graph[node][n]-1)
            else : # if it visited, compare color
                if color[graph[node][n]-1] == color[node] :
                    answer = "NO"
    
        if not que:
            try:
                ret = color.index(0)
                que.append(ret)
                color[ret]=1
                #print("uncolored index", ret)
                #sys.exit(0)
            except:
                # print("there no uncolored")
                break

    # print(graph)
    # print(color)
    print(answer)

