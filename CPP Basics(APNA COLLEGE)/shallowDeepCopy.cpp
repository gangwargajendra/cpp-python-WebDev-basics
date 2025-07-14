#include<iostream>
#include<string>
using namespace std;

class Car {
    public :
        string name;
        string colour;
        int *model;

        Car (string name ,string colour ,int mod){
            this->name = name;
            this->colour = colour;
            model = new int;
            *model = mod;
        }

        Car(Car &original){
            cout << "copying original to new..\n";
            name = original.name;
            colour = original.colour;
            // // for shallow copy
            // model = original.model;
            // for deep copy
            model = new int;
            *model = *original.model;
        }

        ~Car (){
            cout <<"deleting memory.."<< endl; // static memory apne aap free ho jati h
            if(model != NULL){
                delete model;
                model = NULL;
            }
        }
};

int main(){
    Car c1("maruti" , "white" , 2016);

    Car c2(c1);
    cout << "name : " << c2.name << endl;
    cout << "colour : " << c2.colour << endl;
    cout << "model by c2 : " << *c2.model << endl;
    cout << "model by c1 : " << *c1.model << endl;

    *c2.model = 2015;
    
    cout << "model by c2 : " << *c2.model << endl;
    cout << "model by c1 : " << *c1.model << endl;
    return 0;
}