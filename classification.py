# this is a residual file
import gradio as gr
import torch
import requests
from torchvision import transforms

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    i = 0
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
        confidences = {labels[i]: float(prediction[i] for i in range(1000))}
    return confidences


def classify():
    image = gr.inputs.Image(shape=(299, 299))
    label = gr.outputs.Label(num_top_classes=3)

    gr.Interface(fn=predict, inputs=image, outputs=label, capture_session=True).launch(share=True)

