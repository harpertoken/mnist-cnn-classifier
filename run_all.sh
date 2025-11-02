#!/bin/bash

# Single source of truth script for the complete CNN MNIST workflow
# Usage: ./run_all.sh [docker]

set -e  # Exit on error

# Detect if running in Docker
if [ -f /.dockerenv ]; then
    MODE=docker
else
    MODE=${1:-local}  # Default to local
fi

echo "Starting CNN MNIST workflow..."

if [ "$MODE" != "docker" ]; then
    # Local mode: setup venv
    echo "Running in local mode..."

    # Check if venv exists, create if not
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi

    # Activate venv
    source venv/bin/activate

    # Install dependencies
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "Running in Docker mode..."
fi

# Download dataset if not present
echo "Ensuring dataset is available..."
python -c "import ssl; ssl._create_default_https_context = ssl._create_unverified_context; import torchvision; torchvision.datasets.MNIST(root='./data', train=True, download=True); torchvision.datasets.MNIST(root='./data', train=False, download=True)"

# Train the model
echo "Training the model..."
python src/train.py

# Test the model
echo "Testing the model..."
python src/test.py

# Run unit and e2e tests
echo "Running tests..."
python -m pytest tests/

# Create version file
echo "Creating version file..."
if [ "$MODE" = "docker" ]; then
    VERSION=${VERSION:-v1.0.0}
else
    read -p "Enter version (default v1.0.0): " VERSION
    VERSION=${VERSION:-v1.0.0}
fi
echo "$VERSION" > version.txt
echo "Model trained and tested successfully. Version: $(cat version.txt)"

echo "Workflow completed!"
