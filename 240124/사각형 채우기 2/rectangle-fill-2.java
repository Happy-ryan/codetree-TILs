import java.util.*;

public class Main {
    public static int MOD = 10007;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] dp = new int[n + 1];

        if (n == 1){
            System.out.println(1);
        }else if(n == 2){
            System.out.println(3);
        }
        else{
            dp[1] = 1;
            dp[2] = 3;
            for(int i = 3; i <= n; i++){
                dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD;
            }
            System.out.println(dp[n]);
        }
    }
}