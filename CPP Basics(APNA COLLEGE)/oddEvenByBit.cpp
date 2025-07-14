#include<iostream>
using namespace std;

int main(){
    int num;
    cout << "Enter number : ";
    cin >> num;

    num = num & 1;

    if(num){  // num == 0  //  means last bit is 1 i.e. this number is odd
        cout << "number is odd."<<endl;
    }else{  // num == 0   means last bit is 0 i.e. this number is even
        cout << "number is even" << endl;
    }
    return 0;
}