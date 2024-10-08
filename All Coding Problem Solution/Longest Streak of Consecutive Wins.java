You are developing a feature for a mobile game that tracks player performance. The agame records the results of consecutive rounds as a binary array A,
where 1 indicates a win and 0 indicates a loss. The game developers want to analyze how well players are doing by determining the longest streak of consecutive wins.
Your task is to find and a300 retur an integer value representing the count of the maximum number of consecutive
1s (wins) in the array.
Input Specification:
input1: A binary integer array A representing the game records. input2: An integer value representing the number of games played.
Output Specification:
Return an integer value representing the count of the maximum number of consecutive 1s (wins) in the array.
Example 1:
input1: (1,1,0,1,1,1)
input2 : 6


public class MaxConsecutiveOnes {
    public static int maxConsecutiveOnes(int[] A, int n) {
        int maxCount = 0;
        int currentCount = 0;

        for (int i = 0; i < n; i++) {
            if (A[i] == 1) {
                currentCount++;
            } else {
                currentCount = 0;
            }
            maxCount = Math.max(maxCount, currentCount);
        }

        return maxCount;
    }

    public static void main(String[] args) {
        int[] A = {1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1};
        int n = 14;
        System.out.println(maxConsecutiveOnes(A, n));  // Output: 4
    }
}
