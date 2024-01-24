import java.util.*;
import java.io.*;

class Pair{
    int x, y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    // 전역변수 선언
    public static int n, k;
    public static int[][] board;
    // bfs에 필요한 변수
    public static boolean[][] inQueue;
    public static Queue<Pair> bfsQ = new LinkedList<>();
    //
    public static int cnt = 0;
    //
    public static boolean inRange(int r, int c){
        return 0 <= r && r < n && 0 <= c && c < n && board[r][c] == 0 && !inQueue[r][c];
    }
    // 출발점이 2개이상인 bfs
    public static int BFS(){
        int[] dr = new int[]{1, -1, 0, 0};
        int[] dc = new int[]{0, 0, 1, -1};
        // queue가 0이 될 때까지 반복
        while(!bfsQ.isEmpty()){
            Pair curPos = bfsQ.poll();
            int cr = curPos.x;
            int cc = curPos.y;
            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if (inRange(nr, nc)){
                    bfsQ.add(new Pair(nr, nc));
                    inQueue[nr][nc] = true;
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer inputNK = new StringTokenizer(br.readLine());

        n = Integer.parseInt(inputNK.nextToken());
        k = Integer.parseInt(inputNK.nextToken());


        board = new int[n + 1][n + 1];
        inQueue = new boolean[n + 1][n + 1];
        
        for(int i = 0; i < n; i++){
            StringTokenizer row = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                board[i][j] = Integer.parseInt(row.nextToken());
            }
        }

        for(int i = 0; i < k; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            bfsQ.add(new Pair(r - 1, c - 1));
            inQueue[r - 1][c - 1] = true;
            cnt++;
        }

        System.out.println(BFS());
    }
}