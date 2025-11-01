import java.util.Arrays;
public class BubbleSort {
    public static void main(String[] args) {
        int[] unsortedArray = new int[args.length];
        for (int i = 0; i < args.length; i++) {
            unsortedArray[i] = Integer.parseInt(args[i]);
        }

        Boolean swapping = true;
        while (swapping) {
            swapping = false;
            for (int i = 1; i < unsortedArray.length; i++) {
                if (unsortedArray[i] < unsortedArray[i - 1]) {
                    swapping = true;
                    int tmp = unsortedArray[i];
                    unsortedArray[i] = unsortedArray[i - 1];
                    unsortedArray[i - 1] = tmp;
                }
            }
        }
        IO.println(Arrays.toString(unsortedArray));
    }
}


