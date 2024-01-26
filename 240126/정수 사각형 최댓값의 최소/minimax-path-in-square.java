import java.util.*;

public class Main {
    public static int n;
    public static int[][] board;

    public static int[][] dp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        board = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = sc.nextInt();
            }
        }

        dp = new int[n + 1][n + 1];
        System.out.println(dpf(n - 1, n - 1));
    }
    public static boolean inRange(int r, int c){
        return 0 <= r && r < n && 0 <= c && c < n;
    }
    //  dpf(r, c) = 출발점(0, 0)에서 도착점(r, c) 거쳐간 숫자의 최대값 중 최소값!
    // dpf(r, c) = max(dpf(r, c), min(dpf(r - 1, c), board[r][c]))
    public static int dpf(int r, int c) {
        if (dp[r][c] != 0) {
            return dp[r][c];
        }

        if (!inRange(r - 1, c) && !inRange(r, c - 1)) {
            return board[r][c];
        }

        // 최대값의 최소값 ...  min(max(xx))
        int ret = 1000001;
        if (inRange(r - 1, c)){
            ret = Math.min(ret, Math.max(dpf(r - 1, c), board[r][c]));
        }
        if (inRange(r, c - 1)){
            ret = Math.min(ret, Math.max(board[r][c], dpf(r, c - 1)));
        }

        dp[r][c] = ret;

        return ret;
    }
}