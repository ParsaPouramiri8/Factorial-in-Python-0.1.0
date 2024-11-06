import sys
sys.set_int_max_str_digits(100000)
number = input("Enter Your Number For Factorial (like that 1!): ")
number_part = int(number[:-1])
factorial_symbol = number[-1]
numbers_list = []
for i in range(number_part, 0, -1):
    numbers_list.append(i)
product = 1
for num in numbers_list:
    product *= num
    print(f"{product // num} * {num} = {product}")
print(f"Factorial of {number_part} is {product}")