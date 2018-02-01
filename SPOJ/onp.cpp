#include <iostream>
#include <string>
#include <stack>
using namespace std;

int num_input = 0;
int main() {
	stack <int> g;
	std::string rpn;
	std::cin >> num_input;
	for(int i = 0; i < num_input; i++){
		std::cin >> rpn;
		int n = rpn.length();
		char char_array[n+1];
		strcpy(char_array, rpn.c_str());
		for(int i = 1; i < n-1; i++){
			cout << char_array[i];
		}
	}
	return 0;
}
