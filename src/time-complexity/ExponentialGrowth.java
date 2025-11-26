import java.util.Arrays;

public class ExponentialGrowth {

    public static void main(String[] args) {
        int initialFollowers = Integer.parseInt(args[0]);
        int growthFactor = Integer.parseInt(args[1]);
        int days = Integer.parseInt(args[2]);
        int[] result = new int[days+1];
        IO.println("days:" + Integer.toString(days));
        IO.println(Arrays.toString(result));
        IO.println("length of arr:" + Integer.toString(result.length));
        result[0] = initialFollowers;
        int i = 1;

        while (i <= days) {
            result[i] = initialFollowers * growthFactor;
            initialFollowers = result[i];
            i++;
        }
        IO.println(Arrays.toString(result));
    }
}
