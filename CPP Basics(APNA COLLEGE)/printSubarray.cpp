#include<iostream>
using namespace std;

void printSubarray(int *arr ,int n){
    int count = 1;
    
    for(int start = 0; start < n ; start++){
        for(int end = start ; end < n ; end++){
            //cout << "(" << start << "," << end << ") " ;
            cout << count++ <<"th array : ";
            for(int i = start ; i <= end ; i++){
                cout << arr[i] << " ";
            }
            cout << "\n";
        }
    }
}

int main(){
    int n;
    cout << "Enter size of array : " ;
    cin >> n ;

    int arr[n];
    cout << "Enter " << n << " elements of arrray : ";
    for(int i = 0 ; i < n ; i++){
        cin >> arr[i];
    }

    cout << "subarray : " << endl;
    printSubarray(arr , n);
    return 0;
}