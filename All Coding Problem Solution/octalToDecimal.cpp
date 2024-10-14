Program for Octal to Decimal Conversion

// C++ program to convert octal to decimal 
#include <iostream> 
using namespace std; 

// Function to convert octal to decimal 
int octalToDecimal(int n) 
{ 
	int num = n; 
	int dec_value = 0; 

	// Initializing base value to 1, i.e 8^0 
	int base = 1; 

	int temp = num; 
	while (temp) { 

		// Extracting last digit 
		int last_digit = temp % 10; 
		temp = temp / 10; 

		// Multiplying last digit with appropriate 
		// base value and adding it to dec_value 
		dec_value += last_digit * base; 

		base = base * 8; 
	} 

	return dec_value; 
} 

// Driver program to test above function 
int main() 
{ 
	int num = 67; 

	cout << octalToDecimal(num) << endl; 
}
