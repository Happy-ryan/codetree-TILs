import java.util.*;
import java.io.*;

public class Main {
    public static int MAX = 200;
    public static final int[][] board = new int[MAX][MAX];

    public static int N, M;
    // 총 6개의 배열이 모두 포함되게 하는 공통된 이차원 배열을 사용하는 것이 깔끔하다!
    // 2x2 와 3x1 이 있으므로 3x3이 공통된 이차원 배열이라고 할 수 있다.
    // 공통된 이차원 배열의 왼쪽 상단에 밀착!
    // 이렇게 할 수 있는 이유는 결국 최대합을 찾기 때문!
    public static int[][][] possibleShapes = new int[][][]{
        {{1,1,0},
        {1,0,0},
        {0,0,0}},

        {{1,1,0},
        {0,1,0},
        {0,0,0}},

        {{0,1,0},
        {1,1,0},
        {0,0,0}},

        {{1,0,0},
        {1,1,0},
        {0,0,0}},

        {{1,1,1},
        {0,0,0},
        {0,0,0}},

        {{1,0,0},
        {1,0,0},
        {1,0,0}},
    };
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer inputNM = new StringTokenizer(br.readLine());

        N = Integer.parseInt(inputNM.nextToken());
        M = Integer.parseInt(inputNM.nextToken());

        for(int r = 0; r < N; r++){
            StringTokenizer row = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++){
                board[r][c] = Integer.parseInt(row.nextToken());
            }
        }

        int res = 0;
        for(int r = 0; r < N; r++){
            for(int c = 0; c < M; c++){
                res = Math.max(res, getMaxSum(r, c));
            }
        }
        System.out.println(res);
    }
    public static int getMaxSum(int r, int c){
        int maxSumVal = 0;
        for (int i = 0; i < 6; i++){
            int sum = 0;
            boolean isRange = true;
            for(int dr = 0; dr < 3; dr++){
                for (int dc = 0; dc < 3; dc++){
                    if(possibleShapes[i][dr][dc] == 0){
                        continue;
                    }
                    // 1인데 현재(r,c)기준에서 n,m보다 크거나 같으면 격자밖을 의미함.
                    if(r + dr >= N || c + dc >= M){
                        isRange = false;
                    }
                    else{
                        sum += board[r + dr][c + dc];
                    }
                }
                if(isRange){
                    maxSumVal = Math.max(maxSumVal, sum);
                }
            }
        }
        return maxSumVal;
    }
}