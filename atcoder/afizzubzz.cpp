#include <iostream>
using namespace std;

int main() {
	int N = 0;
	int i = 0;
	cin >> N;
	int a[to_string(N).length()];
	if(N % 3 == 0) {
		cout << "YES" << endl;
		return 0;
	}
	while(N) {
		a[i++] = N % 10;
		N /= 10;
	}
	for(int j = 0; j <= i; j++){
		if (a[j] == 3){
			cout << "YES" << endl;
			return 0;
		}
	}
	cout << "NO" << endl;
}
