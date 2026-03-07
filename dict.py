dict = {"name": "Rajesh", "age": 25, "city": "Mumbai"}
print(dict["name"])  # Output: Rajesh
print(dict.get("age"))  # Output: 25
dict["email"] = "therajeshdulhani@gmail.com"
dict["age"] = 26
del dict["city"]
print(dict)