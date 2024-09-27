# #Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
file = open("sample.txt", "w")
file.write("Hello! this is a sample file.")
file.close()
file=open("sample.txt" , "r")
display=file.read()
file.close()
print(display)

#########
# #Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
# file=open("data.txt", "r")
# display=file.read()
# count=len(display)
# file.close()
# print("Number of words in the file ;", count)

######

# #Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.
# for n in range (1,11):
#     print(n)

# #Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.
# n= int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")