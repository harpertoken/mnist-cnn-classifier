import torch
import torchvision.transforms as transforms
from PIL import Image
from model import SimpleCNN

# Device
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

model = SimpleCNN().to(device)
model.load_state_dict(torch.load('./models/cnn_model.pth'))
model.eval()

# Function to predict
def predict_digit(image_path):
    image = Image.open(image_path).convert('L')  # to grayscale
    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    image = transform(image).unsqueeze(0).to(device)  # add batch dim
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return predicted.item()

# Example usage: predict on a random test image
if __name__ == "__main__":
    import torchvision
    testset = torchvision.datasets.MNIST(root='./data', train=False, download=False)
    image, label = testset[0]  # first test image
    # Convert PIL to tensor
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    image_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
    print(f'Actual digit: {label}, Predicted digit: {predicted.item()}')
