#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(int argc, char *argv[]){
  int T, Ni;
  string Ns;
  bool found = false;
  vector<string> answ;
  cin >> T;

  for(int i = 0; i < T; i++){
    cin >> Ns;
    Ni = stoi(Ns);
    if(Ni < 10){
      answ.push_back(Ns);
    }
    else if(Ni == 1000){
      answ.push_back("999");
    }
    else{
      int i = Ns.length() - 1;
      while(i > 0){
        if(Ns[i] < Ns[i - 1]){
          Ni--;
          Ns = to_string(Ni);
          i = Ns.length() - 1;
        }
        else{
          i--;
        }
      }
      answ.push_back(Ns);
    }
  }

  for(int i = 0; i < answ.size(); i++){
    cout << "Deck #" << i + 1 << ": " << answ[i] << endl;
  }

  return 0;
}
