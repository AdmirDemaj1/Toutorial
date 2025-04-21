Link: https://www.youtube.com/watch?v=Z_ikDlimN6A&t=5044s
# Intoduction to Tensors

## PyTorch.Tensor

- torch.Tensor is the core data structure that forms the foundation of the PyTorch deep learning framework. It's similar to NumPy arrays but with added capabilities specifically designed for neural networks and deep learning.

- Why is it used?
Efficient Computation – Supports CPU and GPU acceleration for faster operations.
Automatic Differentiation – Used in deep learning for backpropagation. For `backpropagation` look this: https://www.ibm.com/think/topics/backpropagation
Flexible Operations – Supports mathematical operations like addition, multiplication, and matrix operations.


- What is a Tensor?
At its simplest, a tensor is a container for numbers. You can think of it as a generalization of vectors and matrices to potentially higher dimensions:

A 0-dimensional tensor is just a single number (a scalar)
A 1-dimensional tensor is a list of numbers (a vector)
A 2-dimensional tensor is a table of numbers (a matrix)
A 3-dimensional tensor would be a "cube" of numbers
And so on to higher dimensions

In PyTorch, the torch.Tensor class implements this concept with additional features designed specifically for deep learning.


```python
import torch

# A scalar (0D tensor)
scalar = torch.tensor(7)
print(scalar)  # tensor(7)

# A vector (1D tensor)
vector = torch.tensor([1, 2, 3])
print(vector)  # tensor([1, 2, 3])

# A matrix (2D tensor)
matrix = torch.tensor([[1, 2], [3, 4]])
print(matrix)  # tensor([[1, 2], [3, 4]])

# A 3D tensor
tensor_3d = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(tensor_3d)  # tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```


```python

x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Shape tells you the dimensions
print(x.shape)  # torch.Size([2, 2])

# Datatype (float32, int64, etc.)
print(x.dtype)  # torch.float32

# The device where it's stored (CPU or GPU)
print(x.device)  # cpu (or cuda:0 if on GPU)
```

- Under the hood a torch.Tensor is a `block of memory` storing the numerical data.
One of the most powerful features of PyTorch tensors is their ability to run on GPUs.
This is crucial because GPUs can perform thousands of simple calculations in parallel, making them much faster than CPUs for deep learning.


```python

# Scalar

scalaer = torch.tensor(7)

scalar #Output : tensor(7)

scalar.ndim ##Output : number of dimensions 0

# Get tensor back as Python int
scalar.item() # 7

# Vector
# A vector has magnitude(how far it is going) and direction(which way is it going)
vector = torch.tensor([7, 7])

vector.ndim # Output : 1

vector.shape # Output : torch.Size([2])

# MATRIX
MATRIX = torch.tensor([[7, 8],[9, 10]])

MATRIX.ndim # Output : 2

MATRIX[1] #  Output : tensor([9, 10])

MATRIX.shape # Output : torch.Size([2 , 2])

# TENSOR

TENSOR = torch.tensor([[[1, 2, 3], [3, 6, 9], [2, 4, 5]]])
TENSOR.shape # Output : torch.Size([1, 3, 3])
```

- Random Tensors
Random tensors are important because the way many neural networks learn is that they start with tensors full of
random numbers and then adjust those random numbers to better represent the data.

Start with random numbers --> look at data --> update random numbers --> look at data --> update random numbers

```python
random_tensor = torch.rand(3, 4)
random_tensor
 
```

## Reshaping, stacking, squeezing and unsqueezing tensors





