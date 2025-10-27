import java.util.Arrays;

public class Median{
    public static void main(String[] args){
        double median;
        String result;
        int mid;
        int items = args.length;
        double[] listOfNums = new double[items];

        if (items > 0){
            mid = items / 2;
        }else{
            IO.println("None");
            return;
        }

        for (int i=0; i<items; i++){
            listOfNums[i] = Double.parseDouble(args[i]);
        }

        Arrays.sort(listOfNums);
        if (items % 2 == 0){
            int mid1 = mid;
            int mid2 = mid - 1;
            median = (listOfNums[mid1] + listOfNums[mid2]) / 2;
            result = Double.toString(median);
        }else{
            median = listOfNums[mid];
            result = Double.toString(median).replaceAll("\\.?0+$", "");
        }

        IO.println(Arrays.toString(listOfNums));
        IO.println(result);
    }
}
