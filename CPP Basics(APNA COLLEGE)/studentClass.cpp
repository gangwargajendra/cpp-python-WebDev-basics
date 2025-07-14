#include<iostream>
#include<string>
using namespace std;

class Student {
        // private :
        int Id;
        string password;
    public :
        string userName;
        Student(int Id){
            this->Id = Id; 
        }
        void setPassword(string password){
            this->password = password;
        }
        string getPassword(){
            return password;
        }
};

int main(){
    Student user1(2301081);
    user1.userName = "raj dhawaniya";
    cout << "username : " << user1.userName << endl;
    user1.setPassword("poi123");
    cout << "password : " << user1.getPassword() << endl;
    return 0;
}