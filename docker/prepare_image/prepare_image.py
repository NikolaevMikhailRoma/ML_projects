from PIL import Image                          # Обработка изображений
import numpy as np                              # Работа с массивами
import argparse                                 # Модуль для извлечения аргументов, передаваемых скрипту через командную строку
import os

def prepare_image(path):
    img = Image.open(path)                                    # Загружаем картинку по переданному пути
    print(f'Размер исходных данных: {np.array(img).shape}')   # Выводим информацию о размере исходного изображения

    img = img.resize((32, 32)).convert('L')                   # Приводим изображения к фиксированному размеру и переводим в оттенки серого
    img = np.array(img)                                       # Преобразуем изображение в numpy-массив
    img = img.reshape(1, -1)                                  # Вытягиваем в вектор
    img = img.astype('float32') / 255.                        # Нормализуем данные
    print(f'Размер данных после преобразования: {img.shape}') # Выводим информацию о новом размере данных

    with open('prepared_image.npy', 'wb') as f:               # Создаем новый файл для записи данных
        np.save(f, img)                                       # Записываем в файл обработанный numpy-массив

    print('Изображение обработано!')

if __name__ == '__main__':
#    print(os.listdir())
#    print (os.getcwd())
    parser = argparse.ArgumentParser(description='Prepare image') # Создаем парсер для аргументов, переданных через командную строку
    parser.add_argument('path', type=str, help='Your path')   # Задаем один обязательный аргумент - имя
    args = parser.parse_args()                                # Парсим аргументы
    path = args.path
    prepare_image(path)
    print('Done')
