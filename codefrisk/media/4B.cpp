/******************************************
*    AUTHOR:         julianferres         *
******************************************/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
#define FIN ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define forr(i, a, b) for(int i = (a); i < (int) (b); i++)
#define forn(i, n) forr(i, 0, n)
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define DBG(x) cerr << #x << " = " << (x) << endl
#define show(v,n) cerr << #v << " = "; forn(i,n) cerr << v[i] << " "; cerr << endl;
#define esta(x,c) ((c).find(x) != (c).end())
#define RAYA cerr << "===============================" << endl
const int inf = 1<<30; // const ll inf = 1LL<<62;
const int mod = 1e9+7; // 998244353
const int N  = 2e5+5;


int main() {
    FIN;
    
 	ll n, k;
	cin >> n >> k;
	string pal;
	cin >> pal;
	
	vector <ll> R(n,0), cuenta(n,0);
	if(pal[0]=='R') R[0]=1;
	forr(i,1,n)
	{
		R[i]=R[i-1];
		if(pal[i]=='R') R[i]++;
		else cuenta[i]=R[i];
	}
	
	reverse(all(pal));
	
	vector <ll> L(n,0), cuentaa(n,0);
	if(pal[0]=='L') L[0]=1;
	forr(i,1,n)
	{
		L[i]=L[i-1];
		if(pal[i]=='L') L[i]++;
		else cuentaa[i]=L[i];
	}
	
	reverse(all(pal)); reverse(all(cuentaa));

	ll changes = 0;
	
	for(auto u : cuenta) changes+=u;
	for(auto u : cuentaa) changes+=u;
	
	changes/=2;
	
	if(changes < k) {cout << "-1" << endl; return 0;}
	
	while(changes > k)
	{
		k--;
		vector <int> v;
		forn(i,pal.size()-1)
		{
			if(pal[i]=='R' && pal[i+1]=='L')
			{
				char aux = pal[i];
				pal[i]=pal[i+1];
				pal[i+1]=aux;
				changes--;
				v.pb(i+1);
				i++;
				if(changes == k) break;
			}
		}
		cout << v.size() << " ";
		for(auto u : v) cout << u << " "; cout << "\n";
	}
	
	vector <int> pos;
	
	forn(i,pal.size())
	{
		if(pal[i]=='L') pos.pb(i);
	}
	

	forn(i,pos.size())
	{
		forn(j,pos[i]-i)
		{
			
			cout << "1 " << pos[i]-j << "\n";
		}
	}
	
	
	
	
    return 0;
}