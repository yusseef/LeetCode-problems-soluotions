nums = [1,2,3,4,5,6,7]
k = 3
for i in range(k):
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)