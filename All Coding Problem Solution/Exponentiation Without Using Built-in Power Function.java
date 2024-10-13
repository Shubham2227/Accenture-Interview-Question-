import java.util.Scanner;

public class Main {
    
    // Function to calculate a^b without using built-in power functions
    public static int exponent(int a, int b) {
        int ans = 1;
        for (int i = 1; i <= b; i++) {
            ans *= a;
        }
        return ans;
    }

    public static void main(String[] args) {
        // Creating a Scanner object for input
        Scanner sc = new Scanner(System.in);
        
        // Input the base
        System.out.print("Enter the base (a): ");
        int a = sc.nextInt();
        
        // Input the exponent
        System.out.print("Enter the exponent (b): ");
        int b = sc.nextInt();
        
        // Calling the exponent function and storing the result
        int result = exponent(a, b);
        
        // Output the result
        System.out.println(a + " raised to the power of " + b + " is: " + result);
        
        sc.close();
    }
}
