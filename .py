#SUM OF DIGIT
# def sum_of_digit(n):
#     s = str(n)
#     sum = 0

#     for ch in s:
#         sum+= int(ch)
#     return sum 

# n = 2398
# print(sum_of_digit(n))

#REVERSE STRING
# def reverse_string(n):
#     s = str(n)
#     s = s[::-1]
#     n = int(s)

#     return n 

# n = 234
# print(reverse_string(n))

# #PRIME CHECK 
# def prime_no(n):
#     if n <=1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
        
#     return True

# n = 45
# print(prime_no(n))

# class Student:
#     def __init__(self, name , marks):
#         self.name= name 
#         self.marks = marks

#     def average(self):
#         sum = self.marks
#         a = sum/3
#         print(f"{self.name} , your score is {a}")
        


# s1 = Student("rahul",[22,77,66])

# # s2 = Student("Jiya",21)
# # s3 = Studwnt("vandana", 22)

# print(s1.average())
# # print(s1.age,s2.age)

# import numpy as np
# a1 = np.array([2,3,4,1,5])
# a2 = np.zeros((2,3,4))
# a3 = np.ones((3,4,1))
# a4 = np.arange(0,20,4)
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a1.shape)
# print(a1.dtype)


# X = np.array([10,20],[20,30],[30,40])
# bias = np.array([2,3])
# X + bias

