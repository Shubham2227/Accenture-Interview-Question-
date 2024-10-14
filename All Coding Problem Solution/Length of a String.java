Write a program to calculate the length of a string without
using the strlen() function.

import java.util.Scanner;
public class Main {
    public static int lengthOfString(String str) {
        int cnt = 0;
        for (char ch : str.toCharArray()) {
            cnt++;
        }
        return cnt;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String string = scanner.nextLine(); // shubham
        System.out.println(lengthOfString(string)); // Output: 7
    }
}
