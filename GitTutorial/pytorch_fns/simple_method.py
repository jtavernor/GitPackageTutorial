import torch

def my_func():
    print('Successfully installed package with fixed environment')
    print('PyTorch was installed with cuda?:', torch.cuda.is_available())
    print('Using torch:', torch.randint(high=10, size=(1,)))