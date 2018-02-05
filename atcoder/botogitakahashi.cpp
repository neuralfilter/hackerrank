#include <iostream>
#include <vector>
#include <sort>
using namespace std;

vector<int> orders;
vector<int> lists;

int main() {
	int x;
	for(int i = 0; i < 10; i++){
		cin >> x;
		orders.push_back(x);
	}

	int num_in = 0;
	cin >> num_in;

	for(int j = 0; x < num_in; j++){
		cin >> x;
		for(int k = 0; k < string(x).length(); k++){

		}
		lists.push_back(x);
	}
	
	return 0;
}
