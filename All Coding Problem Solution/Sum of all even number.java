write a program to find the sum of all even number in given array 

public class Main {
    public static int even(int[] arr, int n) {
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 == 0) {
                ans += arr[i];
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8}; 
        int n = arr.length;  /
        System.out.println(even(arr, n)); 
    }
}
