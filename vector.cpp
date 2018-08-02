#include <iostream>
#include <iomanip>
using namespace std ;
int main(){
  int m ,n ;
  m= 3; n =5;
vector < vector<int> > matrix (n);
for (int i= 0 ;i <m ; i++){
    for(int j= 0 ; j<n; j++)
    {
      matrix[i].push_back(i);
    }
}
for (int i= 0 ;i <m ; i++){
    for(int j= 0 ; j<n; j++)
    {
      cout<< matrix[i][j];
    }
    cout<< endl;
}
}
