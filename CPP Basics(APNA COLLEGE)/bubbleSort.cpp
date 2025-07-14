#include<iostream>
using namespace std;

void swap(int *a , int *b){
    int t = *a;
    *a = *b;
    *b = t;
}

void bubbleSort(int *arr ,int n){
    bool flag = false;

    for(int i = 0 ; i < n-1 ; i++){
        for(int j = 0 ; j < n-i-1 ; j++){
            if(arr[j] > arr[j+1]){        // if we exchange '>' to this '<' then arrray will be sorted in decending order 
                swap( &arr[j] , &arr[j+1] );
                flag = true;
            }
        }
        if(!flag){
            break;
        }
    }
}

int main(){
    int n;
    cout << "Enter size of an array : ";
    cin >> n;

    int arr[n];
    cout << "Enter " << n << " elements of array : ";
    for(int i = 0 ;i < n ; i++){
        cin >> arr[i];
    }

    bubbleSort(arr , n);
    cout << "sorted array : ";
    for(int i=0 ; i<n ; i++){
        cout << arr[i] <<" ";
    }
    return 0;
}