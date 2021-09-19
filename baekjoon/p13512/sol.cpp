#include <iostream>
#include <list>
#include <queue>

#define SIZE 100000
using namespace std;

list<int> node[SIZE];
int visited[SIZE];
int color[SIZE];

int DFS(int src, int dst);
void initialize(void);
int N,M;

int main(void)
{


    cin >> N;

    for (int i = 0; i<SIZE; i++)
    {
        color[i]=1; // 1 = white
    }

    for (int i = 0; i<N-1; i++)
    {
        int x,y;
        cin >> x >> y;
        node[x-1].push_back(y);
        node[y-1].push_back(x);
    }

    cin >> M;

    int querry, point;

    for (int i = 0; i<M; i++)
    {
        initialize();

        cin >> querry >> point;
        if(querry == 1) // change color
        {
            color[point-1] = color[point-1]*(-1);
        }
        else if (querry == 2)
        {
            int ret;
            visited[0]=1;

            ret = DFS(1,point);

            if(ret==0)
            {
                cout << "-1\n";
            }
            else
            {
                cout << ret << "\n";
            }
        }
    }

    return 0;
}

void initialize(void)
{
    for (int i=0;i<N;i++)
    {
        visited[i]=0;
    }
}

int DFS(int src, int dst)
{
    int ret;

    for (auto v : node[src-1])
    {
        if(v == dst)
        {
            if (color[src-1]==-1)
            {
                return src;
            }
            else
            {
                if (color[v-1]==-1)
                {
                    return v;
                }
                else
                {
                    return 0;
                }
            }
        }

        if(visited[v-1]==0)
        {
            visited[v-1]=1;

            ret = DFS(v,dst);

            if (ret>=0) // find dst
            {
                if(color[src-1]==-1) // current color black
                {
                    return src;
                }
                else // current color is not black, return next value
                {
                    return ret;
                }
            }
        }
    }

    return -1; // can't find dst
}