#include<iostream>
#include<string>
using namespace std;

class Animal {
protected :
    string colour;
    void eat(){
        cout << "eats..\n";
    }
public :
    void breathe(){
        cout << "breathes..\n";
    }
};

class Fish : protected Animal{
public :
    int fins;
    void swim(){
        cout << "swim..\n";
    }
    void geteat(){
        cout << "can eat .. \n";
    }
};

int main(){
    Fish f1;
    f1.fins = 3;
    cout << "fins : " << f1.fins << endl;
    f1.geteat();
    f1.swim();
    // f1.breathe();
}