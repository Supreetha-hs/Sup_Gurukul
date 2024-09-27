# # 1.Write a Python function to find the maximum of three numbers
# def max_of_three(a, b, c):
#     return max(a, b, c)
# print(max_of_three(10, 20, 30))


#2.Write a Python function to multiply all the numbers in a list.
#Sample List: (8, 2, 3, -1, 7)
#Expected Output: -336
# def multiply_list(numbers):
#     result = 1
#     for num in numbers:
#         result *= num
#     return result
# sample_list = (8, 2, 3, -1, 7)
# print(multiply_list(sample_list))
#
#
# #3.Write a Python program to reverse a string.
# #Sample String: "1234abcd"
# #Expected Output: "dcba4321"
# def reverse_string(s):
#     return s[::-1]
# sample_string = "1234abcd"
# print(reverse_string(sample_string))

# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers."
#     elif n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
# print(factorial(10))

# #5.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# #Sample List :[1,2,3,3,3,3,4,5]
# #Unique List :[1, 2, 3, 4, 5]
# def unique_list(lst):
#     return list(set(lst))
# sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
# print(unique_list(sample_list))

# #6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(4))

# #7.Write a Python program to print the even numbers from a given list.
# #Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #expected Result: [2, 4, 6, 8]
# def even_numbers(lst):
#     return [num for num in lst if num % 2 == 0]
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even_numbers(sample_list))


# #8.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# #Sample String: 'The quick Brow Fox'
# #Expected Output:
# #No. of Upper case characters : 3
# #No. of Lower case Characters : 12
# def count_case(s):
#     upper_count = sum(1 for char in s if char.isupper())
#     lower_count = sum(1 for char in s if char.islower())
#     return upper_count, lower_count
# sample_string = 'The quick Brow Fox'
# upper, lower = count_case(sample_string)
# print(f"No. of Upper case characters: {upper}")
# print(f"No. of Lower case characters: {lower}")


# #9.Write a Python function to sum all the numbers in a list.
# #Sample List: (8, 2, 3, 0, 7)
# #Expected Output: 20
# def sum_list(numbers):
#     return sum(numbers)
# sample_list = (8, 2, 3, 0, 7)
# print(sum_list(sample_list))


# #10.Write a Python function that checks whether a passed string is a palindrome or not.
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("MALAYALAM"))
# print(is_palindrome("CAKE"))



