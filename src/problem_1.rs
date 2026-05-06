#![allow(dead_code)]
use std::collections::HashMap;

struct Solution;

impl Solution {

    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_map: HashMap<i32, i32> = HashMap::with_capacity(nums.len());
        for (i, &a_num) in nums.iter().enumerate() {
            if let Some(&index) = num_map.get(&(target - a_num)) {
                return vec![index, i as i32];
            } else {
                num_map.insert(a_num, i as i32);
            }
        }
        vec![0,1]
    }
}

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::Solution;

    #[rstest]
    #[case(vec![2,7,11,15], 9, vec![0,1])]
    #[case(vec![3,2,4], 6, vec![1,2])]
    #[case(vec![3,3], 6, vec![0,1])]
    fn test_1(#[case] nums: Vec<i32>, #[case] target: i32, #[case] answer: Vec<i32>){
        assert_eq!(Solution::two_sum(nums, target), answer);
    }
}