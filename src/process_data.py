"""Preprocess data to use it as tf dataset.
Take images from source dir and put in out dir subfolders: Cat and Dog"""
import os
import shutil

import click

# in_dir = 'data\\raw\\kaggle'
# out_dir = 'data\\processed\\PetImages'

@click.command()
@click.option('-i', '--in_dir', default='data\\raw\\kaggle')
@click.option('-o', '--out_dir', default='data\\processed\\PetImages')
def preprocess_data(in_dir, out_dir):
    # make_out_dirs(out_dir)
    copy_files(in_dir, out_dir)


def make_out_dirs(out_dir):
    if os.path.exists(out_dir):
        os.remove(out_dir)
        os.mkdir(out_dir)

    os.mkdir(os.path.join(out_dir, 'Cat'))
    os.mkdir(os.path.join(out_dir, 'Dog'))


def copy_files(in_dir, out_dir):
    all_files = os.listdir(in_dir)

    for img_name in all_files:
        if img_name.startswith('cat'):
            shutil.copy2(
                os.path.join(in_dir, img_name),
                os.path.join(out_dir, 'Cat'))

        if img_name.startswith('dog'):
            shutil.copy2(
                os.path.join(in_dir, img_name),
                os.path.join(out_dir, 'Dog'))


if __name__ == '__main__':
    preprocess_data()
