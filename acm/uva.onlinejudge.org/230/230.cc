/*
���⣺ģ��һ��ͼ��ݹ���ϵͳ��������������ͼ��ı�������ߣ�Ȼ��������ָ�
BORROWָ���ʾ���飬RETURNָ���ʾ���飬
SHELVE��ʾ�������ѹ黹����δ�ϼܵ�ͼ����������е���Ƚϴ�С��
��������β�����ܲ����ͼ�����Ͳ���λ�á�
ͼ������ķ������Ȱ����ߴ�С��������Ȼ���ٰ������С��������
�ڴ����һ��ָ��ǰ����Ӧ��������ͼ�鰴�����ַ�ʽ����

����ÿһ����������mapӳ������Ϊ������������ã�Ȼ���Զ���set<Node>��Node�����򷽷���
һ��������е��鵥������һ���滹����鵥��ÿ������һ��SHELVE���������鵥��ռ��ɡ�
�տ�ʼ��ΪֻҪ��������鵥���򣬶�����Ҫ��������е��鵥�Ƚϴ�С���˼��Ρ�
*/

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <sstream>
using namespace std;

typedef map<string, string> Map;

struct Node
{
	string title, name;
	
	Node() {}
	Node(string title, string name):title(title), name(name) {}
	bool operator < (const Node &rhs) const
	{
		if(name != rhs.name) return name < rhs.name;
		else return title < rhs.title;
	}
};

typedef set<Node> Set;

Map R;
Set list, S;
Set::iterator it, it1;

void setDel(string title)
{
	for(it = list.begin(); it != list.end(); it++)
		if(it->title == title)
			 { list.erase(it); break; }
}

Set::iterator find(string title)
{
	for(it = list.begin(); it != list.end(); it++)
		if(it->title == title)
			return (--it);
}

int main()
{
	list.clear(); R.clear(); S.clear();
	string s, title, name;
	int p, q;
	while(getline(cin, s))
	{
		if(s == "END") break;
		p = s.find('"', 1); q = s.find('y', p+1);
		title = s.substr(0, p+1); name = s.substr(q+2);
		list.insert(Node(title, name));
		R[title] = name;
	}
	
	string t, s2;
	while(getline(cin, s))
	{
		if(s == "END") break;
		if(s[0] == 'B')
		{
			p = s.find(' ');
			t = s.substr(0, p); s2 = s.substr(p+1);
			setDel(s2);
		}
		else if(s[0] == 'R')
		{
			p = s.find(' ');
			t = s.substr(0, p); s2 = s.substr(p+1);
			S.insert(Node(s2, R[s2]));
		}
		else if(s[0] == 'S')
		{
			for(Set::iterator it = S.begin(); it != S.end(); it++)
			{
				title = it->title;
				list.insert(Node(title, R[title]));
				if(list.begin()->title == title)
				{
					cout << "Put " << title << " first" << endl;
				}
				else
				{
					it1 = find(title);
					cout << "Put " << title << " after " << it1->title << endl;
				}
			}
			cout << "END" << endl;
			S.clear();
		}
	}
	return 0;
}
