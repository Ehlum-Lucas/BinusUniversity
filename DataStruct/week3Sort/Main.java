import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void iterateCubes(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    System.out.println("i: " + i + ", j: " + j + ", k: " + k);
                }
            }
        }
    }

    public static void iterateSquares(int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println("i: " + i + ", j: " + j);
            }
        }
    }

    public static ArrayList<Integer> generateRandomArray(int n) {
        ArrayList<Integer> list = new ArrayList<>(n);
        Random random = new Random();

        for (int i = 0; i < n; i++) {
            list.add(random.nextInt(100000));
        }
        return list;
    }

    public static void main(String[] args) {
        PerformanceMetrics.measureRuntime(() -> iterateCubes(5));
        PerformanceMetrics.measureRuntime(() -> iterateSquares(10));
        ArrayList<Integer> arr1 = generateRandomArray(10000);
        ArrayList<Integer> arr2 = new ArrayList<>(arr1);

        PerformanceMetrics.measureRuntime(() -> Sort.bubbleSort1(arr1));
        PerformanceMetrics.measureRuntime(() -> Sort.bubbleSort2(arr2));
        /*
         * bubbleSort1 is slower than bubbleSort2 because bubbleSort2 has a flag to check if the array is already sorted.
         * If the array is already sorted, the algorithm will stop early.
         */
    }
}
