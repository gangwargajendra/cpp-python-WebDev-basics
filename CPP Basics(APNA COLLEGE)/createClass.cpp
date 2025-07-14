#include<iostream>
#include<string>
using namespace std;

class Student {
    // private:  // by default these properties will save private
        float cgpa;
        string name;
    public:
        void getPersentage(){
            cout << "parcentage : " << (cgpa * 10) << "% \n";
        }
        //setters
        void setCgpa(float newCgpa){   
            cgpa = newCgpa;
            cout << "cgpa : " << cgpa << endl;
        }

        void setName(string newName){
            name = newName;
            cout << "name : " << name << endl;
        }
        // getters
        float getCgpa(){
            return cgpa;
        }
        string getName(){
            return name;
        }

};

int main(){
    Student s1;  // s1 is object
    s1.setCgpa(8.4) ;
    s1.setName("Gajendra");

    cout << "cgpa : " << s1.getCgpa() << endl;
    cout << "name : " << s1.getName() << endl;
    s1.getPersentage();

    return 0;
}