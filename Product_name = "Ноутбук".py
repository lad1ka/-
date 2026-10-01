#Было
product_name = "Ноутбук"
price = 50000
discount = 5000

final_message = "Вы купили " + product_name + " за " + price - discount + " рублей."
print(final_message)

#Стало
product_name = "Ноутбук"
price = 50000
discount = 5000

# F-строка сама преобразует числа в текст и выполнит математику внутри скобок
final_message = f"Вы купили {product_name} за {price - discount} рублей."
print(final_message)
