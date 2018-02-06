#include <iostream>

using namespace std;

int main(){
	int i;
	cin >> i;
	int arr[i];
	for(int j = 0; j < i; j++){
		cin >> arr[j];
	}
	int search;
	cin >> search;
	for(int j = 0; j < i; j++){
		if(arr[j] == search){
			cout << j << endl;
			return 0;
		}
	}
}
