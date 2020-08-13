import tensorflow as tf
from tensorflow import keras


class DeepNetModel:

    def get_compiled_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(5, activation='relu'),
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(1)
        ])

        model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        return model
