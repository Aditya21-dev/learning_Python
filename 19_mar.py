# Creating a simple dictionary
student = {
    "name": "Adi",
    "age": 20,
    "course": "BCA"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Bhopal"

# Updating a value
student["age"] = 21

# Removing a key-value pair
student.pop("course")

# Looping through dictionary
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)