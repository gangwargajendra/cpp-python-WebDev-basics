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

void selectionSort(int *arr ,int n){
    for(int i = 0 ; i < n-1 ; i++){
        int minIndex = i;
        for(int j = i+1 ; j < n ; j++){
            if (arr[j] < arr[minIndex] ){
                minIndex = j;
            }
        }
        swap(&arr[minIndex] , &arr[i]);
    }
    printArray(arr , n);
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

    selectionSort(arr , n);
    return 0;
}