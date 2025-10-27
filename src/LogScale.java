import java.util.Arrays;
import java.text.DecimalFormat;

public class LogScale{
    public static void main(String[] args){
        DecimalFormat df = new DecimalFormat("###.###");
        String[] data = new String[args.length - 1];
        double base = Double.parseDouble(args[args.length - 1]);
        for (int i = 0; i < data.length; i++){
            data[i] = df.format(Math.rint(logArbitraryBase(Double.parseDouble(args[i]), base)));
        }
        IO.println(Arrays.toString(data));
    }
    public static double logArbitraryBase(double dbl, double base){
        return Math.log(dbl) / Math.log(base);
    }
}
