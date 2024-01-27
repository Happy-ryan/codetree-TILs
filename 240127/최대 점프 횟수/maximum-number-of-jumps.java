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
        int maxVal = 0;
        for(int i = 1; i <= n; i++){
            maxVal = Math.max(maxVal, dpf(i));
        }
        System.out.println(maxVal);

    }
    // dpf(x) =  max(ret, dpf(i) where 1 <= i < x and i(현재위치) + numbers[i](점프할 수 있는 길이) >= n(도착점))
    // 시작점이 고정된 문제..
    public static int dpf(int x) {
        if (dp[x] != -1) {
            return dp[x];
        }

        if (x == 1) {
            return 0;
        }

        int ret = -10000000;
        for (int start = 0; start < x; start++) {
            if (start + numbers[start] >= x) {
                ret = Math.max(ret, dpf(start) + 1);
            }
        }

        dp[x] = ret;

        return ret;
    }
}