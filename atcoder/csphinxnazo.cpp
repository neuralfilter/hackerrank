#include <iostream>
using namespace std;

int n;
int m;

int main() {
	cin >> n >> m;
	for(int i = 0; i < n+1; i++) {
		for(int j = 0; j < n-i+1; j++){
			if((i*2)+(j*3) > m){
				break;
			}
			if(((i*2)+(0)+(n-i-j)*4) == m && n-j == n){
				cout << i << " " << 0 << " " <<  n-i-j << endl;
				return 0;
			}
			if(((i*2)+3+(n-i-j)*4) == m && n-j+1 == n){
				cout << i << " " << 1 << " " << n-i-j << endl;
				return 0;
			}
		}
	}
	cout << -1 << " " << -1 << " " << -1 << endl;
	return 0;
}
