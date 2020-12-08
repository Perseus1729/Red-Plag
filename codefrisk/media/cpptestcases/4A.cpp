#include <bits/stdc++.h>
using namespace std;
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
typedef long long ll;
typedef unsigned long long ull;
#define FIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define forr(i, a, b) for(ll i = (a); i < (ll) (b); i++)
#define forn(i, n) forr(i, 0, n)
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define DBG(x) cerr << #x << " = " << (x) << endl
#define esta(x,c) ((c).find(x) != (c).end())
#define MOD 1000000007



int main() {
    FIN;
    
    #ifdef input
		freopen("test2.txt", "r", stdin);
	#endif
	
	ll n, k;
	cin >> n >> k;
	string pal;
	cin >> pal;
	
	vector <ll> R(n,0), contl(n,0);
	if(pal[0]=='R') R[0]=1;
	forr(i,1,n)
	{
		R[i]=R[i-1];
		if(pal[i]=='R') R[i]++;
		else contl[i]=R[i];
	}
	
	reverse(all(pal));
	
	vector <ll> L(n,0), contr(n,0);
	if(pal[0]=='L') L[0]=1;
	forr(i,1,n)
	{
		L[i]=L[i-1];
		if(pal[i]=='L') L[i]++;
		else contr[i]=L[i];
	}
	
	reverse(all(pal)); reverse(all(contr));
	//for(auto u : contl) cout << u << " "; cout << endl;
	//for(auto u : contr) cout << u << " "; cout << endl;
	
	ll cambios = 0;
	
	for(auto u : contl) cambios+=u;
	for(auto u : contr) cambios+=u;
	
	cambios/=2;
	//DBG(cambios);
	
	if(cambios < k) {cout << "-1" << endl; return 0;}
	
	while(cambios > k)
	{
		k--;
		ll cont = 0;
		vector <int> v;
		forn(i,pal.size()-1)
		{
			if(pal[i]=='R' && pal[i+1]=='L')
			{
				char aux = pal[i];
				pal[i]=pal[i+1];
				pal[i+1]=aux;
				cambios--;
				v.pb(i+1);
				i++;
				if(cambios == k) break;
			}
		}
		cout << v.size() << " ";
		for(auto u : v) cout << u << " "; cout << "\n";
	}
	
	vector <int> pos;
	//DBG(pal);
	
	forn(i,pal.size())
	{
		if(pal[i]=='L') pos.pb(i);
	}
	
	//for(auto u : pos) cout << u << " "; cout << endl;
	
	forn(i,pos.size())
	{
		forn(j,pos[i]-i)
		{
			
			cout << "1 " << pos[i]-j << "\n";
		}
	}
	
	
	
	
	
	
    return 0;
}