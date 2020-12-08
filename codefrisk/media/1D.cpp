#include <bits/stdc++.h> 
#define mod 1000000007
#define pb push_back
#define len length()
#define umap unordered_map
#define ll long long
#define endl "\n"
#define pii pair<int, int>
using namespace std;  

ll power(ll x, ll n)
{
	ll res=1;
	while(n){
		if(n&1)
			res=res*x%mod;
		n=n/2;
		x=x*x%mod;
	}
	return res;
}

ll divt(ll a, ll b)
{
	return (a%mod * (power(b,mod-2)%mod))%mod;
}


ll func(ll n, ll r)
{
	ll ans=1;
	ll k=min(r, n-r);
	for(ll i=0; i<k ;i++)
	{
		ans=(ans%mod * (n-i)%mod)%mod;
		ans=divt(ans, i+1);
	}
	return ans%mod;
}

void solve()
{
	ll n;
	cin>>n;
	ll a[n], ans;
	for(ll i=0; i<n; i++)
		cin>>a[i];

	ll max=0, maxval=0;
	for(int i=0; i<n; i++)
	{
		if(max<a[i])
			max=a[i];
	}

	for(int i=0; i<n; i++)
	{
		if(max==a[i])
			maxval++;
	}

	if(n==1){
		cout<<2<<endl;
		return;
	}
	if(maxval%2!=0)
		ans=power(2, n)%mod;
	else
		ans=power(2, n)%mod-((power(2, n-maxval)%mod) * func(maxval, maxval/2)%mod)%mod;

	if(ans<0)
		ans=(ans+mod)%mod;
	cout<<ans%mod<<endl;

}

int main() 
{ 
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL); 

#ifndef ONLINE_JUDGE 
	freopen("input.txt", "r", stdin);  
	freopen("output.txt", "w", stdout); 
#endif 

	int t;
	cin>>t;
	while(t--)
	{
		solve();
	}
}