import java.util.Arrays;
public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = createIntArray(args);
        if (arrayContains(arr, Integer.parseInt(args[args.length - 1]))) {
            IO.println("target found!");
        } else IO.println("target not found!");
    }
    public static int[] createIntArray(String[] args) {
        int[] argsArray = new int[args.length];
        for (int i = 0; i < args.length - 1; i++) {
            argsArray[i] = Integer.parseInt(args[i]);
        }
        return argsArray;
    }
    public static boolean arrayContains(int[] arr,
                                        int target) {
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
    return false;
    }
}
