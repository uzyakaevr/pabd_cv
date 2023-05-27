import os.path
import shutil
import PIL.Image
import click


# in_dir = 'data\\raw\\kaggle'
# out_dir = 'data\\processed\\PetImages'
# n_img = 20


@click.command()
@click.option('-i', '--in_dir', default='data\\raw\\kaggle')
@click.option('-o', '--out_dir', default='data\\processed\\PetImages')
@click.option('-n', '--n_img', default=20)
@click.option('-s', '--img_size', default=180)
def process_data(in_dir, out_dir, n_img, img_size):
    make_out_dir(out_dir)
    process_imgs(in_dir, out_dir, n_img, img_size)


def make_out_dir(out_dir):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)

    os.mkdir(out_dir)
    os.mkdir(os.path.join(out_dir, 'Cat'))
    os.mkdir(os.path.join(out_dir, 'Dog'))


def process_imgs(in_dir, out_dir, n_img, img_size):
    all_imgs = os.listdir(in_dir)
    cat_imgs = [img for img in all_imgs if img.startswith('cat')]
    dog_imgs = [img for img in all_imgs if img.startswith('dog')]

    def resize_and_save(img_list, category_name):
        for img_list in img_list[:n_img]:
            in_img_path = os.path.join(in_dir, img_list)
            img = PIL.Image.open(in_img_path)
            img_r = img.resize((img_size, img_size))
            out_img_path = os.path.join(out_dir, category_name, img_list)
            img_r.save(out_img_path)

    resize_and_save(cat_imgs, "Cat")
    resize_and_save(dog_imgs, "Dog")

if __name__ == '__main__':
    process_data()
