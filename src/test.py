import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from model import SimpleCNN

# Device
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

model = SimpleCNN().to(device)
model.load_state_dict(torch.load('./models/cnn_model.pth'))
model.eval()

# Data
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = DataLoader(testset, batch_size=32, shuffle=False)

# Test
correct = 0
total = 0
with torch.no_grad():
    for data in testloader:
        images, labels = data[0].to(device), data[1].to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy on test set: {100 * correct / total:.2f}%')
