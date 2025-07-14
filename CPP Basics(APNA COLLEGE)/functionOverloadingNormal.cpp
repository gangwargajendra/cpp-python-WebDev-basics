#include<iostream>
using namespace std;

int sum(int a , int b){
    cout << (a + b) << endl ;
    return (a + b);
}

// on the basis of data type 

double sum(double a , double b){
    cout << (a + b) << endl ;
    return (a + b );
}

// on the basis of no of parameter

int sum(int a ,int b ,int c){
    cout << (a + b + c) << endl;
    return (a + b + c);
}

int main(){
    //int sum(int a ,int b);
    sum(2 , 3);
    // doubl sum(double a ,double b);
    sum(2.5 , 4.5);
    // int sum(int a , int b ,int c);
    sum(1 , 2 , 3);
    return 0;
}