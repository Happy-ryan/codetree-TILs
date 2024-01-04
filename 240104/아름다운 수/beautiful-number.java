import java.io.*;
import java.util.*;

public class Main {

    public static List<Integer> ans = new ArrayList<>();
    public static int cnt = 0;
    public static int n;

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        dfs(0);
        System.out.println(cnt);
        
    }
    public static boolean isBeautiful(){
        for(int start = 0; start < n; start += ans.get(start)){
            if(start + ans.get(start) - 1 >= n){
                return false;
            }
            for(int end = start; end < start + ans.get(start); end++){
                if(ans.get(end) != ans.get(start)){
                    return false;
                }
            } 
        }
        return true;
    }
    public static void dfs(int level){
        if(level == n){
            if(isBeautiful()){
                cnt++;
            }
            return;
        }
        for(int i = 1; i < 5; i++){
            ans.add(i);
            dfs(level + 1);
            ans.remove(ans.size() - 1);
        }
    }
}