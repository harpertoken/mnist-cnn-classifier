# CNN MNIST Project

A simple CNN for MNIST digit classification, trained from scratch.

## Setup

1. Create virtual environment: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Train model: `python src/train.py`
5. Test model: `python src/test.py`
6. Predict: `python src/predict.py`

## Understanding Key Concepts

### Git Branches

Git branches are parallel versions of your codebase. They allow you to work on features or fixes without affecting the main code.

- **Main Branch**: The primary branch (often `main` or `master`) where stable code lives.
- **How to Use**:
  - Create a new branch: `git checkout -b feature-branch`
  - Switch branches: `git checkout main`
  - Merge changes: `git merge feature-branch`
- In this project, push to `main` triggers CI and Docker push.

### Containers

Containers are lightweight, portable environments that package your app with all dependencies. Docker creates containers from images.

- **Benefits**: Run consistently across machines, isolate environments, easy deployment.
- **How to Choose**:
  - **Local**: For development, quick testing, or when you have Python installed. Use `./run_all.sh` for full workflow.
  - **Docker**: For production, sharing, or when you want isolation/portability. Use `docker run yourusername/cnn-mnist` after pulling the image.
- **How to Use**:
  - Build locally: `docker build -t cnn-mnist .`
  - Run: `docker run --rm cnn-mnist`
  - Pull from Docker Hub: `docker pull yourusername/cnn-mnist`

Choose local for experimentation, Docker for deployment.

## Sharing and Deployment

### GitHub

1. Create a new repository on GitHub.
2. Push the code: `git remote add origin <repo-url> && git push -u origin main`
3. Set up secrets in GitHub repo settings:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub password or access token
4. The CI workflow will run on push, testing and pushing Docker image to Docker Hub.

### Docker Hub

The CI automatically builds and pushes the image to `yourusername/cnn-mnist:latest` on successful tests.

To run locally: `docker run yourusername/cnn-mnist`

## Conventional Commits

This project uses conventional commit standards.

### Setup Hook

To enable commit message validation:

```bash
cp scripts/commit-msg .git/hooks/commit-msg
```

### Commit Types

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `style:` formatting
- `refactor:` code refactor
- `test:` testing
- `chore:` maintenance
- `perf:` performance
- `ci:` CI/CD
- `build:` build system
- `revert:` revert

### Rules

- First line: lowercase, ≤60 chars, starts with type:
- Example: `feat: add new cnn model`

### Rewriting History

To clean up existing commits:

```bash
git filter-branch --msg-filter 'bash scripts/rewrite_msg.sh' -- --all
git push --force
```

Use with caution.
