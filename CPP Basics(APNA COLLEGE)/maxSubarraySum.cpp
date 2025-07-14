#include<iostream>
using namespace std;

// // by using Brute force approach . time complexity = O(n^3)
// int maxSubarraySum(int *arr ,int n){
//     int maxSum = INT8_MIN;
//     for(int start = 0 ; start < n ; start++){
//         for(int end = start ; end < n ; end++){
//             int currentSum = 0;
//             for(int i = start ; i <= end ; i++){
//                 currentSum += arr[i];
//             }
//             cout << currentSum << ",";
//             maxSum = max(currentSum , maxSum);  // a header file .it's return maximum of two numnbers
//         }
//     }
//     cout << "\nmaximum subarray sum : " << maxSum << endl;
//     return maxSum;
// }

// // by using Brute force approach in optimise way. time complexity = O(n^2)
// int maxSubarraySum(int *arr ,int n){
//     int maxSum = INT8_MIN;
//     for(int start = 0 ; start < n ; start++){
//         int previousSum = 0;
//         for(int end = start ; end < n ; end++){ // here we are not running loop again and again from a starting index. 
//             previousSum += arr[end];
//             cout << previousSum << " ,";
//             maxSum = max(maxSum , previousSum); // header file. it's gives maximum of two numbers. 
//         }
//     }
//     cout << "\nmaximum subarray sum : " << maxSum << endl;
//     return maxSum;
// }

// by using Kadane's algorithm. time complexity = O(n)
int maxSubarraySum(int *arr, int n){
    int currentSum = 0;
    int maxSum = INT8_MIN;
    for(int i = 0; i < n ; i++){
        currentSum += arr[i];
        maxSum = max(maxSum ,currentSum);
        if(currentSum < 0){
            currentSum = 0;
        }
    }
    cout << maxSum << endl;
    return maxSum;
}

int main(){
    int n;
    cout<<"Enter size of array : ";
    cin >> n;
    int arr[n];

    cout << "Enter " << n << " elements of array : ";
    for(int i = 0; i < n ; i++){
        cin >> arr[i];
    }

    int maxSum = maxSubarraySum(arr, n);
    cout << "maximum sum of an subarray : " << maxSum << endl;
    return 0;
}