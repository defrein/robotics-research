from typing import Iterable


list_variable = [x for x in Iterable]

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

# idk, still error
