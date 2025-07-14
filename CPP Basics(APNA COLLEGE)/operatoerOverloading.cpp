#include<iostream>
using namespace std;

class Complex {
    int real;
    int img;
public: 
    Complex(){
        cout <<"created...\n";
    }
    Complex(int real ,int img){
        this->real = real;
        this->img = img;
    }
    void showComplex(){
        cout << "number : " << real << " + " << img << "i" << endl;
    }
    // operator overloading
    Complex operator + (Complex &ob){  // kisi ek ko by reference send karna hota h
        Complex c3;
        c3.real = this->real + ob.real;
        c3.img = this->img + ob.img;
        return c3;
    }
};

int main(){
    Complex c1(4,5);
    Complex c2(5,4);
    c1.showComplex();
    c2.showComplex();

    Complex c3 = c2 + c1;
    c3.showComplex();
    return 0;
}