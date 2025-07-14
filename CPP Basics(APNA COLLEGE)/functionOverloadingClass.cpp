#include<iostream>
using namespace std;

class Print {
public: 
    void print(int x){
        cout << "integer is : " << x << endl;
    }
    void print(float x){
        cout << "float is : " << x << endl;
    }
    void print(double x){
        cout << "double is : " << x << endl;
    }
};

int main(){
    Print p1;
    p1.print(1);
    p1.print((float)3.6);
    p1.print(2.5);
    return 0;
}