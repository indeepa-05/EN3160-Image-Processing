import torch
import torchvision

print("PyTorch version:", torch.__version__)
print("TorchVision version:", torchvision.__version__)
print("CUDA runtime:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

    x = torch.randn(1000, 1000, device="cuda")
    y = x @ x

    print("GPU computation successful!")
    print("Result device:", y.device)
else:
    print("GPU unavailable - using CPU.")
