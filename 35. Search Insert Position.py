def searchInsert(nums, target):
    if nums.count(target) == 0:
        nums.append(target)
        nums.sort()
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid

        elif guess < target:
            low = mid + 1

        elif guess > target:
            high = mid - 1


