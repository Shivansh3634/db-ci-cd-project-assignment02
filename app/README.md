# PROG8860 - CI/CD Pipeline Assignment

## Technologies Used
- Python Flask
- Docker
- GitHub Actions

## Steps to Implement the Pipeline
1. Created a Python Flask app.
2. Wrote test cases using unittest.
3. Created a Dockerfile to containerize the app.
4. Set up GitHub Actions workflow triggered on Pull Requests.
5. Workflow builds the app, runs tests, builds and runs Docker container, then stops it.

## CI Pipeline Stages
- **Build:** Docker image build.
- **Test:** Python unit tests.
- **Containerize:** Docker container build and run.
- **Clean-up:** Stop and remove Docker container.
