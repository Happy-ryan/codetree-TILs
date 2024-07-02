import java.util.*;

public class Main {

    private static int n, m;


    public static void main(String[] args) {
        HashMap<Integer, Integer> numCountHashMap = new HashMap<>();

        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        for(int i = 0; i < n; i++) {
            int k = sc.nextInt();
            if(!numCountHashMap.containsKey(k)) {
                numCountHashMap.put(k, 1);
            }
            else {
                numCountHashMap.put(k, numCountHashMap.get(k) + 1);
            }
        }

        for (int j = 0; j < m; j++){
            int q = sc.nextInt();
            if(!numCountHashMap.containsKey(q)) {
                System.out.print(0 + " ");
            }
            else{
            System.out.print(numCountHashMap.get(q) + " ");
            }
        }

    }

}