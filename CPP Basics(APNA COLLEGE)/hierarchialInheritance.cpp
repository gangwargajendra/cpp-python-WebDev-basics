#include<iostream>
using namespace std;

class Animal {
public: 
    void eat(){
        cout << "eat..\n";
    }
    void breathe(){
        cout <<"breathe..\n";
    }
};

class Bird : public Animal {
public:
    void fly(){
        cout <<"fly..\n";
    }
};

class Fish : public Animal {
public : 
    void swim(){
        cout<< "swim..\n";
    }
};

int main(){
    Fish f1;
    f1.breathe();
    f1.eat();
    f1.swim();

    Bird b1;
    b1.breathe();
    b1.eat();
    b1.fly();
    return 0; 
}