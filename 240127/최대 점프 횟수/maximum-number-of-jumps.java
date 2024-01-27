import java.util.*;

public class Main {
    public static int n;

    public static int[] dp;

    public static int[] numbers;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        numbers = new int[n + 1];
        dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            numbers[i] = sc.nextInt();
            dp[i] = -1;
        }

        System.out.println(dpf(n));

        // for (int x : dp) {
        //     System.out.print(x + " ");
        // }

    }
    // dpf(n) =  max(ret, dpf(i) where 1 <= i < n and i(현재위치) + numbers[i](점프할 수 있는 길이) >= n(도착점))
    public static int dpf(int n) {
        // 시작점
        if (n == 1) {
            return 0;
        }
        if (dp[n] != -1) {
            return dp[n];
        }

        int ret = dp[n];
        for (int i = 1; i < n; i++) {
            if (i + numbers[i] >= n) {
                ret = Math.max(ret, dpf(i) + 1);
            }
        }
        
        dp[n] = ret;

        return ret;

    }   
}