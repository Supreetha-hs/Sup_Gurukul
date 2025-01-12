# Function to find the maximum of three numbers
def find_max(num1, num2, num3):
    return max(num1, num2, num3)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print("The maximum number is:", find_max(num1, num2, num3))
# Function to multiply all the numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
numbers = [2, 3, 4]
print("The product of all numbers in the list is:", multiply_list(numbers))
# Program to reverse a string
def reverse_string(s):
    return s[::-1]

# Example usage
input_string = input("Enter a string: ")
print("Reversed string:", reverse_string(input_string))
# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is:", factorial(num))
# Function to return a new list with distinct elements
def distinct_elements(lst):
    return list(set(lst))

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print("List with distinct elements:", distinct_elements(input_list))
# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
# Program to print the even numbers from a given list
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list are:")
print_even_numbers(numbers)
# Function to count the number of upper and lower case letters
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Example usage
input_string = input("Enter a string: ")
upper, lower = count_case(input_string)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")
