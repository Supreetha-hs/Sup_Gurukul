# Program to check if a number is even or odd using the modulus operator
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
# Program to check if a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print("The number is zero.")
# Program to calculate grade based on marks
marks = float(input("Enter the marks: "))
if marks >= 90:
    grade = 'A'
elif 80 <= marks < 90:
    grade = 'B'
elif 70 <= marks < 80:
    grade = 'C'
elif 60 <= marks < 70:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")
# Program to write to a file and read from it
# Writing to the file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("Content of the file:", content)
# Program to count the number of words in a file
try:
    with open("data.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"Number of words in the file: {word_count}")
except FileNotFoundError:
    print("File 'data.txt' not found.")
# Program to print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)
# Program to display the multiplication table of a number
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
