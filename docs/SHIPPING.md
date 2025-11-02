# Shipping Guide

This guide outlines the steps required to ship the MNIST CNN Classifier project.

## Prerequisites

- GitHub account
- Docker Hub account
- Project code pushed to GitHub repository: https://github.com/harpertoken/mnist-cnn-classifier

## Steps to Ship

### 1. Set Up GitHub Secrets

In your GitHub repository:

1. Go to **Settings** > **Secrets and variables** > **Actions**
2. Add the following secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username
   - `DOCKER_PASSWORD`: Your Docker Hub password or access token

### 2. Trigger CI/CD Pipeline

The CI/CD pipeline is configured in `.github/workflows/ci.yml` and triggers on pushes to the `main` branch.

- Ensure your code is on the `main` branch.
- Push any changes to trigger the pipeline.
- The pipeline will:
  - Install dependencies
  - Train the model
  - Run tests
  - Build and push the Docker image to Docker Hub as `yourusername/cnn-mnist:latest`

### 3. Monitor CI/CD

- Go to the **Actions** tab in your GitHub repository.
- Check the status of the latest workflow run.
- Ensure all steps pass: test, train, validate, build, and push.

### 4. Deploy the Application

Once the Docker image is pushed to Docker Hub:

1. Pull the image:
   ```
   docker pull harpertoken/cnn-mnist:latest
   ```

2. Run the container:
   ```
   docker run -it harpertoken/cnn-mnist:latest
   ```

   This will execute the training, testing, and prediction pipeline inside the container.

### 5. Optional: Clean Up Git History with Rebase

If you need to clean up the commit history before shipping:

1. Ensure you're on the `main` branch:
   ```
   git checkout main
   ```

2. Fetch the latest changes:
   ```
   git fetch origin
   ```

3. Rebase interactively to squash or edit commits:
   ```
   git rebase -i origin/main
   ```
   - Follow the prompts to squash commits, edit messages, etc.

4. Force push the cleaned history (use with caution):
   ```
   git push origin main --force-with-lease
   ```

### 5.1 Handling Merges and Merge Conflicts

If working with multiple branches, follow these steps for merging:

1. Create and switch to a feature branch:
   ```
   git checkout -b feature-branch
   ```

2. Make changes and commit:
   ```
   git add .
   git commit -m "feat: add new feature"
   ```

3. Switch back to main and merge:
   ```
   git checkout main
   git merge feature-branch
   ```

4. If merge conflicts occur:
   - Git will indicate conflicted files.
   - Edit the conflicted files, resolve conflicts by choosing or combining changes.
   - Stage the resolved files:
     ```
     git add <resolved-file>
     ```
   - Complete the merge:
     ```
     git commit
     ```

5. Push the merged changes:
   ```
   git push origin main
   ```

6. Delete the feature branch:
   ```
   git branch -d feature-branch
   ```

For complex merges, consider using `git merge --no-ff` to preserve branch history.

### 6. Additional Requirements

- **Dependencies**: All required packages are listed in `requirements.txt` and `pyproject.toml`.
- **Environment**: The project runs in a Docker container with Python 3.8.
- **Model**: The CNN model is trained on MNIST and achieves ~98% accuracy.
- **Tests**: Unit and e2e tests are included and run in CI.
- **Linting**: Pre-commit hooks ensure code quality.

## Troubleshooting

- If CI fails, check the logs in GitHub Actions.
- Ensure Docker Hub credentials are correct.
- For local testing, use `run_all.sh` script.

## Final Notes

The project is now ready for deployment. The Docker image contains the full pipeline, so no additional setup is required on the deployment machine beyond Docker.
