function sortArray(nums: number[]): number[] {
    if (nums === undefined){
        return [];
    }
    if (nums.length < 2) {
        return nums;
    }
    const mid = Math.floor(nums.length / 2);
    const left = sortArray(nums.slice(0,mid));
    const right = sortArray(nums.slice(mid, nums.length));
    return merge(left, right);
};

function merge(left: number[], right: number[]): number[] {
    const result = [];
    let i = 0;
    let j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            result.push(left[i]);
            i += 1;
        } else {
            result.push(right[j]);
            j += 1;
        }
    }
    while (i < left.length) {
        result.push(left[i]);
        i++;
    }
    while (j < right.length) {
        result.push(right[j]);
        j++;
    }
    return result;
}
