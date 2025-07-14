#include<iostream>
using namespace std;

class Parent {
public : 
    void show(){
        cout << "inside parent class..\n";
    }
    virtual void hello (){
        cout << "inside parent hello..\n";
    }
};

class Child : public Parent {
public:
    void hello() {
        cout << "inside child class..\n";
    }
};


int main(){
    Child c1;
    Parent *p2;
    p2 = &c1;    // Run time binding or late binding 
    p2->hello();
    p2->show();

    // c1.hello();
    // c1.show();

    // Parent p1;
    // p1.hello();
    // p1.show();
}