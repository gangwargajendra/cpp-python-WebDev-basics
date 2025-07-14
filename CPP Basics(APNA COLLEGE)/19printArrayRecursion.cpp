#include<iostream>
using namespace std;

void printArray(int *arr , int st , int end){
    if(st == end + 1){
        return ;
    }
    cout << arr[st] << " ";
    printArray(arr, st+1 , end);
}

int factorial(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    return n * factorial(n-1);
}

void printNumberDec(int n){
    if(n == 0){
        return ;
    }
    cout << n << " ";
    printNumberDec(n-1);
}

int sumOfNnumbers(int n){
    if(n == 1){
        return 1;
    }
    return n + sumOfNnumbers(n-1);
}

int fibonacci(int n){
    if(n == 0 || n == 1){
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

bool arraySorted(int *arr , int size){
    if(size > 0){
        if(arr[size] < arr[size - 1]){
            return false;
        }
        return arraySorted(arr , size - 1);
    }
    return true;
}

int main(){
    int n;
    cout << "Enter size of array : ";
    cin >> n;
    cout <<"Enter " << n << " elements of array : " ;
    int arr[n];
    for(int i = 0 ; i < n ; i++){
        cin >> arr[i];
    }

    cout << "array is : ";
    cout <<   arraySorted(arr , n-1);
    return 0;
}