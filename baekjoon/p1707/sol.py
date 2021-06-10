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

for test in range (1, int(num_of_test) + 1):
    V,E = input().split()

    graph = list()
    colored = list()
    answer = True

    for i in range(1+ int(V)):
        graph.append(0)
        colored.append(0)

    #print("V, E ", V, E)
    for e in range(1, int(E) + 1):
        #print(input())
        v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)

        if(colored[v1-1]==0):
            colored[v1-1] = 1
            graph[v1-1] = graph[v2-1] ^ 1

        if(colored[v2-1]==0):
            colored[v2-1] = 1
            graph[v2-1] = graph[v1-1]^ 1

        if(graph[v2-1] == graph[v1-1]):
            answer = False
            break

    if answer :
        print("YES")
    else:
        print("NO")

