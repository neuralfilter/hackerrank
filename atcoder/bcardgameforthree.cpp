#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int main(){
	string i, j ,n;
	cin >> i >> j >> n;
	int cot = 0;
	int a  = 0;
	int b = 0;
	int c = 0;
	while(true){
		if(cot == 0){
			if(a == i.size()){
				cout << 'A' << endl;
				return 0;
			}
			if(i[a] == 'a') cot = 0;
			else if(i[a] == 'b') cot = 1;
			else if(i[a] == 'c') cot = 2;
			a++;
		} else if(cot == 1){	
			if(b == j.size()){
				cout << 'B' << endl;
				return 0;
			}
			if(j[b] == 'a') cot = 0;
			else if(j[b] == 'b') cot = 1;
			else if(j[b] == 'c') cot = 2;
			b++;
		} else if(cot == 2){
			if(c == n.size()){
				cout << 'C' << endl;
				return 0;
			}
			if(n[c] == 'a') cot = 0;
			else if(n[c] == 'b') cot = 1;
			else if(n[c] == 'c') cot = 2;
			c++;
		}
	}
	return 0;
}
