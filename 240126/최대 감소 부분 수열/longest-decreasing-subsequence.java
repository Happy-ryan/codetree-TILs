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
        // 도착점은 여려개!!
        int maxLength = 0;
        for(int endpoint = 0; endpoint < n; endpoint++){
            maxLength = Math.max(maxLength, dpf(endpoint));
        }

        System.out.println(maxLength);
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