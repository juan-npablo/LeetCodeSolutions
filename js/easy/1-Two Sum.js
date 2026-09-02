/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/**solution 1 - brute force -> O(n^2) double loop to check all pairs of numbers **/
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++){
        for(let j = i+1; j < nums.length; j++){
            if(nums[i] + nums[j] === target){
                return [i, j]
            }
        }
    }
};

/**solution 2 - Verifying if target - nums[i] is in the list -> O(n^2) .index() method is O(n) and we are calling it inside a loop **/
var twoSum = function(nums, target) {
    for(i = 0; i < nums.length; i++){
        if(nums.slice(i+1).includes(target - nums[i])){
            return [i, nums.indexOf(target - nums[i], i+1)]
        }
    }
};

/**solution 3 - Using a dictionary to store the indices of the numbers -> O(n) **/
var twoSum = function(nums, target) {
    let dictionary = {};
    for (let i = 0; i < nums.length; i++){
        let complement = target - nums[i];
        if (dictionary[complement] !== undefined){
            return [dictionary[complement], i];
        }
        dictionary[nums[i]] = i;
    }
