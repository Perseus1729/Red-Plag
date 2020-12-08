#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long int
typedef tree<int, null_type, less<int>, rb_tree_tag,
            tree_order_statistics_node_update> indexed_set;
#define MOD 1000000007
#define MXLP for (int i=0; i<n; i++) {\
                    if(max<a[i])\
                    max=a[i]; \
                    }
#define LOOPX for(int i=0; i<n; i++) {\
            if(max==a[i])\
            max_value++; }
#define loopl for(int i=0; i<k; i++) {\
            ans = (ans % MOD * (n-i) % MOD) % MOD;\
            ans=divl(ans, i + 1);\
            }
void soln();
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
#ifndef ONLINE_JUDGE
    clock_t tstart = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    soln();
#ifndef ONLINE_JUDGE
    fprintf(stderr, "Runtime: %.10fs\n", (double)(clock() - tstart) / CLOCKS_PER_SEC);
#endif
    return 0;
}
ll powLL(ll x, ll n)
{
    ll res=1;
    while(n)
    {
        if(n & 1)
           res=res * x %MOD;
        n = n / 2;
        x = x * x % MOD;
        
        
    }
    return res;
}
ll divl(ll a, ll b)
{
    return(a % MOD * (powLL(b, MOD - 2) % MOD)) % MOD;
    
}
ll soln1(ll n, ll r)
{
   ll ans = 1;
   ll k = min(r,n - r);
   loopl;
   return ans % MOD;
}
void soln()
{
    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        ll a[n],ans;
        for(ll i=0; i<n; i++)
        cin>>a[i];
        ll max = 0,max_value = 0;
        MXLP
        LOOPX
        if(n == 1)
        {
            cout<< 2 <<endl;
            continue;
            
        }
        if(max_value % 2!=0)
        
            ans=powLL(2, n) % MOD;
        else
        {
            ans=powLL(2, n) % MOD - 
                ((powLL(2, n-max_value) % MOD) * soln1(max_value, max_value / 2) % MOD) % MOD;
            
            
        }
        if(ans < 0)
        ans = (ans + MOD) % MOD;
        cout<<ans % MOD<<endl;
    }
    return;
}