# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).

# Python поддерживает умножение строк на числа.

hello = "Hello "

world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных
hello_world = hello + world
# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками
hello10 = hello * 10
# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками
########
world_world = hello[:-1] + ", " + world + "! " + (world + " ") * 2 + (hello * 2)[:-1] + "!"
#beautiful = "{0}, {1}! {1} {1} {0} {0}!".format(hello[:-1],world)
# Вы можете получить доступ к символу строки, если знаете его позицию. Например, str[index] даст символ в позиции index в строке str.

# Запомните! Строки всегда индексируются с 0.

python = "Python"

p_letter = python[0].lower() + python[2:4] + python[-1] # Используйте переменную python для получения строки "pthn".
########


# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки.
# Обратите внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1.
# Таким образом, вы можете использовать отрицательные числа в операторе индексирования для подсчета символов с конца строки.

long_string = "This is a very long string!"
short_string = long_string[-1]
# Используйте отрицательный индекс для получения символа '!' из строки