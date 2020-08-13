import tensorflow as tf
from DeepNetModel import DeepNetModel
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from KNNModel import KNNClassifier


k_predictor = KNNClassifier('clothes.data', 'worthy')
model = k_predictor.Train()
sample_data = np.array([0, 1, 0, 1, 0])
sample_data = sample_data.reshape(1, -1)

prediction = model.predict(sample_data)
print(prediction)
