#include<iostream>
using namespace std;

class Example {
public :
    static int x;  // static variable only declare ho sakta h 
    static const int y = 0;
};
// initialize class ke outside hi karna padega
int Example::x = 0;

int main(){
    Example e1;
    Example e2;
    Example e3;
    cout << "e1 = " << e1.x++ << " & " << e1.y << endl;  // 0 & 0
    cout << "e2 = " << e2.x++ << " & " << e2.y << endl;  // 1 & 0
    cout << "e3 = " << e3.x++ << " & " << e3.y << endl;  // 2 & 0
    return 0;
}