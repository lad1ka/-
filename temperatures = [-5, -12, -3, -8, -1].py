#Было
temperatures = [-5, -12, -3, -8, -1]

max_temp = 0  # Инициализация максимального значения

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp

print("Самая высокая температура:", max_temp)

#Стало
temperatures = [-5, -12, -3, -8, -1]

# Решение 1: Берем первый элемент списка как стартовое значение
max_temp = temperatures[0] 

for temp in temperatures:
    if temp > max_temp:
        max_temp = temp

print("Самая высокая температура:", max_temp) # Выведет -1

# Решение 2 : Использовать встроенную функцию
# print("Самая высокая температура:", max(temperatures))
