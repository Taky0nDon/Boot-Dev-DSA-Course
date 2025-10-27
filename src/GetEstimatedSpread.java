public class GetEstimatedSpread{
    public static void main(String[] args){
        double num_followers = args.length;
        if (num_followers == 0){ IO.println(0); return; }
        double total_audience_followers = 0;
        for (int i = 0; i < num_followers; i++){
            total_audience_followers += Integer.parseInt(args[i]);
        }
        double average_audience_followers = total_audience_followers / num_followers;
        double estimated_spread = average_audience_followers *
            Math.pow((double) num_followers, 1.2);
        IO.println(estimated_spread);

    }
}
