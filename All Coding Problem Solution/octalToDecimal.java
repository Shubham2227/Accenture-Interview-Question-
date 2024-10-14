Program for Octal to Decimal Conversion

// Java program to convert octal to decimal 
import java.io.*; 

class GFG { 

	// Function to convert octal to decimal 
	static int octalToDecimal(int n) 
	{ 
		int num = n; 
		int dec_value = 0; 

		// Initializing base value to 1, i.e 8^0 
		int base = 1; 

		int temp = num; 
		while (temp > 0) { 
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

	// driver program 
	public static void main(String[] args) 
	{ 
		int num = 67; 
		System.out.println(octalToDecimal(num)); 
	} 
} 

// This code is contributed 
// by Pramod Kumar
