#include<iostream>
using namespace std;

class Example {
public:
    Example (){
        cout << "constructor ..\n";
    }

    ~Example(){
        cout << "destructor ..\n";
    }
};

int main(){
    int a = 0;
    if(a == 0){
        // Example eg1; // eg1 ka scope if ki curly bracket tak hona chahiye
        static Example eg1; // iska scope code ki ending tak hona chahiye
    }
    cout << "code ending...\n";
    return 0;
}