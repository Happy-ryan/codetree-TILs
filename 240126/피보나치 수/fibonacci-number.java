import java.util.*;

public class Main {
    public static int[] dp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        dp = new int[n + 1];
        // dpf(n) = dpf(n - 1) + dpf(n - 2)
        System.out.println(dpf(n));
    }

    public static int dpf(int n){
        if(dp[n] != 0){
            return dp[n];
        }

        // indegree 0
        if (n == 1 ||  n == 2) {
            return 1;
        }

        int ret = dpf(n -1) + dpf(n - 2);

        dp[n] = ret;

        return ret;
    }
}