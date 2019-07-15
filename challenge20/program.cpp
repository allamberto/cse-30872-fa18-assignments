#include <iostream>
using namespace std;

int N, minimum;
int graph[103][103], backtrack[103]; // 100 max w/ buffer
const int INT_MAX = 999999999;

int findPath(int current, int target){
	if(current == target){
    return true;
  }
	for(int i = 1; i <= N; i++)
		if(backtrack[i] == 0 && graph[current][i] > 0){
			if(minimum > graph[current][i]){
        minimum = graph[current][i];
      }

			backtrack[i] = current;

			if(findPath(i,target) == 1){
				graph[current][i] -= minimum;
				graph[i][current] += minimum;
				return true;
			}
		}
	return false;
}

int findMaxFlow(int source, int target){
	int sum = 0;
	while(true){
		for(int i = 1; i <= N; i++){
      	backtrack[i] = 0;
    }
		minimum = INT_MAX;
		backtrack[source] = 1;
		if(findPath(source, target) == 0){
      return sum;
    }
		sum += minimum;
	}
}

int main(){
  int count = 0;
  while(cin >> N && N > 0){
    for(int r = 1; r <= N; r++){
      for(int c = 1; c <= N; c++){
        graph[r][c] = 0;
      }
    }

    int numConnect, source, target;
    cin >> source >> target >> numConnect;

    int node1, node2, capacity;
    for(int i = 0; i < numConnect; i++){
      cin >> node1 >> node2 >> capacity;
      graph[node1][node2] += capacity;
      graph[node2][node1] += capacity;
    }

    cout << "Network " << ++count << ": Bandwidth is " << findMaxFlow(source, target) << "." << endl;
  }
	return 0;
}
