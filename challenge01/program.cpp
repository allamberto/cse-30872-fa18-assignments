//Ana Luisa Lamberto - Challenge 01
#include <iostream>
#include <string>

using namespace std;
const size_t NLETTERS = 26;

int count_word(string &s1, string &s2){

  int total = 0;
  //2. Compare Sizes
  if(s1.length() < s2.length()){
    return total;
  }

  //3. Compute Histograms
    size_t h1[NLETTERS] = {0};
    size_t h2[NLETTERS] = {0};

    for(auto c: s1){
      h1[tolower(c) - 'a']++;
    }

    for(auto c: s2){
      h2[tolower(c) - 'a']++;
    }

  //4. Compare Histograms
  bool cont_count = true;
  while(cont_count){
    for(size_t i = 0; i < NLETTERS; i++){
      if(h1[i] < h2[i]){ //if no enough letters left, end program
        cont_count = false;
        break;
      }
      else if(h2[i] != 0){ //"use letter" - aka one less letter to work with
        h1[i] = h1[i] - h2[i];
      }
    }
    total++;
  }

  return --total; //account for final total that was added when breaked
}

int main(int argc, char *argv[]){
  //1. Read Input
  string s1, s2;

  while(cin >> s1 >> s2){
    //5. Output Result
    cout << count_word(s1, s2) << endl;
  }
}
