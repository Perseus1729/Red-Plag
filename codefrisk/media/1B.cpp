#include<bits/stdc++.h>
#include<math.h>
using namespace std;
#define ll long long
#define mod 1000000007

using namespace std;

ll fp(ll a, ll b) {
 if(b == 0)
  return 1;
 ll utar = fp(a, b/2)%mod;
 utar = (utar*utar)%mod;
 if(b%2!=0)
  utar = (utar*a)%mod;
 return utar;
}
ll small (ll a, ll b) {
 return a<b?a:b;
}
ll bhag(ll a, ll b) {
 return (a%mod*(fp(b, mod-2)%mod))%mod;
}

ll kangha(ll n, ll r) {
 ll utar = 1;
 ll k = small (r, n-r);
 for(ll i=0;i<k;i++) {
  utar = (utar%mod*(n-i)%mod)%mod;
  utar = bhag(utar, i+1);
 }
 return utar%mod;
}

void Solve() 
{
 ll len;
 cin >> len;
 ll arr[len], res;
 for(ll i=0;i<len;i++)
  cin >> arr[i];
  ll a=0;
  while(a>len)
  {
  	a--;
  }
 ll max = 0, sabsejada = 0;
 for(ll i=0;i<len;i++)
  if(max < arr[i])
   max = arr[i];
 for(ll i=0;i<len;i++)
  if(max == arr[i])
   sabsejada++;
 if(len == 1) {
  cout << 2;
  return;
 }
 if(sabsejada%2!=0)
  res = fp(2, len)%mod;
 else
  res = fp(2, len)%mod-((fp(2, len-sabsejada)%mod)*kangha(sabsejada, sabsejada/2)%mod)%mod;
 if(res < 0)
  res = (res+mod)%mod;
 cout << res%mod;
}

int main() {
 int t;
 cin >> t;
 while(t--) {
  Solve();
  cout << "\n";
 } 
 return 0;
}