// greedy > 회의실 배정 문제와 동일함.
// 끝나는 시간으로 정렬하고 나서 시작시간으로 정렬

import java.util.*;

class Pair implements Comparable<Pair> {
    int start, end;

    public Pair(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public int compareTo(Pair other) {
        if (this.end == other.end) {
            // 시작 시간 기준 - 오름차순
            return Integer.compare(this.start, other.start);
        }
        // 끝나는 시간 기준- 오름차순
        return Integer.compare(this.end, other.end);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        List<Pair> pairs = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            pairs.add(new Pair(start, end));
        }

        // Collections.sort(pairs, new Comparator<Pair>() {
        //     @Override
        //     public int compare(Pair pair1, Pair pair2) {
        //         if (pair1.end == pair2.end) {
        //             return Integer.compare(pair1.start, pair2.start);
        //         }
        //         // compare(앞, 뒤)
        //         return Integer.compare(pair1.end, pair2.end);
        //     }
        // });

        Collections.sort(pairs);

        int cnt = 1;
        int last = pairs.get(0).end;
        for (int i = 1; i < n; i++) {
            if (last < pairs.get(i).start) {
                cnt++;
                last = pairs.get(i).end;
            }
        }

        System.out.println(cnt);

        
    }
}