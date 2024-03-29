import java.util.*;

public class Main {
    private static final int MAX_N = 100000;

    private static int n, m;
    private static int[] nums = new int[MAX_N];
    private static HashMap<Integer, Integer> freq = new HashMap<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
        }

        for (int i = 0; i < m; i++) {
            int want = sc.nextInt();
            System.out.print(freq.getOrDefault(want, 0) + " ");
        }

    }

}