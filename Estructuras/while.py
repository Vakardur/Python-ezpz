# While es repetir lo que está dentro de la estructura
# Mientras se cumpla su condición

# number = 100

# Hay código arriba ↑

# while number < 10:
#     # print(number)
#     number += 1

# Hay código abajo ↓
# number = 0
# print('terminó el while')


# Imprimir los números del 1 al 10 excepto el 5 y el 7

# counter = 1
# while counter <= 10:
#     if counter == 5 or counter == 7:
#         counter += 1
#         continue
#     print(counter)
#     counter += 1

# Fizz buzz
# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# counter = 0
# while counter <= 50:
#     if counter % 3 == 0 and counter % 5 == 0:
#         print("FizzBuzz")
#     elif counter % 3 == 0:
#         print("Fizz")
#     elif counter % 5 == 0:
#         print("Buzz")
#     else:
#         print(counter)
#     counter += 1
