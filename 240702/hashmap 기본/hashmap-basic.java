import java.util.*;

public class Main {

    private static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        HashMap<Integer, Integer> hm = new HashMap<>();

        n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            // String 형 입력 및 리턴	(공백을 기준으로 한 단어를 읽음)
            String cmd = sc.next();

            if(cmd.equals("add")) {
                int k = sc.nextInt();
                int v = sc.nextInt();
                hm.put(k, v);
            }
            else if(cmd.equals("remove")){
                int k = sc.nextInt();
                hm.remove(k);
            }
            else{
                int k = sc.nextInt();
                if(hm.containsKey(k)) {
                    System.out.println(hm.get(k));
                }
                else{
                    System.out.println("None");
                }
            }


        }


    }
}