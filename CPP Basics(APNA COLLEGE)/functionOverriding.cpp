#include<iostream>
using namespace std;

class Parent {
public :
    void callParent(){
        cout << "parent function is calling..\n";
    }
};

class Child : public Parent {
public:
    void callParent(){
        cout << "child function is calling..\n";
    }
};

int main(){
    Child c1;
    c1.callParent();
    return 0;
}