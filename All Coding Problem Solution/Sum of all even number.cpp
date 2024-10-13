Wrire a program find the sum of all even number in given array 

#include <iostream>
using namespace std;
int even(int arr[], int n) {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 == 0) {
            ans += arr[i];
        }
    }
    return ans;
}
int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};  
    int n = sizeof(arr) / sizeof(arr[0]); 
    cout << even(arr, n) << endl; 
    return 0;
}
