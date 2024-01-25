import java.util.*;

public class Main {
    public static int n;
    public static int[][] board, dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        board = new int[n + 1][n + 1];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = sc.nextInt();
            }
        }

        dp = new int[n + 1][n + 1];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i == 0){
                    if(j == 0){
                        dp[i][j] = board[i][j];
                    }
                    else{
                        dp[i][j] = board[i][j] + dp[i][j - 1];
                    }
                }
                else{
                    if(j == 0){
                        dp[i][j] = dp[i - 1][j] + board[i][j];
                    }
                    else{
                        dp[i][j] = board[i][j] + Math.max(dp[i - 1][j], dp[i][j - 1]);
                    }
                }
            }
        }

        System.out.println(dp[n-1][n-1]);

    }
}