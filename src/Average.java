class Average{
    public static int[] getNums(String[] strArr){
        int[] res = new int[strArr.length];
        if (strArr.length == 0){
            return new int[0];
        }
        for (int i=0;i<strArr.length;i++){
            res[i] = Integer.parseInt(strArr[i]);
        }
        return res;
    }

    public static int getSum(int[] nums){
        int sum = 0;
        for (int i=0;i<nums.length;i++){
            sum += nums[i];
        }
        return sum;
    }

    public static void main (String[] args){
        double average;
        int[] nums = getNums(args);
        if (nums.length == 0){ average = 0;
        }else{
            int sum = getSum(nums);
            average = (double) sum / (double) args.length;
        }
        IO.println(average);
    }
}

