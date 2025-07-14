#include<iostream>
using namespace std;

int main(){
    bool isAdult;
    int age;
    cout << "Enter age : ";
    cin >> age;

    // if(age >= 18){
    //     isAdult = true;
    // }else {
    //     isAdult = false ;
    // }
    // cout << "man is : " << isAdult << endl ; 

    // using ternary operator 

    isAdult = (age >= 18) ? true : false ;

    cout << "man is : " << isAdult << endl ;

    isAdult ? cout << "man is Adult." : cout << "man is not adult.";

    return 0;
}