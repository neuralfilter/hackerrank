#include <iostream>
#include <string>
using namespace std;

int main() {
	int i;
	cin >> i;
	char vowels[5] = {'a', 'e', 'i', 'o', 'u'};
	int counter;
	for(int j = 0; j < i; j++){
		counter = 0;
		string original;
		cin >> original;
		char inputted[original.length()];
		for(int k = 0; k < original.length(); k++){
			inputted[k] = tolower(original[k]);
		}
		for(int m = 0; m < original.length(); m++){
			for(int l = 0; l < 5; l++){
				if(vowels[l] == inputted[m]){
					counter+=1;
				}
			}
		}
		cout << counter << endl;
	}	
	return 0;
}
