#include<iostream>
using namespace std;

void printArray(int *arr ,int n){
    cout << "array : ";
    for(int i = 0 ; i < n ;i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
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

    // for ascending order
    sort(arr , arr+n);

    cout << "in ascending order : ";
    printArray(arr , n);

    // for descending order
    sort(arr, arr+n , greater<int>());

    cout << "in ascending order : ";
    printArray(arr , n);

    return 0;
}