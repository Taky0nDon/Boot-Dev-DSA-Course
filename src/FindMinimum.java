import java.util.Arrays;
class FindMinimum{
    public static void main(String[] args){
        if (args.length == 0){
            return;
        }
        int min = Integer.parseInt(args[0]);

        for (int i = 0; i<args.length; i++){
            if (Integer.parseInt(args[i]) < min){
               min = Integer.parseInt(args[i]);
            }
        }
        IO.println(min);
    }
}
