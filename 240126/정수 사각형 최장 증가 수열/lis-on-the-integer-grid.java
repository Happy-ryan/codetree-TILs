import java.util.*;

public class Main {
    public static final int INF = 100000000;

    public static int n;
    public static int[][] board;
    public static int[][] dp;

    public static int[] dr = new int[]{-1, 1, 0, 0};
    public static int[] dc = new int[]{0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        board = new int[n][n];
        dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
                dp[i][j] = -1;
            }
        }

        int maxRet = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                maxRet = Math.max(maxRet, dpf(i, j));
            }
        }

        System.out.println(maxRet);

    }

    public static boolean inRange(int r, int c){
        return 0 <= r && r < n && 0 <= c && c < n;
    }

    public static int dpf(int r, int c) {
        if (dp[r][c] != -1) {
            return dp[r][c];
        }

        boolean isStart = true;
        int ret = -INF;
        for (int dir = 0; dir < 4; dir++) {
            int pre_r = r + dr[dir];
            int pre_c = c + dc[dir];
            if (inRange(pre_r, pre_c) && board[r][c] > board[pre_r][pre_c]) {
                isStart = false;
                ret = Math.max(ret, dpf(pre_r, pre_c) + 1);
            }
        }

        if(isStart){
            return 1;
        }

        dp[r][c] = ret;

        return ret;
    }
}