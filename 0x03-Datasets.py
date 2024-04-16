#!/usr/bin/python3

import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.transforms import ToTensor
from torchvision import datasets
from torchvision.io import read_image
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST (
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
    )

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
    )
class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotation_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform


    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_lables.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.targetr_transform:
            label = self.target_transform(label)
        return image, label



train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

#Iterate through the DataLaoder

train_features, train_labels = next(iter(train_dataloader))
print("{}".format(train_features.size()))
print("{}".format(train_labels.size()))

img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="blue")
plt.show()
print("Label: {}".format(label))
