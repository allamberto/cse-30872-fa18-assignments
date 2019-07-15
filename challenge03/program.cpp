//Ana Luisa Lamberto - Challenge03

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(int argc, char *argv[]){
  int row, col, ntargets, num;
  vector<int> matrix;
  while(cin >> row >> col){
    if(row == 0 && col == 0) //check exit
      break;
    for(int i = 0; i < row * col; i++){
      cin >> num;
      matrix.push_back(num);
    }

    cin >> ntargets;
    int targets[ntargets] = {0};
    for(int i = 0; i < ntargets; i++){
      cin >> targets[i];
    }

    for(int i = 0; i < ntargets; i++){
      int target = targets[i];
      auto it = lower_bound(matrix.begin(), matrix.end(), target);
      int num = (it != matrix.end() && *it == target ? it - matrix.begin() : -1);
      if(num != -1){
        cout << target << " is at row=" << floor(num/col)  << ", col=" <<  num % col << endl;
      }
      else{
        cout << target << " is not in the grid" << endl;
      }
    }
  matrix.clear();
  }
  return 0;
}
