def topKelement(nums, k):

    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    sorted_count = sorted(count,key=count.get,reverse=True)
    return sorted_count[:k]
nums = [1,2,2,3,3,3,4,4,4,4]
k= 3
print(topKelement(nums,k))