import java.util.Scanner;

public class Main {

    private static int n, m;
    private static int[][] board, dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();


        board = new int[n][m];
        dp = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = sc.nextInt();
                dp[i][j] = -1;
            }
        }

        int maxAnswer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                maxAnswer = Math.max(dpf(i, j), maxAnswer);
            }
        }

        System.out.print(maxAnswer);

        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++) {
        //         System.out.print(dp[i][j] + " ");
        //     }
        //     System.out.println();
        // }


    } 
    // dpf(r, c) = (0, 0) ~ (r, c) 도착할 때까지의 최대 칸의 수
    // dpf(r, c) = max(dpf(preR, preC) + 1, ret) where 0 <= preR < R and 0 <= preC < c 
    // and board[preR][preC] < board[r][c]
    private static int dpf(int r, int c) {
        if (dp[r][c] != -1) {
            return dp[r][c];
        }
        // 최소는 1이다.
        int ret = 0;
        for (int preR = 0; preR < r; preR++) {
            for (int preC = 0; preC < c; preC++) {
                if (board[preR][preC] < board[r][c]){
                    ret = Math.max(dpf(preR, preC) + 1, ret);
                }
            }
        }


        if (r == 0 && c == 0) {
            return 1;
        }


        dp[r][c] = ret;
        return ret;
    }
}