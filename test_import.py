#!/usr/bin/env python3
import lab3a
import lab3b
import lab3c
import lab3d
import lab3e
from lab3f import *

text = lab3a.return_text_value()
print(text)
print(lab3a.return_number_value())


print(lab3b.sum_numbers(10, 5))
print(lab3b.subtract_numbers(10, 5))
print(lab3b.multiply_numbers(10, 5))


print(lab3c.operate(10, 20, 'add'))
print(lab3c.operate(2, 3, 'add'))
print(lab3c.operate(100, 5, 'subtract'))
print(lab3c.operate(10, 20, 'subtract'))
print(lab3c.operate(5, 5, 'multiply'))
print(lab3c.operate(10, 100, 'multiply'))
print(lab3c.operate(100, 5, 'divide'))
print(lab3c.operate(100, 5, 'power'))


print(lab3d.free_space())


print(lab3e.give_list())
print(lab3e.give_first_item())
print(lab3e.give_first_and_last_item())
print(lab3e.give_second_and_third_item())


print(my_list)
add_item_to_list(my_list)
add_item_to_list(my_list)
add_item_to_list(my_list)
print(my_list)

remove_items_from_list(my_list, [1, 5, 6])
print(my_list)
