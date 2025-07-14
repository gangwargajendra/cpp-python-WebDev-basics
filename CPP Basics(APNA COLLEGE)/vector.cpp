#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> vec1;
    cout << "size of vec1 : " << vec1.size() << endl;

    vector<int> vec2 = {1, 2, 3, 4};
    cout << "size of vec2 : " << vec2.size() << endl;
    cout << "element of vec2 : " ;
    for(int i = 0 ; i < vec2.size() ;i++){
        cout << vec2[i] << " ";
    }
    cout << endl;

    vector<int> vec3(10, -1);   // vector will create of size 10 and all index will initialise with -1.
    cout << "size of vec3 : " << vec3.size() << endl;
    cout << "element of vec3 : " ;
    for(int i = 0 ; i < vec3.size() ;i++){
        cout << vec3[i] << " ";
    }
    return 0;
}