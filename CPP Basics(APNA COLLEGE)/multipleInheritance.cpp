#include<iostream>
using namespace std;

class Teacher {
public :
    int salary;
    string subject;
};

class Student {
public :
    int rollNO;
    float cgpa;
};

class TA : public Teacher , public Student {
public :
    string name;
};

int main(){
    TA t1 ;
    t1.name = "xyz";
    cout << "name : " << t1.name << endl;
    t1.salary = 15000;
    cout << "salary : " << t1.salary <<  endl;
    t1.subject = "computer science";
    cout << "subject : " << t1.subject << endl;
    t1.cgpa = 9.1;
    cout << "cgpa : " << t1.cgpa << endl;
}