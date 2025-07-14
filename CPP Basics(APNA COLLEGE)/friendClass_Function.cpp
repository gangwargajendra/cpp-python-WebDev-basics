#include<iostream>
#include<string>
using namespace std;

class Father {
    friend class Friend;
    friend void revealSecret(Father &obj);
    string secret = "secret data";
};
// friend ke pass father ke data ki access hogi but friend ke pass Father ke data ki access nhi hogi
class Friend {  // it became friend class of Father
public:
    void showSecret (Father &obj){ 
        cout << "secret data inside class : " << obj.secret << endl;
    }
};

void revealSecret(Father &obj){  // friend function
    cout << "secret data inside function : " << obj.secret << endl;
}

int main(){
    Father fa1;
    Friend fr1;
    fr1.showSecret(fa1);
    revealSecret(fa1);
}