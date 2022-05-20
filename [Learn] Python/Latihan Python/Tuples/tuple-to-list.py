from tkinter import Y


x = ("apple", "orange", "pear")
y = list(x)
y[1] = "grape"
x = tuple(y)
print(y)
print(x)
