import java.util.*;

public class Main {
    public static int n;

    public static int[][] board;
    public static int[][] dp;

    public static int[] dr = new int[]{-1, 0};
    public static int[] dc = new int[]{0, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        board = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = sc.nextInt();
            }
        }

        dp = new int[n][n];
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

        boolean isStartPoint = true;
        
        int ret = 1000001;
        for (int d = 0; d < 2; d++) {
            int pre_r = r + dr[d];
            int pre_c = c + dc[d];
            if (inRange(pre_r, pre_c)) {
                ret = Math.min(ret, Math.max(dpf(pre_r, pre_c), board[r][c]));
                isStartPoint = false;
            }
        }

        if (isStartPoint) {
            return board[r][c];
        }

        dp[r][c] = ret;

        return ret;
    }
}