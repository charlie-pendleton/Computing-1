"""print("hello world")
student_name = "Charlie"
student_age = 18
print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")

def sum(a,b):
    return a + b

print(f"the sum is: {sum(10,15)}")"""

#challenge week 1
border = ""
name = input("what is your name: ")
username = input("what is your username: ")
location = input("what is your location: ")


name_l = len(name)
username_l = len(username)
location_l = len(location)

length = max(int(name_l), int(username_l), int(location_l))
for i in range(0, length + 13):
    border = border + "-"

name_end_border = "|"
username_end_border = "|"
location_end_border = "|"

for i in range(0, length-name_l):
    " ".join(name_end_border)
for i in range(0, length-username_l):
    " ".join(username_end_border)
for i in range(0, length-location_l):
    "".join(location_end_border)
    


print(f"+ {border} +")
print(f"| Name:     {name}    {name_end_border}")
print(f"| Username: {username}    {username_end_border}")      
print(f"| Location: {location}    {location_end_border}") 
print(f"+ {border} +")     