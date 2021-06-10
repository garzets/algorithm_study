"""
2       num of test case
3 2     V,E value of test case 1
1 3
2 3
4 4     V,E value of test case 2
1 2
2 3
3 4
4 2
"""

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


num_of_test = input()
#print("number of test case ",num_of_test)


for test in range(1, int(num_of_test) + 1):
    V,E = input().split()

    graph = list()
    #colored = list()
    color = list()
    answer = True

    for i in range(1 + int(V)):
        graph.append(list())
        #colored.append(0)
        color.append(0)

    #print("V, E ", V, E)
    for e in range(1, int(E) + 1):
        #print(input())
        v1, v2 = input().split()
        
        v1 = int(v1)
        v2 = int(v2)

        graph[v1-1].append(v2)
        graph[v2-1].append(v1)

    #print("\ngraph : ", graph)
    answer = True
    #colored[0] = 1
    color[0] = 1

    if DFS(0):
        print("YES")
    else:
        print("NO")

#print("colored : ", colored)
#print("color : ", color)
#print("graph : ", graph)
"""
        if(colored[v1-1]==0):
            colored[v1-1] = 1
            graph[v1-1] = graph[v2-1] ^ 1

        if(colored[v2-1]==0):
            colored[v2-1] = 1
            graph[v2-1] = graph[v1-1]^ 1

        if(graph[v2-1] == graph[v1-1]):
            answer = False
            break
        """

