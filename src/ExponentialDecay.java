class ExponentialDecay{
// remaining_total = quantity * ( retention_rate ^ time )
    public static void main(String[] args){
        if (args.length < 3){
            IO.println("Please provide correct arguments.");
            IO.println("initialFollowers, fractionLost, days");
            return;
        }
        int initialFollowers = Integer.parseInt(args[0]);
        double fractionLost = Double.parseDouble(args[1]);
        int days = Integer.parseInt(args[2]);
        double remaining = calculateRemaining(initialFollowers,
                                              fractionLost,
                                              days);
        IO.println((int) remaining);
    }

    public static double calculateRemaining(int initialFollowers,
                                            double fractionLost,
                                            int days){
    double remaining = initialFollowers * Math.pow(1 - fractionLost, (double) days);
    return remaining;
    }
}

