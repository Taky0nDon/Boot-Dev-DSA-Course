import java.util.Arrays;
public class MergeSort {
    public static void main(String[] args) {
        long[] inputList = new long[args.length];
        for (int i = 0; i < args.length; i++) {
            inputList[i] = Long.parseLong(args[i]);
        }
        long [] outputList = splitList(inputList);
        IO.println(Arrays.toString(outputList));
    }

    public static long[] splitList(long[] list) {
        if (list.length < 2) {
            return list;
        }

        int mid = list.length / 2;
        long[] left = new long[mid];
        long[] right = new long[list.length - mid];
        for (int i = 0; i < list.length; i++) {
            if (i < mid) {
                left[i] = list[i];
            }
            else {
                right[i - mid] = list[i];
            }
        }
        long[] L = splitList(left);
        long[] R = splitList(right);
        return mergeLists(L, R);
    }

    public static long[] mergeLists(long[] left, long[] right) {
        long[] result = new long[left.length + right.length];
        int resultIndex = 0;
        int i = 0;
        int j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]){
                result[resultIndex] = left[i];
                i++;
            } else {
                result[resultIndex] = right[j];
                j++;
            }
            resultIndex++;
        }

        while (i < left.length) {
            result[resultIndex] = left[i];
            i++;
            resultIndex++;
        }
                
        while (j < right.length) {
            result[resultIndex] = right[j];
            j++;
            resultIndex++;
        }
        return result;
    }
}
