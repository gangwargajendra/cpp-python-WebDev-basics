#include<iostream>
#include<vector>
using namespace std;

vector<int> pairSum(vector<int> arr , int target){
    int st = 0 , end = arr.size() - 1 ;
    vector<int> ans;
    int currentSum = 0;
    while(st < end){
        currentSum = arr[st] + arr[end];
        if(target == currentSum){
            ans.push_back(st);
            ans.push_back(end);
            break;
        }else if(target > currentSum){
            st++;
        }else{
            end--;
        }
    }
    return ans;
}

int main(){
    vector<int> vec ;
    int size;
    cout << "Enter size of array : " ;
    cin >> size;
    cout << "Enter " << size << " element : ";
    for(int i = 0 ; i < size ; i++){
        int t;
        cin>>t;
        vec.push_back(t);
    }

    int target;
    cout << "Enter target value : ";
    cin >> target;

    vector<int> ansArr = pairSum(vec , target);
    cout << "indices are : " << ansArr[0] << " & " << ansArr[1] ;
    return 0;
}