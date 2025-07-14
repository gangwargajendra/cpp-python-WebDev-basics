#include<iostream>
using namespace std;

int sum(int a = 1 ,int b){  // isme b as a default paremeter bna diya h
    return (a + b);
}

int main(){
    int s = sum(2,3); //is case mai a = 2 and b = 3 
    cout << "sum = " << s << endl;

    s = sum(2); // is case mai a = 2 , b = 1 ho jayega 
    cout << "sum = " << s << endl;

    s = sum(); // is case mai a = 2 , b = 1 ho jayega 
    cout << "sum = " << s << endl;
    return 0;
}