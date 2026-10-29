#HASHMAP APPROACH
# def twoSum(nums, target):
#     array = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in array:
#             return [array[diff], i]
#         array[num] = i
# nums = [2, 7, 11, 15]
# target = 9
# result = twoSum(nums, target)
# print("Output:", result)


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
s = Student("Jiya", 101)
print(s.name)
print(s.roll)
