import argparse # Модуль для извлечения аргументов, передаваемых скрипту через командную строку

# Основная функция
def say_hello(name):
    print(f'Привет, {name}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Greetings') # Создаем парсер для аргументов, переданных через командную строку
    parser.add_argument('name', type=str, help='Your name')   # Задаем один обязательный аргумент - имя
    args = parser.parse_args()                                # Парсим аргументы
    name = args.name                                          # Извлекаем имя
    say_hello(name)                                           # Передаем имя в функцию для приветствия