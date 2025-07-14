#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    float PI = 3.1456161819884;
    double PI2 = 3.1456161819884;
    // without set precision
    cout << "PI = " << PI << endl;
    cout << "PI2 = " << PI2 << endl;
    
    //with set precision
    cout << setprecision(20) << "PI = "  << PI << endl;
    cout << setprecision(20) << "Pi2 = " << PI2 << endl;

    return 0;
}