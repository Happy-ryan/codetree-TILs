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
    //
    public static final int MAX_STONE = 8;
    //
    public static int n, k, m;
    public static int[][] board;
    // bfs
    public static Queue<Pair> bfsQ = new LinkedList<>();
    public static List<Pair> starts = new ArrayList<>();
    // 조합
    public static List<Pair> stonPos;
    public static List<Pair> ans = new ArrayList<>();
    public static int[] used = new int[MAX_STONE];
    //
    public static int maxValue = 0;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer inputNKM = new StringTokenizer(br.readLine());

        n = Integer.parseInt(inputNKM.nextToken());
        k = Integer.parseInt(inputNKM.nextToken());
        m = Integer.parseInt(inputNKM.nextToken());

        board = new int[n + 1][n + 1];

        for(int i = 0; i < n; i++){
            StringTokenizer row = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                board[i][j] = Integer.parseInt(row.nextToken());
            }
        }

        for(int i = 0; i < k; i++){
            StringTokenizer inputPos = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(inputPos.nextToken());
            int c = Integer.parseInt(inputPos.nextToken());
            starts.add(new Pair(r - 1, c - 1));
        }

        stonPos = findStonPos();
        findMaxValue(0, 0);
        System.out.println(maxValue);

    }

    public static boolean inRange(int r, int c){
        return 0 <= r && r < n && 0 <= c && c < n  && board[r][c] == 0;
    }


    public static int BFS(){
        //
        int[] dr = new int[]{-1, 1, 0, 0};
        int[] dc = new int[]{0, 0, -1, 1};
        // 출발점의 개수
        int cnt = 0;
        // 기본 false로 초기화
        boolean[][] inQueue = new boolean[n + 1][n + 1];
        // 시작점 넣기
        for(Pair pair : starts){
            bfsQ.add(pair);
            inQueue[pair.x][pair.y] = true;
            cnt++;
        }

        while(!bfsQ.isEmpty()){
            Pair cusPos = bfsQ.poll();
            int cr = cusPos.x;
            int cc = cusPos.y;
            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i];
                int nc = cc + dc[i];
                if(inRange(nr, nc) && !inQueue[nr][nc]){
                    bfsQ.add(new Pair(nr, nc));
                    inQueue[nr][nc] = true;
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public static List<Pair> findStonPos(){
        List<Pair> pos = new ArrayList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == 1){
                    pos.add(new Pair(i, j));
                }
            }
        }
        return pos;
    }

    public static void findMaxValue(int level, int idx){
        if(level == m){
            //  돌 선택 후 1 -> 0으로 변경
            for(Pair pair : ans){
                board[pair.x][pair.y] = 0;
            }
            maxValue = Math.max(maxValue, BFS());
            // 다시 원상복귀
            for(Pair pair : ans){
                board[pair.x][pair.y] = 1;
            }
            return;
        }
        for(int i = idx; i < stonPos.size();i++){
            if(used[i] == 0){
                used[i] = 1;
                ans.add(stonPos.get(i));
                findMaxValue(level + 1, i + 1);
                used[i] = 0;
                ans.remove(ans.size() - 1);
            }
        }
    }
}