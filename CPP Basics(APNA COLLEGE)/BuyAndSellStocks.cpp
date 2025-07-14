#include<iostream>
using namespace std;

int maxProfit1(int *prices ,int n){  // it is done by in time complexity = O(n^2)
    int maxProfit = INT8_MIN;
    int currentProfit = 0;
    for(int i = 0; i < n ; i++){
        for(int j = i+1 ; j < n ; j++){
            currentProfit = prices[j] - prices[i];
            maxProfit = max(maxProfit , currentProfit);
        }
    }
    return (maxProfit < 0) ? -1 : maxProfit;
}

int maxProfit2(int *prices ,int n){
    int bestbuyday[n];   // it will store best buy day of stock for each day.
    bestbuyday[0] = INT8_MAX;
    for(int i = 1 ; i < n ; i++){
        bestbuyday[i] = min(prices[i-1] , bestbuyday[i-1]);
    }
    int maxProfit = 0;
    int currentProfit;
    for(int i = 0 ; i < n ; i++){
        currentProfit = prices[i] - bestbuyday[i];   // profit = sell - buy
        maxProfit = max(currentProfit ,maxProfit);
    }
    cout << "maximum profit = " << maxProfit << endl;
    return maxProfit;
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

    int maxProfit = maxProfit2(arr , n);
    cout << "maximum profit : " << maxProfit <<endl;
    return 0;
}