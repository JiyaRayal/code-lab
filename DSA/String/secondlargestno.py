# def secondlargest(arr):
#     first = second = float('-inf')
#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#     return second if second != float('-inf') else None

def secondLargest(s):
    largest = second = -1
    for ch in s:
        if ch.isdigit():
            num = int(ch)
            if num > largest:
                second = largest
                largest = num
            elif largest > num > second:
                second  =  num
    return second 
s = input("Enter a string: ")
print(secondLargest(s))