# ML_projects
Здесь представленны шаблоны и инструкции для различных задач
Основной стек: tensorflow
1. ChatGPT.ipynb - используем OpenAI для заполнения простых тектовых ответов в таблицу:
  а. Переводим текстовую оценку отзывов в цифру и сортируем таблицу
2. ML_audio.ipynb - обработка аудио-сигналов, первым блоком идут датасеты, ML-модели выведенны отдельно в конце.
Стек: librosa.
  а. Предсказывание жанра аудио: датасет разбиваются на фрагменты по 15 секунд с шагом 2 секунды
  б. Обработка 2-4 секунднх записей слов с отпределенной эмоцией
3. ML_AE_mnist.ipynb - автокодировщик (autoencoder) на датасете MNIST
  a. Простой автокодировщик
  б. TODO: добавиться арзитектуры вариационного кодировщика VAE и с условием CAE, VCAE/
4. ML_UNET, PSPNET object_segmentation.ipynb - Задача сегментации по архитектурам U-NET, PSP-NET для изображений со стройки
! при обработке датасета уменьшенно кол-во классов от оригинала
  Варианты для обучения: a. дообучить модели и оценить время, б. сравнить с RES-NET
5. ./Object_detection/
  a. PROTOTYPE_ML_RetinaNet.ipynb (неактуально) - комментарии для задачи OD на датасете COCO17 архитектуре Retina-NET на базе ResNet-50. Обучение занимает космос
6. ./docker/ - docker images, containes operations
  a. docker_mnist - prepare number
  b. hello_app - print 'hello'
  c. prepare_image - prepare images
  d. print_numbers - print sum of two numbers
7. ./tf_serving/ - hh data processing
  a. tf_serving_hh_custom.ipynb - развертывание модели с использованием кастомной сигнатуры
  b. tf_serving_hh_custom_2versions.ipynb - то же с использованием двух моделей
7. ./Treacking/YOLO_humans.ipynb (неактуально) - текинг людей на базе YOLOv4. В блокноте проблема с путями
8. Задачник_Генетические_алгоритмы.ipynb - на этом можно большую часть тестовых заданий для тинькофф стажировки сделать. Дополняется
9. Кластеризация, задачник.ipynb - задачи кластеризации, ничего интересного. Стек: sklearn
10 ./NLP/
  а.
  б.
  в.
11. ./pytorch-tensorflow_tests/
  a. pytorch-tensorflow.ipynb - gpu test on local machine

