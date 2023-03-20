

model_weight_path = 'model'

import tensorflow as tf
import argparse
import numpy as np
#import os

# Hide GPU from visible devices
tf.config.set_visible_devices([], 'GPU')

def create_model():
    model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)),
                                tf.keras.layers.Dense(128, activation='relu'),
                                tf.keras.layers.Dense(10)])
    model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],)
    return (model)

def main_function(image_file_path, model_weight_path):
    model2 = create_model()
    model2.load_weights(model_weight_path)
    test_image = np.load(image_file_path)
    prediction = np.argmax(model2.predict(test_image.reshape(1,28,28,1), verbose = False))
    with open('prediction.txt', 'w') as f:               # Создаем новый файл для записи данных
        f.write(str(prediction))
    print("Prediiiiiiiiiiiiiiiiction:", prediction)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='mnist_path')
    parser.add_argument('mnist_path', type=str, help='Picture_path')
    args = parser.parse_args()
    mnist_path = args.mnist_path                                   
    main_function(mnist_path, model_weight_path)
#    print('Предположим что семь')
