# BRUTE FORCE
# def missingno(arr, n):
#     n = len(arr) 
#     for i in range(1, n + 1):
#         if i not in arr:
#             return i

def missingno(arr):
    n = len(arr)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    return missing
        