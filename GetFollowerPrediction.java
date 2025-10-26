class GetFollowerPrediction{
    public static void main(String[] args){
        String influencerType = args[1];
        double followerCount = Double.parseDouble(args[0]);
        double numMonths = Double.parseDouble(args[2]);
        double factor = 2;
        switch (influencerType) {
            case "fitness": factor = 4;
                break;
            case "cosmetic": factor = 3;
                break;
        }
        double newFollowerCount = followerCount * Math.pow(factor, numMonths);
        IO.println(newFollowerCount);
    }
}
