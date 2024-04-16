#!/usr/bin/python3

import torch

x = torch.ones(5)
y = torch.zeros(3)
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

print("Gradient function for z :{}".format(z.grad_fn))
print("Gradient function loss: x{}".format(loss.grad_fn))

#Gradient
loss.backward()
print("Gradient for w is :{}".format(w.grad))
print("Gradient for b is : {}".format(b.grad))

z = torch.matmul(x, w)+b
print(z.requires_grad)

with torch.no_grad():
    z = torch.matmul(x,w)+b
print(z.requires_grad)
