#include<bits/stdc++.h>
#define mod 1000000007
 
using namespace std;
 
long long multi(long long a, long long b)  {
  if(b == 0)
    return 1;
  long long ans = multi(a, b/2)%mod;
  ans = (ans*ans)%mod;
  if(b%2!=0)
    ans = (ans*a)%mod;
  return ans;
}
long long min(long long a, long long b)  {
  return a<b?a:b;
}
long long divi(long long a, long long b)  {
  return (a%mod*(multi(b, mod-2)%mod))%mod;
}
 
long long comb(long long n, long long r)  {
  long long ans = 1;
  long long k = min(r, n-r);
  for(long long i=0;i<k;i++)  {
    ans = (ans%mod*(n-i)%mod)%mod;
    ans = divi(ans, i+1);
  }
  return ans%mod;
}
 
void subMain()  {
  long long n;
  cin >> n;
  long long a[n], ans;
  for(long long i=0;i<n;i++)
    cin >> a[i];
  long long max = 0, maxcp = 0;
  for(long long i=0;i<n;i++)
    if(max < a[i])
      max = a[i];
  for(long long i=0;i<n;i++)
    if(max == a[i])
      maxcp++;
  if(n == 1)  {
    cout << 2;
    return;
  }
  if(maxcp%2!=0)
    ans = multi(2, n)%mod;
  else
    ans = multi(2, n)%mod-((multi(2, n-maxcp)%mod)*comb(maxcp, maxcp/2)%mod)%mod;
  if(ans < 0)
    ans = (ans+mod)%mod;
  cout << ans%mod;
}
 
int main()  {
  ios_base::sync_with_stdio(false);
    cin.tie(NULL);
  int t = 1;
  cin >> t;
  while(t--)  {
    subMain();
    cout << "\n";
  }  
  return 0;
}