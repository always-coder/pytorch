import torch
from torch import nn

def main():
    gpu_available = torch.cuda.is_available()
    print(gpu_available)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(device)

    print(torch.cuda.current_device())
    print(torch.cuda.get_device_name(0))

if __name__ == '__main__':
    main()
