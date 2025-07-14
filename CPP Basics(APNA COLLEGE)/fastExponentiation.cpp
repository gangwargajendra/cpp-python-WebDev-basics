#include<iostream>
using namespace std;

int exponentiation(int num ,int pow){
    int ans = 1;
    while(pow > 0){
        int lastBit = pow & 1 ;
        pow = pow >> 1;
        if(lastBit){
            ans = ans * num;
        }
        num = num * num;
    }
    return ans;
}

int main(){
    int num ,pow;
    cout << "ENter number and power : ";
    cin >> num;
    cin >> pow;

    cout << "answer is : " << exponentiation(num , pow) ; 
    return 0;
}