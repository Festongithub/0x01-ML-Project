#!/usr/bin/python3

import torch

tensor = torch.rand(3,4)

print("Tensor shape: {}".format(tensor.shape))
print("Tensor  data type: {}".format(tensor.dtype))
print("Device tensor is stored on: {}".format(tensor.device))


t = torch.ones(9)
print("t :{}", t)
n = t.numpy()
print("{}".format(n))

t.add_(1)
print("t :{}".format(t))
print("{}".format(n))

# Numpy to Tensor

n = np.ones(5)
t = torch.from_numpy(n)
# changes in the Numpyarray reflect in the tensor

np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")
