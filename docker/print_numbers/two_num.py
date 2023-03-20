import argparse # Модуль для извлечения аргументов, передаваемых скрипту через командную строку

# Основная функция
def get_sum(a,b):
    print(f'{a+b}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Greetings') # Создаем парсер для аргументов, переданных через командную строку
    parser.add_argument('a', type=float, help='a_num')   # Задаем один обязательный 
    parser.add_argument('b', type=float, help='b_num')   # Задаем один обязательный
    args = parser.parse_args()                                # Парсим аргументы
    a = args.a
    b = args.b
    get_sum(a,b)
    
