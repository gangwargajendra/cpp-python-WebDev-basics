#include<iostream>
using namespace std;

void swap(int *a ,int *b){
    int t = *a;
    *a = *b;
    *b = t;
}

void printArray(int *arr ,int n){
    cout << "array : ";
    for(int i = 0 ; i < n ;i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}

void insertionSort(int *arr ,int n){
    for(int i = 1 ; i < n ; i++){
        int temp = arr[i];
        for(int j = i-1 ; j >= 0 ; j--){
            if(arr[j] > temp){
                swap(&arr[j] , &arr[j+1]);
            }
        }
    }
    printArray(arr, n);
}

int main(){
    int n;
    cout << "Enter size of an array : ";
    cin >> n ;

    int arr[n];

    cout << "Enter " << n << " elements of array : ";
    for(int i = 0; i < n ; i++){
        cin >> arr[i];
    }

    insertionSort(arr , n);
    return 0;
}