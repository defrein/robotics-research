# How to remove an Item from a List

# 1. using remove()
android = ["jellybean", "kitkat", "marshmallow"]
android.remove("jellybean")
print(android)

# 2. using pop() to remove the last item
fruits = ["apple", "mango", "guava"]
fruits.pop()
print(fruits)

# 3. using del() to remove a specific item
colors = ["red", "green", "blue"]
del colors[1]
print(colors)
