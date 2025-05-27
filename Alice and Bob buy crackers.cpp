#include<bits/stdc++.h>
using namespace std;

int main()
{


    int m;
    cin >> m;
    int cost[m];
    for(int i = 0; i < m; i++)
        cin >> cost[i];
    int firecrakers = 0;
    bool temp[20000 * m] = {0};
    for(int i = 0; i < (1<<m); i++)
    {
        long long int sum = 0;
        for(int j = 0; j < m; j++)
            if(i & (1<<j))
                sum += cost[j];
        if(!(temp[sum]) && sum && !(sum & 1))
            firecrakers++;
        temp[sum] = {1};
    }
    cout << firecrakers;
    return 0;
}
