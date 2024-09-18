#Create a Tuple:How do you create a tuple with the following elements: "red", "green", "blue"?
n=("red", "green", "blue")
print(n)

#Access Elements in a Tuple:How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
colors=("red", "green", "blue", "yellow")
first_elem=colors[0]
last_elem=colors[-1]
print("First:", first_elem)
print("Last:", last_elem)

#Immutable Nature of Tuples:What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
# c = ("red", "green", "blue")
# c[1]="yellow"
#will raise an error as the element cannot be changed directly.

#Tuple Unpacking:Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
coordinates = (10,20,30)
x,y,z=coordinates
print("x:" ,x)
print("y:",y)
print("z:",z)

#Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
colors = ("red", "green", "Blue")
if "blue" in colors:
    print("Blue is present")
else:
    print("Blue is not present")


#Tuple Length:Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(len(days))
