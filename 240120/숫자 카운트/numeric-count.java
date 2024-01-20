import java.util.*;

public class Main {

    private static final int MAX_DIGIT = 3;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        Set<Integer> cnt = new HashSet<>();
        for (int i = 100; i < 1000; i++) {
            cnt.add(i);
        }

        int[][] predicts = new int[N][3];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 3; j++) {
                predicts[i][j] = scanner.nextInt();
            }
        }


        for (int[] predict : predicts) {
            Set<Integer> candidateList = new HashSet<>();
            for (int candidateNumber = 100; candidateNumber < 1000; candidateNumber++) {
                //  틀린이유: predict가 변경되고 있음! -> check 함수 변경해야함
                if (check(candidateNumber, predict)) {
                    candidateList.add(candidateNumber);
                }
            }
            // 교집합
            cnt.retainAll(candidateList);
        }

        System.out.println(cnt.size());
    }

    private static boolean check(int candidateNumber, int[] predict) {
        List<Integer> candidate = new ArrayList<>();
        List<Integer> pre = new ArrayList<>();

        for (int i = 1; i <= MAX_DIGIT; i++) {
            // 기존 값이 변해서는 안된다!!
            // candidateNumber % 10
            // candidate / 10 하면 기존 값이 변경된다!
            int a = candidateNumber % (int) Math.pow(10, i) / (int) Math.pow(10, i - 1);
            int p = predict[0] % (int) Math.pow(10, i) / (int) Math.pow(10, i - 1);

            if (candidate.contains(a) || a == 0) {
                return false;
            }
            candidate.add(a);

            if (pre.contains(p) || p == 0) {
                return false;
            }
            pre.add(p);
        }

        int cnt_1 = 0;
        int cnt_2 = 0;

        for (int i = 0; i < MAX_DIGIT; i++) {
            if (candidate.get(i).equals(pre.get(i))) {
                cnt_1++;
            } else {
                if (pre.contains(candidate.get(i))) {
                    cnt_2++;
                }
            }
        }

        return cnt_1 == predict[1] && cnt_2 == predict[2];
    }

}