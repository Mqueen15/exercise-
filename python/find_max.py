def find_max(nums):
    max_num = float ("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num=num # fill in the missing line here : (num = max_num) or (max_num = num) or (max_num += 1) or (max_num += num)
    return max_num
nums = (4,9,7)
print (find_max(nums))
#At first, max_num is filled with the minimum number. Then, on iterating over the list of numbers in nums, each value of nums is stored in the iterable num in series one by one on each iteration till the list of elements gets complete. On every iteration, the max_num value is compared with the current value in the iterable, and if num is greater than max_num, max_num is replaced with the big one, num. In such a way, once the loop terminates, we will have the maximum number of the list in the variable max_num and it is returned to the function call and is printed max_num=num will help in replacing the value in the max_num with biggest number
