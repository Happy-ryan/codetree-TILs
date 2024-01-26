import java.util.*;

public class Main {
    public static int n;

    public static int[] dp;
    public static int[] numbers;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        numbers = new int[n];
        dp = new int[n];
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            numbers[i] = x;
            dp[i] = -1;
        }

        System.out.println(dpf(n - 1));
    }
    // max: 최대 길이를 구하므로
    // dpf(x) = max(ret, dpf(y) where 0 <= y < x and numbers[y] > numbers[x] + 1)
    public static int dpf(int x) {
        if (dp[x] != -1) {
            return dp[x];
        }
        //  x가 스타트가 될 수 있냐?
        //  x보다 큰 놈이 존재해서는 안된다!
        boolean isStartPoint = true;
        int ret = 0;
        for (int y = 0; y < x; y++) {
            if (numbers[x] < numbers[y]) {
                isStartPoint = false;
                ret = Math.max(ret, dpf(y) + 1);
            }
        }

        if (isStartPoint) {
            return 1;
        }

        dp[x] = ret;

        return ret;
    }
}