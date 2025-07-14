#include<iostream>
using namespace std;

class Animal {
public : 
    void breathe(){
        cout << "breathe..\n";
    }
};

class Mammal : public Animal{
public :
    void bloodtype(){
        cout << "bloodtype : warm" <<endl;
    }
};

class Dog : public Mammal{
public :
    void tail(){
        cout << "having tail.."<< endl;
    }
};

int main(){
    Dog d1;
    d1.breathe();
    d1.bloodtype();
    d1.tail();

    Mammal m1;
    m1.breathe();
    m1.bloodtype();

    Animal a1;
    a1.breathe();
    return 0;
}