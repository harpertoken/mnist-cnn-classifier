import torch
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from model import SimpleCNN

def test_model_instantiation():
    model = SimpleCNN()
    assert isinstance(model, torch.nn.Module)

def test_forward_pass():
    model = SimpleCNN()
    model.eval()
    # Dummy input: batch_size=1, channels=1, height=28, width=28
    dummy_input = torch.randn(1, 1, 28, 28)
    with torch.no_grad():
        output = model(dummy_input)
    assert output.shape == (1, 10)  # 10 classes for MNIST
