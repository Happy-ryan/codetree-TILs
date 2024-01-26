import java.util.*;

public class Main {
    public static int n;

    public static int[] numbers;
    public static int[] dp;

    public static void main(String[] args) {
        // 최대 증가 부분 수열 > 대표적인 DP유형
        // 조건에 맞게 선택적으로 전진하는 DP
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        numbers = new int[n];
        dp = new int[n]; // 최소는 1이므로 0도 상관없음!
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }
        //  도착점은 다양할 수 있다!!!
        int maxLength = 0;
        for(int i = 0; i < n; i++){
            maxLength = Math.max(maxLength, dpf(i));
        }
        System.out.println(maxLength);

    }
    // dpf(x): 시작부터 도착점 - 인덱스(x - 1)일 때까지의 최대 증가 부분 수열
    // dpf(x) = max(ret, dpf(y) where (0 <= y < x) and (numbers[y] < numbers[x]) + 1)
    public static int dpf(int x) {

        if (dp[x] != 0) {
            return dp[x];
        }
        //  x가 시작점이 될 수 있는가?
        //  시작점이 되기위해서는 나보다 작은 놈이 있으면 안돼!
        boolean isXStartPoint = true;
        int ret = 0;
        for (int y = 0; y < x; y++) {
            if (numbers[y] < numbers[x]) {
                // 나보다 작은 놈이 있네? 그러면 시작점은 아니야!!
                ret = Math.max(ret, dpf(y) + 1);
                isXStartPoint = false;
            }
        }
        // 시작점의 길이는 1이다.
        if (isXStartPoint) {
            return 1;
        }

        dp[x] = ret;

        return ret;
    }
}