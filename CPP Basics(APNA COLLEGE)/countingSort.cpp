#include<iostream>
using namespace std;

void printArray(int *arr ,int n){
    cout << "array : ";
    for(int i = 0 ; i < n ;i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
}
 
// generally it is used if range is less
void countingSort(int *arr , int n){
    int frequency[10000] = {0};  // all index will be initilise with 0  

    int maxValue = INT8_MIN , minValue = INT8_MAX;
    for(int i = 0 ; i < n ; i++){
        minValue = min( minValue , arr[i]);
        maxValue = max( maxValue , arr[i]);
    }

    // To store the frequency
    for(int i = 0 ; i < n ; i++){
        frequency[arr[i]]++;
    }
    // for modifying the original array
    int count = 0;
    for(int i = minValue ; i <= maxValue ; i++){
        while(frequency[i] > 0){
            arr[count++] = i;
            frequency[i]--;
        }
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

    countingSort(arr , n);
    return 0;
}