#include <iostream>
using namespace std;

int maxPath, n, m;
int adj[30][30];

// Remove Edges from Matrix While Recursing
void findLongestPath(int nd, int count) {
    if(count > maxPath)
        maxPath = count;
    for(int i = 0; i < n; i++) {
        if(adj[nd][i]) {
            adj[nd][i] = 0;
            adj[i][nd] = 0;
            findLongestPath(i, count + 1);
            adj[nd][i] = 1;
            adj[i][nd] = 1;
        }
    }
}

// Main Execution
int main(){

  while(cin >> n >> m && n && m){

    // Reset Matrix
    for(int r = 0; r < n; r++){
      for(int c = 0; c < n; c++){
        adj[r][c] = 0;
      }
    }

    // Build Matrix
    for(int i = 0; i < m; i++){
      int node1, node2;
      cin >> node1 >> node2;
      adj[node1][node2] = 1;
      adj[node2][node1] = 1;
    }

    // Find Longest Path for Every Node
    maxPath = 0;
    for(int i = 0; i < n; i++){
      findLongestPath(i, 0);
    }

    // Print Result
    cout << maxPath << endl;
  }
}
