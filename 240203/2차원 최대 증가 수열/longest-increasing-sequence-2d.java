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

        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++) {
        //         dpf(i, j);
        //         System.out.println("i: " + i + "j " + j);
        //         for (int r = 0; r < n; r ++) {
        //             for (int c = 0; c < m; c++) {
        //                 System.out.print(dp[r][c] + " ");
        //             }
        //             System.out.println();
        //             System.out.println("=");

        //         }
        //     }
        // }
        // System.out.println(dpf(3, 2));      
        int maxAnswer = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                maxAnswer = Math.max(dpf(i, j), maxAnswer);
                // System.out.print(dp[i][j] + " ");
            }
            // System.out.println();
        }


        System.out.print(maxAnswer);
    } 
    // dpf(r, c) = (0, 0) ~ (r, c) 도착할 때까지의 최대 칸의 수 if value > 0
    //           = 0 if impossible
    // dpf(r, c) = max(dpf(preR, preC) + 1, ret) where 0 <= preR < R and 0 <= preC < c 
    // and board[preR][preC] < board[r][c] 
    // and dpf(preR, preC) > 0
    // 시작점이 board[0][0]보다는 무조건 커야함!
    // 틀린 이유? 0이라는 값을 불가능 하다고 처리했는데, +1로 수가 되어버린것
    // dpf(r, c) == 0: 도착 불가

    private static int dpf(int r, int c) {
        if (dp[r][c] != -1) {
            return dp[r][c];
        }
        // 최소 1개? 0개?
        int ret = 0;
        for (int preR = 0; preR < r; preR++) {
            for (int preC = 0; preC < c; preC++) {
                if (board[preR][preC] < board[r][c]) {
                    if (dpf(preR, preC) == 0)
                        continue;
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