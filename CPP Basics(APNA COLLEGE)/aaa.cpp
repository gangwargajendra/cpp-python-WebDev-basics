#include<iostream>
using namespace std;

int main(){
    int m ,n;
    cin >> m;
    cin >> n;

    int **arr = new int*[m];
    int i;
    for(i = 0; i < m ; i++){
        arr[i] = new int[n];
    }

    cout << "Enter element   " << m * n << " :";
    for(i = 0 ; i <  m ; i++) {
        for(int j = 0 ; j < n ; j++){
            cin >> arr[i][j];
        }
    }

    for(i = 0 ; i < m ; i++){
        cout << i << "th row : ";
        for( int j = 0; j < n ; j++){
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }

    
    return 0;
}