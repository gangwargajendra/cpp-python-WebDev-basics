#include<iostream>
#include<string>
using namespace std;

bool validAnagram(string str1, string str2){
    if(str1.length() != str2.length()){ // if length will not be equal then it can not be a anagram
        return false;
    }
    int arr[26] = {0};
    for(char ch : str1){
        arr[ch - 'a']++;
    } 
    for(char ch : str2){
        if(arr[ch -'a'] == 0){
            return false;
        }
        arr[ch - 'a']--;
    }
    return true;
}

int main(){
    string str1;
    string str2;
    cout << "Enter first word : " ;
    getline(cin , str1);
    cout << "Enter second word : " ;
    getline(cin ,str2);

    if(validAnagram(str1 ,str2)){
        cout << "valid anagram ";
    }else {
        cout << "not valid anagram"; 
    }
    return 0;
}