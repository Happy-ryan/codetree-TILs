import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        List<Integer> arr = new ArrayList<>();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            // Integer.parseInt를 사용하여 문자열을 정수로 변환해야 합니다.
            arr.add(Integer.parseInt(st.nextToken()));
        }
        List<Integer> sortedArr = bubblSort(arr);
        for(int i : sortedArr){
            System.out.print(i + " ");
        }
    }
  private static List<Integer> bubblSort(List<Integer> arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; i++) {
            boolean isSwap = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr.get(j) > arr.get(j + 1)) {
                    // Swap elements if they are in the wrong order
                    int temp = arr.get(j);
                    arr.set(j, arr.get(j + 1));
                    arr.set(j + 1, temp);
                    isSwap = true;
                }
            }

            // If no two elements were swapped by inner loop, the array is already sorted
            if (!isSwap) {
                break;
            }
        }
        return arr;
    }
}