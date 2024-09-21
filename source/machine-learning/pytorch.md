# PyTorch

## Commands

- [torch.Tensor.item()](https://pytorch.org/docs/stable/generated/torch.Tensor.item.html)
  - convert tensor to standard Python number
  - only works for tensors with one element - otherwise an exception is raised
  - implicitly moves the value to the CPU

## shape

Example:

```python
batch_size, sequence_length = attention_mask.shape
```
