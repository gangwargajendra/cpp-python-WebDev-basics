#include<iostream>
using namespace std;

int trapWater(int *height ,int n){
    int leftLargest[n];
    int rightLargest[n];
    leftLargest[0] = 0;
    rightLargest[n-1] = 0;

    for(int i = 1 ; i < n ; i++){
        leftLargest[i] = max(leftLargest[i-1] , height[i-1]);
        rightLargest[n-i-1] = max(rightLargest[n-i] , height[n-i]);
    }
    
    // for(int i = 0 ; i < n ; i++){
    //     cout << height[i] <<" left Largest : " << leftLargest[i] << " , right Largest : " << rightLargest[i] <<endl;
    // }

    int filledWater = 0;

    for(int i = 0 ; i < n ; i++){   // also we can ignore for index 0 and n-1 means for(i=1 ; i<n-1 ;i++)
            int filledAtIindex = min(leftLargest[i] , rightLargest[i]) - height[i];
            if(filledAtIindex > 0){
                filledWater += filledAtIindex;
            }
    }

    cout << "ammount of water trapped : " << filledWater << endl;
    return filledWater;
}

int main(){
    int n;
    cout<< "Enter the size of array : ";
    cin >> n;

    int height[n];
    cout << "Enter " << n << " elements of : ";
    for(int i = 0; i < n ; i++){
        cin >> height[i];
    }

    int trappedWater = trapWater(height , n);
    cout << "ammount of water trapped : "<<trappedWater << endl;
    return 0;
}