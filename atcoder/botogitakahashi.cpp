#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> orders;
vector<int> lists;
int corres[10];
int aries[10];

int main() {
	int x;
	for(int i = 0; i < 10; i++){
		cin >> x;
		orders.push_back(x);
		corres[x] = i;
		aries[i] = x;
	}
	int num_in = 0;
	cin >> num_in;

	for(int j = 0; j < num_in; j++){
		int digits = 1;
		int convert = 0;
		cin >> x;
		for(int k = 0; k < 10; k++){
			convert += digits*corres[(x/digits)%10];
			digits *= 10;
		}
		lists.push_back(convert);
	}
	sort(lists.begin(), lists.end());
	for(int i = 0; i < num_in; i++){
		int digits = 1;
		int convert = 0;
		for(int k = 0; k < 10; k++){
			convert += digits*aries[(x/digits)%10];
			digits *= 10;
		}
		cout << convert << endl;
	}
	return 0;
}
