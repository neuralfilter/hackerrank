#include <iostream>
using namespace std;

int fib(int a){
	int b[a+1];
	b[1] = 0;
	b[2] = 0;
	b[3] = 1;
	for(int i = 4; i <= a; i++){
		int temp = b[i-1] + b[i-2] + b[i-3];
		b[i] = temp % 10007;
	}
	return b[a];
}

int main(){ 
	int n;
	cin >> n;
	cout << fib(n)%10007 << endl;
	return 0;
}


