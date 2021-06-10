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

num_of_test = input()
#print("number of test case ",num_of_test)

for test in range(1, int(num_of_test) + 1):
    V,E = input().split()

    graph = list()
    colored = list()
    color = list()
    answer = True

    for i in range(1 + int(V)):
        graph.append(list())
        colored.append(0)
        color.append(1)

    #print("V, E ", V, E)
    for e in range(1, int(E) + 1):
        #print(input())
        v1, v2 = input().split()
        
        v1 = int(v1)
        v2 = int(v2)

        graph[v1-1].append(v2)
        graph[v2-1].append(v1)

    # search
    for v in range (graph.__len__()):
        # visit each vertices
        if colored[v] == 0 :
            colored[v] = 1
            #print("visit node ", v, graph[v].__len__())
            # paint each connected node
            for n in range(graph[v].__len__()):
                #print("graph[v][n]", "n", n, "v", v)
                if colored[graph[v][n]-1] == 0:
                    colored[graph[v][n]-1] = 1
                    color[graph[v][n]-1] = color[v] * (-1)
        for n in range(graph[v].__len__()):
            if color[graph[v][n]-1] == color[v]:
                answer = False

    if answer :
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