import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications.resnet_v2 import ResNet50V2
from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Dropout


def make_model(input_shape, num_classes):
    
    rn50v2 = ResNet50V2(weights='imagenet', include_top=False, input_shape=input_shape)
    
    for layer in rn50v2.layers:
        layer.trainable = False

    rn50v2 = Sequential([
        rn50v2,
        Flatten(),
        Dense(1024, activation = 'relu'),
        Dropout(0.4),
        Dense(num_classes, activation = 'softmax')])


    return rn50v2
