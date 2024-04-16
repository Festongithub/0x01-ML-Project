#!/usr/bin/python3
import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
    )
print("Using: {}".format(device))


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            )
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork()
print(model)

#x = torch.rand(1, 28, 28, device=device)
#logits = model(x)
#pred_probab = nn.Softmax(dim=1)(logits)
#y_pred =pred_probab.argmax(1)
#print("Predicted class:{}".format(y_pred))

#input_image = torch.rand(3, 28, 28)
#print(input_image.size())


#flatten the image
#flatten = nn.Flatten()
#flat_image = flatten(input_image)
#print(flat_image.size())

#nn.Linear linear layer is a module that applies a linear transformation on the inputs using its stored wieghts

#layer1 = nn.Linear(in_features=28*28, out_features=20)
#hidden1 = layer1(flat_image)
#print(hidden1.size())

#nn.Relu
#print("Before Relu: {}".format(hidden1))
#hidden1 = nn.ReLU()(hidden1)
#print("After Relu: {}".format(hidden1))

#nn.Sequential
#seq_modules = nn.Sequential(flatten, layer1, nn.ReLU(), nn.Linear(20,10))
#input_image = torch.rand(3, 28, 28)
#logits = seq_modules(input_image)

#nn.SoftMax
#softmax = nn.Softmax(dim=1)
#pred_probab = softmax(logits)

#print("Model structure:{}".format(model))

#for name, param in model.named_parameters():
    #print("Layer:{} | Size: {} | Values: {}".format(name, param.size(), param)#)