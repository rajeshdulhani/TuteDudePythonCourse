# simple dictionary examples

# create a dictionary with some key/value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# access a value by its key
print("Name:", person["name"])      # Alice
print("Age:", person.get("age"))    # 30

# add a new entry or update an existing one
person["email"] = "alice@example.com"
person["age"] = 31

# remove an entry
del person["city"]       # removes the "city" key
# or use pop to get the value while removing
email = person.pop("email", None)

# iterate over keys and values
for key, value in person.items():
    print(f"{key} -> {value}")

# check for existence of a key
if "name" in person:
    print("Name is in the dictionary")

# dictionary comprehension (build from a list)
squares = {n: n * n for n in range(1, 6)}
print("squares:", squares)

# output when run:
# Name: Alice
# Age: 30
# name -> Alice
# age -> 31
# Name is in the dictionary
# squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}