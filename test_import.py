#!/usr/bin/env python3
import lab3a
import lab3b
import lab3c

text = lab3a.return_text_value()
print(text)
print(lab3a.return_number_value())


print(lab3b.sum_numbers(10, 5))       # Should return 15
print(lab3b.subtract_numbers(10, 5))   # Should return 5
print(lab3b.multiply_numbers(10, 5))    # Should return 50


print(lab3c.operate(10, 20, 'add'))
print(lab3c.operate(2, 3, 'add'))
print(lab3c.operate(100, 5, 'subtract'))
print(lab3c.operate(10, 20, 'subtract'))
print(lab3c.operate(5, 5, 'multiply'))
print(lab3c.operate(10, 100, 'multiply'))
print(lab3c.operate(100, 5, 'divide'))
print(lab3c.operate(100, 5, 'power'))
