#include <iostream>  
#include <cstdlib>  
#include <cstring>  
#include <cstdio>  
#include <string>  
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
using namespace std;

const int maxn = 110;
const int maxm = 1600;

string article[maxn][maxm];
string cache[maxn][maxm];

int n, m;
int size[maxn];

void transform(string &s)
{
	for(int i = 0; i < s.length(); i++)
		if(isupper(s[i]))
			s[i] = tolower(s[i]);
}

int search1(string s)
{
	string t;
	int ok = 0;
	string ans = "";
	int find = 0;
	for(int i = 0; i < n; i++)
	{
		if(ok) { ans += "----------\n"; ok = 0; }
		for(int j = 0; j < size[i]; j++)
		{
			t = cache[i][j];
			if(t.find(s) != string::npos)
			{
				find = 1;
				ans += article[i][j] + "\n";
				ok = 1;
			}
		}
		if(ok) { ans += "----------\n"; ok = 0; }
	}
	if(!find) return 0;
	ans = ans.substr(0, ans.length()-11);
	cout << ans;
}

int search2(string s)
{
	bool vis[maxn] = {0};
	int find = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < size[i]; j++)
		{
			string t = cache[i][j];
			if(t.find(s) != string::npos) { vis[i] = 1; break; }
		}
	}
	string ans = "";
	for(int i = 0; i < n; i++) if(!vis[i])
	{
		find = 1;
		for(int j = 0; j < size[i]; j++)
		{
			ans += article[i][j] + "\n";
			cout << article[i][j] << endl;
		}
		ans += "----------\n";
	}
	if(!find) return 0;
	ans = ans.substr(0, ans.length()-11);
	cout << ans;
}

int search3(string s, string t)
{
	string ans = "";
	int find = 0;
	for(int i = 0; i < n; i++)
	{
		int e1 = 0, e2 = 0, exist = 0;
		for(int j = 0; j < size[i]; j++)
		{
			string q = cache[i][j];
			if(q.find(s) != string::npos) e1 = 1;
			if(q.find(t) != string::npos) e2 = 1;
			if(e1 && e2) { exist = 1; break; }
		}
		if(exist)
		{
			find = 1;
			for(int j = 0; j < size[i]; j++)
			{
				string q = cache[i][j];
				if(q.find(s) != string::npos || q.find(t) != string::npos)
					{ ans += article[i][j] + "\n"; }
			}
			ans += "----------\n";
		}
	}
	if(!find) return 0;
	ans = ans.substr(0, ans.length()-11);
	cout << ans;
}

int search4(string s, string t)
{
	int ok = 0;
	string ans = "";
	int find = 0;
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < size[i]; j++)
		{
			string q = cache[i][j];
			if(q.find(s) != string::npos || q.find(t) != string::npos)
				{ ans += article[i][j] + "\n"; ok = 1; find = 1; }
		}
		if(ok) { ans += "----------\n"; ok = 0; }
	}
	if(!find) return 0;
	ans = ans.substr(0, ans.length()-11);
	cout << ans;
}

void read()
{
	scanf("%d", &n);
	memset(size, 0, sizeof(size));
	string s;
	for(int i = 0; i < n; i++)
	{
		int N = 0;
		while(getline(cin, s) && s != "**********")
		{
			article[i][N] = s;
			transform(s);
			cache[i][N++] = s;
		}
		size[i] = N;
	}
}

void print()
{
	string s, t[3];
	int q; scanf("%d", &q);
	getline(cin, s);
	
	while(q--)
	{
		int b = 0, find = 0;
		getline(cin, s);
		stringstream ss(s);
		while(ss >> t[b]) b++;
		if(b == 1)
		{
			find = search1(t[0]);
		}
		else if(b == 2)
		{
			find = search2(t[1]);
		}
		else if(b == 3)
		{
			if(t[1] == "AND")
			{
				find = search3(t[0], t[2]);
			}
			else if(t[1] == "OR")
			{
				find = search4(t[0], t[2]);
			}
		}
		if(!find) cout << "Sorry, I found nothing." << endl;
		cout << "==========" << endl;
	}	
}

int main()
{
	read();
	print();
	return 0;
}
