#include<iostream>
#include <string>
using namespace std;

class car {
    string colour;
    int model;

    public: 
        car(){
            cout << "constructor without parameter.\n";
        }
    // By making new variables
        // car(string newColour,int newModel){
        //     colour = newColour;
        //     model = newModel;
        // }
    // without making new variables [by this keyword]
        car(string colour ,int model){
            //this->colour = colour;
             (  *this).colour = colour;
            //this->model = model;
            (*this).model = model;
        }
        void start(){
            cout << "car has started..\n";
        }
        void setColour(string colour){
            this->colour = colour;
        }
        void stop(){
            cout << "car has stopped..\n";
        }
        string getColour(){
            return colour;
        }
        int getModel(){
            return model;
        }
};

int main(){
    car c0;    // made by non-parameterised constructor
    c0.setColour("green");
    cout << "colour : " << c0.getColour() << endl;

    car c1("blue" , 2015); // made by parameterised constructor
    cout <<"colour : " << c1.getColour();
    cout << ", Model : " << c1.getModel() << endl;

    car c2("pink",2016);
    cout <<"colour : " << c2.getColour();
    cout << ", Model : " << c2.getModel() << endl;
    return 0;
}