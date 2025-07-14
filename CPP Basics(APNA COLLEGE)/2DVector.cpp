#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector <vector<int> > matrix = {{1,2,3} , {4, 5, 6} , {7,8,9}};
    //vector <vector<int> > matrix = {{1,2,3} , {4, 5} , {7}};   // can also possible
    for(int i = 0 ; i < matrix.size() ; i++){
        for(int j = 0 ; j < matrix[i].size() ; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
     
    vector <int > vec;
    for(int i = 0 ; i < 5 ; i++){  // i=0 s=1 c=1, i=1 s=2 c=2, i=2 s=3 c=4, i=3 s=4 c=4, i=4 s=5 c=8 
        vec.push_back(i);
    }
    cout << "size of vec : " << vec.size() << endl;
    cout << "capacity of vec : " << vec.capacity() << endl;
    return 0;
}