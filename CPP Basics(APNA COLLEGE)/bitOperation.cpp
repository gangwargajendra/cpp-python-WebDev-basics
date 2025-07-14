#include<iostream>
using namespace std;

int getIthBit(int num , int pos){
    int bitMask = 1 << pos;
    num = num & bitMask;
    if(num){
        return 1;
    }else {
        return 0;;
    }
    return -1; // mje ke liye
}

void setIthBit(int num ,int pos){
    int bitMask = 1 << pos;
    // return num | bitmask;   // if you want to return new number.
    num = num | bitMask;
    cout << "new number : " << num << endl; 
}

void clearIthBit(int num ,int pos){
    int bitMask =  ~(1 << pos);
    // return num | bitmask;   // if you want to return new number.
    num = num & bitMask;
    cout << "new number : " << num << endl;  
}

void cheak2Power(int num){
    if( !( num & (num-1) )) {  // this will give 0 if num is power of 2
        cout << "it's a power of 2 ." << endl;
    }else{
        cout << "it's not a power of 2." << endl;
    }
}

void updateIthBit(int num, int pos, int val){
    // first clear pos bit
    int bitMask = ~(1 << pos);
    num = num & bitMask;
    // second set that bit
    num = num | (val << pos);
    
    cout << "final number : " << num << endl;
}

void clearLastIBits(int num ,int i){
    int bitMask = (~0) << i ; // ~0 will make all bits 1 and left shift will make last i bits 0.
    num = num & bitMask;
    cout << "final number : " << num << endl;
}

void countSetBits(int num){
    int count = 0;
    while(num > 0){
        //int lastBits = num & 1;
        count += (num & 1); 
        num = num >> 1;
    }
    cout << "no of set bits : " << count << endl;
}

int main(){

    // cout << "bit = " << getIthBit(6 ,2) << endl;
    // cout << "bit = " << getIthBit(6 ,4) << endl;

    // clearIthBit(6 , 1);
    // clearIthBit (5 , 0);
    
    // cheak2Power(16);
    // cheak2Power(8);
    // cheak2Power(1);
    // cheak2Power(0);
    // cheak2Power(3);

    // updateIthBit(6 , 1 ,0);
    // updateIthBit(6 , 0 ,1);
    // updateIthBit(6 ,2 ,0);
    // updateIthBit(6 , 2, 1);
    // updateIthBit(6 , 3,1);

    // clearLastIBits(15 , 2);
    // clearLastIBits(6 , 2);
    // clearLastIBits(6 ,3);

    countSetBits(6);
    countSetBits(15);
    countSetBits(-1);
    countSetBits(2);
    return 0;
}