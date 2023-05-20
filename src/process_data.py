import os.path
import shutil

import click


# in_dir = 'data\\raw\\kaggle'
# out_dir = 'data\\processed\\PetImages'
# n_img = 20


@click.command()
@click.option('-i', '--in_dir', default='data\\raw\\kaggle')
@click.option('-o', '--out_dir', default='data\\processed\\PetImages')
@click.option('-n', '--n_img', default=20)
def process_data(in_dir, out_dir, n_img):
    # make_out_dir(out_dir)
    copy_imgs(in_dir, out_dir, n_img)


def make_out_dir(out_dir):
    if os.path.exists(out_dir):
        os.remove(out_dir)
        os.mkdir(out_dir)
        os.mkdir(os.path.join(out_dir, 'Cat'))
        os.mkdir(os.path.join(out_dir, 'Dog'))


def copy_imgs(in_dir, out_dir, n_img):
    all_imgs = os.listdir(in_dir)
    cat_imgs = [img for img in all_imgs if img.startswith('cat')]
    dog_imgs = [img for img in all_imgs if img.startswith('dog')]


    for cat_img in cat_imgs[:n_img]:
        shutil.copy2(
            os.path.join(in_dir, cat_img),
            os.path.join(out_dir, "Cat")
        )

    for dog_img in dog_imgs[:n_img]:
        shutil.copy2(
            os.path.join(in_dir, dog_img),
            os.path.join(out_dir, "Dog")
        )


if __name__ == '__main__':
    process_data()
