#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	int a;
	int b;
	int sums = 0;
	for(int i = 0; i < N; i++){
		cin >> a >> b;
		sums += (a*b);
	}
	sums = float(sums);
	sums = sums * 1.05;
	cout << sums << endl;
}
