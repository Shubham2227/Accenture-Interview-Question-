#include <iostream>
using namespace std;
    int ans = 1;
    for (int i = 1; i <= b; i++) {
        ans *= a;
    }
    return ans;
}
int main() {
    int a, b;

    cout << "Enter the base (a): ";
    cin >> a;
    cout << "Enter the exponent (b): ";
    cin >> b;
    int result = exponent(a, b);
    cout << a << " raised to the power of " << b << " is: " << result << endl;

    return 0;
}
