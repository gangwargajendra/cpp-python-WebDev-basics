#include<iostream>
#include<string>
using namespace std;

class Car {
    public :
        string name;
        string colour;

        Car(string name ,string colour){  // parametrised constructor
            this->name = name;
            this->colour = colour;
        }

        Car (Car &orgin){    // copy constructor
            cout <<"in copy constructor" << endl ;
            name = orgin.name;
            colour = orgin.colour;  
        }
};

int main(){
    Car c1("maruti" , "white");

    Car c2(c1);
    cout <<"car name of c2 : " << c2.name << endl;
    cout << "car colour of c2 : " << c2.colour <<  endl;
    return 0;
}