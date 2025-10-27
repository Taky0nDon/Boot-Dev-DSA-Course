import java.util.Arrays;
import java.math.BigDecimal;
import java.math.MathContext;

public class LogScale{
    public static void main(String[] args){
        //BigDecimal[] data = new BigDecimal[args.length - 1];
        double[] data = new double[args.length - 1];
        double base = Double.parseDouble(args[args.length - 1]);
        for (int i = 0; i < data.length; i++){
            data[i] = Math.rint(logArbitraryBase(Double.parseDouble(args[i]), base));
        }
        IO.println(Arrays.toString(data));
    }
    public static double logArbitraryBase(double dbl, double base){
        return Math.log(dbl) / Math.log(base);
    }
}
