import click
import keras
import tensorflow as tf
from model import make_model

from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.applications.xception import preprocess_input  

@click.command()
@click.option('-i', '--in_dir', default="data\\processed\\PetImages")
@click.option('-o', '--out_dir', default="models\\my_model")
@click.option('-e', '--epochs', default=5)
@click.option('-l', '--lr', default=1e-3)
@click.option('-b', '--batch_size', default=64)
@click.option('-s', '--image_size', default=180)
def train(in_dir, out_dir, epochs, lr, batch_size, image_size):
    image_size = (image_size, image_size)
    train_model(in_dir, out_dir, epochs, lr, batch_size, image_size)


def train_model(in_dir, out_dir, epochs, lr, batch_size, image_size):
    
    train_dir = 'data\\processed\\PetImages\\train'
    val_dir = 'data\\processed\\PetImages\\test'

    train_data_gen = ImageDataGenerator(preprocessing_function=preprocess_input,
                                    rotation_range=10,
                                    zoom_range=0.1,
                                    horizontal_flip=True)

    train_ds = train_data_gen.flow_from_directory(train_dir,
                                                     target_size=image_size,
                                                     batch_size=batch_size,
                                                     class_mode='categorical')
    
    val_data_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

    val_ds = val_data_gen.flow_from_directory(val_dir,
                                                 target_size=image_size,
                                                 batch_size=batch_size,
                                                 class_mode='categorical')

    model = make_model(input_shape=image_size + (3,), num_classes=2)


    callbacks = [
        # keras.callbacks.ModelCheckpoint("save_at_{epoch}.keras"),
    ]

    model.compile(
        optimizer="Adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    model.fit(
        train_ds,
        epochs=epochs,
        callbacks=callbacks,
        validation_data=val_ds,
    )

    model.save(out_dir)


if __name__ == '__main__':
    train()
