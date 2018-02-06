#include <iostream>
#include <string>
using namespace std;

int main(){
	string s;
	cin >> s;
	int counter = 0;
	char sos[] = {'S', 'O', 'S'};
	string sig_chomp;
	for(int i = 0; i < s.length(); i+=3){	
	        sig_chomp = s.substr(i, 3);
		if(sig_chomp != "SOS"){
			cout << sig_chomp << endl;
			for(int j = 0; j < 3; j++){
				if(sig_chomp[j] != sos[j]){
					counter++;
				}
			}
		}	
	}
	cout << counter << endl;
	return 0;
}
