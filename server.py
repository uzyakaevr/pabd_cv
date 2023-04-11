from flask import Flask, request
import torch
import torchvision
from torchvision.models import resnet101, ResNet101_Weights

resnet = resnet101(weights=ResNet101_Weights.DEFAULT, progress=False)
resnet.eval()
preprocess_img = ResNet101_Weights.DEFAULT.transforms()
cats_en = ResNet101_Weights.DEFAULT.meta["categories"]

app = Flask('Image classifier')


@app.route('/')
def home():
    return 'Home page'


@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_data()
    jpg_tensor = torch.frombuffer(data, dtype=torch.uint8)
    img = torchvision.io.decode_image(jpg_tensor)
    assert type(img) == torch.Tensor
    assert len(img.shape) == 3

    img_p = preprocess_img(img).unsqueeze(dim=0)
    out = resnet(img_p)
    idxs = out.argsort()[0][:3]
    result = ', '.join([cats_en[int(i)] for i in idxs])
    return result


if __name__ == '__main__':
    app.run()
    input()
